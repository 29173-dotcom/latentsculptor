import streamlit as st
import streamlit.components.v1 as components
import os

# ตั้งค่าหน้าเว็บ Streamlit
st.set_page_config(
    page_title="Latent Sculptor — Neuromotor Kinematic Assessment",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ซ่อน Streamlit Header / Padding ส่วนเกิน เพื่อให้แสดงผลแบบเต็มหน้าจอ (Full Screen)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# อ่านไฟล์ index.html
html_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # เรนเดอร์ไฟล์ HTML โดยตรงใน Streamlit พร้อมรองรับการเปิดกล้องและ WebGL
    components.html(html_code, height=980, scrolling=True)
else:
    st.error("⚠️ ไม่พบไฟล์ index.html กรุณาตรวจสอบตำแหน่งไฟล์")