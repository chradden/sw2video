import streamlit as st
import os
from PIL import Image
import tempfile
from colorizer import colorize_image
from animator import animate_image
import base64

st.set_page_config(page_title="🎨📽️ Alte Fotos lebendig machen", layout="centered")
st.title("🖼️➡️🎨➡️🎞️ Schwarz-Weiß zu Farb-Video")

uploaded_file = st.file_uploader("📎 Lade ein Schwarz-Weiß-Bild hoch", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Original (Schwarz-Weiß)", use_column_width=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("🎨 Koloriere Bild..."):
        color_path = colorize_image(tmp_path)
        st.image(color_path, caption="Koloriertes Bild", use_column_width=True)

    with st.spinner("🎞️ Erzeuge animiertes Video..."):
        video_path = animate_image(color_path)

    st.video(video_path)

    with open(video_path, "rb") as f:
        video_bytes = f.read()
        b64 = base64.b64encode(video_bytes).decode()
        href = f'<a href="data:video/mp4;base64,{b64}" download="lebendiges_foto.mp4">📥 Video herunterladen</a>'
        st.markdown(href, unsafe_allow_html=True)