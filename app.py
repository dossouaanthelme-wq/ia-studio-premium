import streamlit as st
from supabase import create_client, Client
import replicate
import os

# --- CONFIGURATION SECRÈTE (Utilisez st.secrets en production) ---
# Pour tester en local, remplacez par vos vraies valeurs
URL_SB = "https://divgvkxzpgrykggmehnu.supabase.co"
KEY_SB = "VOTRE_CLE_SUPABASE_ICI" 
supabase: Client = create_client(URL_SB, KEY_SB)

# --- CONFIGURATION PAGE & DESIGN ---
st.set_page_config(page_title="IA Studio Premium", page_icon="💎", layout="centered")

# CSS pour masquer le menu Streamlit, le footer et le header "Share"
st.markdown("""
    <style>
    /* Masquer les éléments Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Design Premium */
    .stApp { background-color: #0e1117; }
    .auth-card { 
        background-color: #161b22; 
        padding: 40px; 
        border-radius: 20px;
        border: 1px solid #30363d;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE D'AUTHENTIFICATION ---
if 'user' not in st.session_state:
    st.session_state.user = None

def login():
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.title("💎 IA Studio Premium")
    st.subheader("Connexion sécurisée")
    
    email = st.text_input("Adresse e-mail")
    password = st.text_input("Mot de passe", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Se connecter", use_container_width=True):
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state.user = res.user
                st.rerun()
            except Exception as e:
                st.error("Identifiants incorrects ou compte non vérifié.")
                
    with col2:
        if st.button("Créer un compte", use_container_width=True):
            st.info("Redirection vers l'inscription...")
            # Ajoutez ici supabase.auth.sign_up si vous voulez l'automatiser
    st.markdown('</div>', unsafe_allow_html=True)

# --- AFFICHAGE DE L'APP ---
if st.session_state.user is None:
    login()
else:
    # Interface principale après connexion
    st.sidebar.success(f"Connecté : {st.session_state.user.email}")
    if st.sidebar.button("Déconnexion"):
        st.session_state.user = None
        st.rerun()
        
    st.title("Tableau de bord IA")
    # Votre logique Replicate ici...
    prompt = st.text_area("Que voulez-vous créer ?")
    if st.button("Générer l'image"):
        st.write("Génération en cours...")
