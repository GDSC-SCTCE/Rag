import streamlit as st
class GetTheFreakingWatermarkOut:
    """
    Streamlit deployment watermark remover 
    """
    def __init__(self):
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
