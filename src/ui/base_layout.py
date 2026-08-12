import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background: linear-gradient(180deg, #EEF2FF 0%, #E0E7FF 100%) !important;
                    background-attachment: fixed !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #FFFFFF !important;
                    padding: 2.25rem !important;
                    border-radius: 1.25rem !important;
                    box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.08), 0 8px 10px -6px rgba(79, 70, 229, 0.04) !important;
                    border: 1px solid #E2E8F0 !important;
                    transition: all 0.25s ease !important;
                }
                
                .stApp div[data-testid="stColumn"]:hover {
                    border-color: #C7D2FE !important;
                    box-shadow: 0 20px 30px -10px rgba(79, 70, 229, 0.12) !important;
                }
        </style>  
                """, unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp {
                    background: #F8FAFC !important;
                    background-attachment: fixed !important;
                }
        </style>  
                """, unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top: 1.5rem !important;    
                max-width: 960px !important;
            }

            /* Contrast & Text Hierarchy */
            h1, h2, h3, h4, h5, h6 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                color: #0F172A !important;
            }

            h1 {
                font-weight: 800 !important;
                font-size: 2.5rem !important;
                letter-spacing: -0.02em !important;
                line-height: 1.15 !important;
            }

            h2 {
                font-weight: 700 !important;
                font-size: 1.75rem !important;
                letter-spacing: -0.01em !important;
                line-height: 1.2 !important;
            }

            h3 {
                font-weight: 700 !important;
                font-size: 1.35rem !important;
                color: #0F172A !important;
            }

            p, label {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                color: #334155 !important;
            }

            /* Card Column Specific Text Contrast */
            div[data-testid="stColumn"] h1,
            div[data-testid="stColumn"] h2,
            div[data-testid="stColumn"] h3,
            div[data-testid="stColumn"] h4 {
                color: #0F172A !important;
            }

            div[data-testid="stColumn"] p,
            div[data-testid="stColumn"] span {
                color: #475569 !important;
            }

            /* Button Styling without layout breaking */
            button {
                border-radius: 0.75rem !important;
                background-color: #4F46E5 !important;
                border: none !important;
                box-shadow: 0 2px 6px rgba(79, 70, 229, 0.25) !important;
                transition: all 0.2s ease !important;
            }

            button p, button span {
                color: #FFFFFF !important;
                font-weight: 600 !important;
            }

            button[kind="secondary"] {
                background-color: #0F172A !important;
            }
            button[kind="secondary"] p, button[kind="secondary"] span {
                color: #FFFFFF !important;
            }

            button[kind="tertiary"] {
                background-color: #F1F5F9 !important;
                border: 1px solid #E2E8F0 !important;
                box-shadow: none !important;
            }
            button[kind="tertiary"] p, button[kind="tertiary"] span {
                color: #334155 !important;
            }

            button:hover {
                transform: translateY(-1px) !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
            }

            button:active {
                transform: translateY(0px) !important;
            }
        </style>  
                """, unsafe_allow_html=True)
