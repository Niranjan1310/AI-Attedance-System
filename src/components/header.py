import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:2rem; margin-top:1rem">
            <img src='{logo_url}' style='height:90px; filter: drop-shadow(0 4px 10px rgba(79, 70, 229, 0.2));' />
            <h1 style='text-align:center; color:#1E293B; margin-top: 12px; font-weight: 800; font-size: 2.5rem; letter-spacing: -0.03em;'>SNAP CLASS</h1>
            <p style='color:#64748B; font-size: 1rem; font-weight: 500; margin-top: 4px; text-align: center;'>Smart Facial & Voice Attendance System</p>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:12px; padding: 12px 0;">
            <img src='{logo_url}' style='height:60px;' />
            <div>
                <h2 style='text-align:left; color:#1E293B; margin:0; font-weight:800; font-size:1.75rem; letter-spacing:-0.02em;'>SNAP CLASS</h2>
                <p style='color:#64748B; font-size:0.85rem; font-weight:500; margin:0;'>AI Attendance Dashboard</p>
            </div>
        </div>   
    """, unsafe_allow_html=True)


