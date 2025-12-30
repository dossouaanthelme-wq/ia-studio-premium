import streamlit as st
from supabase import create_client, Client
import replicate

# --- CONFIGURATION SUPABASE ---
URL_SB = "https://divgvkxzpgrykggmehnu.supabase.co"
KEY_SB = "sb_publishable_Wbo5zWMMsIxhygE_GitTRQ_8g2EyTlk"
supabase: Client = create_client(URL_SB, KEY_SB)

st.set_page_config(page_title="IA Studio Premium", page_icon="💎")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .auth-card { background-color: #161b22; padding: 30px; border-radius: 15px; border: 1px solid #30363d; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'AUTHENTIFICATION ---
if 'user' not in st.session_state:
    st.session_state.user = None

def login_page():
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.title("💎 IA Studio Premium")
    
    tab_login, tab_signup = st.tabs(["Connexion", "Créer un compte"])
    
    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")
        if st.button("Se connecter"):
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state.user = res.user
                st.rerun()
            except:
                st.error("Identifiants incorrects.")
        st.button("Continuer avec Google (Bientôt)", disabled=True)

    with tab_signup:
        new_email = st.text_input("Votre Email", key="reg_email")
        new_password = st.text_input("Choisir un mot de passe", type="password", key="reg_pass")
        if st.button("S'inscrire"):
            try:
                res = supabase.auth.sign_up({"email": new_email, "password": new_password})
                st.success("Compte créé ! Vérifiez vos emails pour confirmer, puis connectez-vous.")
            except Exception as e:
                st.error(f"Erreur : {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE PRINCIPALE (APRÈS CONNEXION) ---
if st.session_state.user is None:
    login_page()
else:
    st.sidebar.title(f"👤 {st.session_state.user.email}")
    if st.sidebar.button("Déconnexion"):
        supabase.auth.sign_out()
        st.session_state.user = None
        st.rerun()

    st.title("🎨 Votre Studio Créatif")
    
    # --- SECTION PAIEMENT ---
    with st.expander("💳 Recharger vos crédits (Paiement Automatisé)"):
        st.write("Envoyez votre paiement par **Wave ou Orange Money** au : **05 54 17 81 28**")
        st.info("Une fois payé, vos crédits seront activés sous 5 minutes après vérification de votre email.")
    
    # --- OUTILS IA ---
    t1, t2 = st.tabs(["🎥 Vidéo HD", "📸 Photo Pro"])
    with t1:
        prompt_v = st.text_area("Décrivez votre vidéo...")
        if st.button("Générer Vidéo"):
            # Ici votre logique Replicate habituelle
            st.info("Traitement en cours...")
