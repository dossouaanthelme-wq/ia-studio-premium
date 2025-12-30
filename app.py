import streamlit as st

# --- CONFIGURATION VISUELLE ---
st.set_page_config(page_title="IA Studio Premium - Connexion", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .auth-container {
        background-color: #161b22;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
    }
    .stButton>button { width: 100%; border-radius: 5px; height: 45px; font-weight: bold; }
    .google-btn {
        background-color: white !important;
        color: #000 !important;
        border: 1px solid #ddd !important;
    }
    .signup-link { color: #58a6ff; text-decoration: none; font-size: 0.9em; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    with st.container():
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.title("Bienvenue")
        st.write("Connectez-vous à votre compte IA Studio")
        
        # OPTION 1: GOOGLE
        if st.button("S'identifier avec Google", key="google", help="Continuer avec Google"):
            st.info("La connexion Google est en cours de maintenance. Utilisez votre code VIP.")

        st.markdown("--- OU ---")
        
        # OPTION 2: EMAIL / PASS
        email = st.text_input("Adresse e-mail")
        password = st.text_input("Mot de passe (Code VIP)", type="password")
        
        if st.button("Se connecter"):
            if password == "MASTER2025": # Votre code actuel
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Identifiants incorrects.")
        
        # OPTION 3: INSCRIPTION
        st.markdown("""
            <p style='margin-top:20px;'>Vous n'avez pas de compte ? 
            <a href='https://wa.me/2250554178128' class='signup-link'>S'inscrire / Créer un compte</a></p>
            <p><a href='#' class='signup-link'>Mot de passe oublié ?</a></p>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- RESTE DU CODE (Génération Vidéo/Photo) ---
st.success("Connecté avec succès !")
# (Le reste du code de génération suit ici...)
