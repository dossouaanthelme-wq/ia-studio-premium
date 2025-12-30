import streamlit as st
from supabase import create_client, Client
import replicate
import os

# --- CONFIGURATION SUPABASE ---
URL_SB = "https://divgvkxzpgrykggmehnu.supabase.co"
KEY_SB = "sb_publishable_Wbo5zWMMsIxhygE_GitTRQ_8g2EyTlk"
supabase: Client = create_client(URL_SB, KEY_SB)

# --- CONFIGURATION PAGE ---
st.set_page_config(page_title="IA Studio Premium", page_icon="💎", layout="centered")

# --- STYLE CSS (DARK MODE PREMIUM) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .auth-card { 
        background-color: #161b22; 
        padding: 30px; 
        border-radius: 15px; 
        border: 1px solid #30363d;
        text-align: center;
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
    }
    .main-btn { background-color: #238636 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Initialisation de la session
if 'user' not in st.session_state:
    st.session_state.user = None

# --- FONCTION : RECUPERER LES CREDITS ---
def get_user_credits(user_id):
    try:
        res = supabase.table("profiles").select("credits").eq("id", user_id).single().execute()
        return res.data['credits'] if res.data else 0
    except:
        return 0

# --- PAGE D'AUTHENTIFICATION ---
def auth_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("💎 IA Studio")
        
        tab_login, tab_signup = st.tabs(["Se connecter", "Créer un compte"])
        
        with tab_login:
            email = st.text_input("Email", key="l_email")
            password = st.text_input("Mot de passe", type="password", key="l_pass")
            if st.button("Connexion", type="primary"):
                try:
                    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                    st.session_state.user = res.user
                    st.rerun()
                except:
                    st.error("Identifiants incorrects.")

        with tab_signup:
            new_email = st.text_input("Votre Email", key="s_email")
            new_password = st.text_input("Mot de passe", type="password", key="s_pass")
            if st.button("S'inscrire"):
                try:
                    supabase.auth.sign_up({"email": new_email, "password": new_password})
                    st.success("✅ Compte créé ! Connectez-vous maintenant.")
                except Exception as e:
                    st.error(f"Erreur : {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE PRINCIPALE DU STUDIO ---
def main_studio():
    user = st.session_state.user
    credits = get_user_credits(user.id)
    
    # Sidebar
    st.sidebar.title("👤 Mon Espace")
    st.sidebar.metric(label="Mes Crédits", value=f"{credits} 🎥")
    
    if st.sidebar.button("Se déconnecter"):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()

    st.title("🎨 Studio Créatif IA")
    
    # Section Paiement si crédits = 0
    if credits <= 0:
        st.warning("🚨 Votre solde est de 0 crédit.")
        with st.expander("💳 COMMENT ACHETER DES CRÉDITS ?"):
            st.write("1. Envoyez votre paiement (Wave/Orange) au **05 54 17 81 28**")
            st.write("2. Envoyez la capture d'écran sur WhatsApp avec votre email.")
            st.link_button("Contacter le support WhatsApp", "https://wa.me/2250554178128")
    
    # Zone de travail
    tab1, tab2 = st.tabs(["🎥 Générer une Vidéo", "📸 Générer une Image"])
    
    with tab1:
        st.subheader("Vidéo Haute Définition")
        p_video = st.text_area("Décrivez votre vidéo...", placeholder="Une vue aérienne d'Abidjan la nuit...")
        
        if st.button("Lancer la création (1 crédit)", type="primary", disabled=(credits <= 0)):
            st.info("🔄 Connexion au serveur Replicate... Veuillez patienter.")
            # La logique de génération Replicate viendra ici
            
    with tab2:
        st.subheader("Image Ultra-Réaliste")
        p_image = st.text_area("Décrivez l'image...", placeholder="Un chef cuisinier africain dans un restaurant de luxe...")
        
        if st.button("Générer l'image (1 crédit)", disabled=(credits <= 0)):
            st.info("🔄 Traitement de l'image en cours...")

# --- AFFICHAGE ---
if st.session_state.user is None:
    auth_page()
else:
    main_studio()
