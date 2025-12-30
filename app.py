import streamlit as st
from supabase import create_client, Client
import replicate

# --- CONFIGURATION SUPABASE ---
URL_SB = "https://divgvkxzpgrykggmehnu.supabase.co"
KEY_SB = "sb_publishable_Wbo5zWMMsIxhygE_GitTRQ_8g2EyTlk"
supabase: Client = create_client(URL_SB, KEY_SB)

st.set_page_config(page_title="IA Studio Premium", page_icon="💎", layout="centered")

# --- STYLE CSS (STYLE VEXUB) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .auth-card { 
        background-color: #161b22; 
        padding: 40px; 
        border-radius: 15px; 
        border: 1px solid #30363d;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 48px;
        font-weight: bold; 
        background-color: #238636;
        color: white;
    }
    .google-btn {
        background-color: #ffffff !important;
        color: #000000 !important;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'user' not in st.session_state:
    st.session_state.user = None

# --- PAGE D'AUTHENTIFICATION ---
def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("💎 IA Studio")
        st.write("L'excellence de l'IA en Afrique")
        
        tab_login, tab_signup = st.tabs(["Se connecter", "S'inscrire"])
        
        with tab_login:
            st.button("🚀 Continuer avec Google", key="google_ui", disabled=True)
            st.markdown("<p style='text-align:center'>ou avec votre email</p>", unsafe_allow_html=True)
            email = st.text_input("Email", key="l_email")
            password = st.text_input("Mot de passe", type="password", key="l_pass")
            
            if st.button("Connexion"):
                try:
                    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                    st.session_state.user = res.user
                    st.rerun()
                except:
                    st.error("Identifiants incorrects ou compte non confirmé.")

        with tab_signup:
            new_email = st.text_input("Votre Email", key="s_email")
            new_password = st.text_input("Créer un mot de passe", type="password", key="s_pass")
            if st.button("Créer mon compte"):
                try:
                    supabase.auth.sign_up({"email": new_email, "password": new_password})
                    st.success("✅ Compte créé ! Connectez-vous maintenant dans l'onglet 'Se connecter'.")
                except Exception as e:
                    st.error(f"Erreur : {e}")
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE DU STUDIO (APRES CONNEXION) ---
if st.session_state.user is None:
    login_page()
else:
    # Barre latérale
    st.sidebar.title("💎 Studio Premium")
    st.sidebar.write(f"Utilisateur : {st.session_state.user.email}")
    if st.sidebar.button("Déconnexion"):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()

    # Corps de l'application
    st.title("🎨 Bienvenue dans votre Studio")
    
    with st.expander("💳 ACTIVER MON COMPTE / RECHARGER"):
        st.write("Pour obtenir des crédits de génération :")
        st.write("1. Envoyez votre paiement par **Wave** au **05 54 17 81 28**")
        st.write("2. Envoyez la capture d'écran sur WhatsApp avec votre email.")
        st.link_button("Envoyer le reçu sur WhatsApp", "https://wa.me/2250554178128")

    # Onglets de création
    t1, t2 = st.tabs(["🎥 Création Vidéo HD", "📸 Photographie Pro"])
    
    with t1:
        st.subheader("Générateur de Vidéo IA")
        prompt = st.text_area("Décrivez la scène que vous voulez créer...", placeholder="Un astronaute qui marche sur Mars au coucher du soleil...")
        if st.button("Lancer la génération vidéo"):
            st.warning("⚠️ Solde insuffisant. Veuillez recharger votre compte.")

    with t2:
        st.subheader("Générateur d'Images Studio")
        prompt_i = st.text_area("Décrivez l'image...", placeholder="Un portrait cinématographique d'un lion avec une couronne...")
        if st.button("Générer l'image"):
            st.warning("⚠️ Solde insuffisant. Veuillez recharger votre compte.")
