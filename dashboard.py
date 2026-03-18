import streamlit as st

# Configura a página para o modo "Wide" (Largo)
st.set_page_config(layout="wide", page_title="Dashboard TV")

# CSS para transformar o Streamlit em um "Player" de tela cheia
st.markdown("""
    <style>
    /* Esconde menus e rodapés do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove as margens das laterais e do topo */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    
    /* Faz o vídeo ocupar a largura total disponível */
    video {
        width: 100vw;
        height: auto;
        max-height: 100vh;
        object-fit: contain;
        background-color: black;
    }
    
    /* Fundo preto para não cansar a vista na TV */
    .stApp {
        background-color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# Caminho para o vídeo dentro da pasta data
video_path = 'data/IndicadoresTV.mp4'

try:
    with open(video_path, 'rb') as v_file:
        video_bytes = v_file.read()
    
    # Exibe o vídeo:
    # loop=True (recomeça sozinho)
    # autoplay=True (inicia sozinho)
    # muted=True (obrigatório para autoplay funcionar na maioria das TVs)
    st.video(video_bytes, format="IndicadoresTV/mp4", loop=True, autoplay=True, muted=True)

except FileNotFoundError:
    st.error("Erro: O arquivo 'data/IndicadoreTV.mp4' não foi encontrado.")
