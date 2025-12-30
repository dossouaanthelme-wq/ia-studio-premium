import streamlit as st
import replicate

# --- CONFIGURATION SÉCURISÉE ---
VOTRE_NUMERO_WA = "2250554178128"
CODE_ACCES_MASTER = "MASTER2025"

st.set_page_config(page_title="IA Studio Premium", page_icon="💎", layout="wide")

# --- STYLE INTERFACE PREMIUM ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #007bff; color: white; font-weight: bold; }
    .description-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- SYSTÈME DE CONNEXION ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("🔐 Accès Studio Premium")
    st.markdown("""
    <div class="description-box">
        <h3>L'Excellence de l'Intelligence Artificielle.</h3>
        <p>Générez des vidéos cinématographiques et des photos ultra-réalistes en quelques secondes.</p>
    </div>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Identifiant (Email)")
    password = st.text_input("Code d'accès VIP", type="password")
    
    if st.button("Se connecter au Studio"):
        if password == CODE_ACCES_MASTER:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Code d'accès incorrect.")
    
    st.markdown(f"[📲 OBTENIR UN CODE (Payer par Wave)](https://wa.me/{VOTRE_NUMERO_WA})")
    st.stop()

# --- INTERFACE DE GÉNÉRATION ---
st.title("🚀 Studio Premium Actif")
tab1, tab2 = st.tabs(["🎥 VIDÉO HD", "📸 PHOTO PRO"])

with tab1:
    st.header("Générateur Vidéo")
    # Votre vidéo de démo
    st.video("https://youtu.be/q3xaGATnLHk")
    prompt_v = st.text_area("Description de la vidéo :")
    if st.button("Lancer la Production Vidéo"):
        try:
            client = replicate.Client(api_token=st.secrets["REPLICATE_API_TOKEN"])
            with st.spinner("IA en action..."):
                output = client.run("luma/ray", input={"prompt": prompt_v})
                st.video(output)
        except:
            st.error("Solde Replicate insuffisant.")

with tab2:
    st.header("Générateur Photo")
    prompt_p = st.text_area("Description de l'image :")
    if st.button("Générer la Photo"):
        try:
            client = replicate.Client(api_token=st.secrets["REPLICATE_API_TOKEN"])
            with st.spinner("Création..."):
                output = client.run("black-forest-labs/flux-schnell", input={"prompt": prompt_p})
                st.image(output[0])
        except:
            st.error("Erreur de crédit.")
