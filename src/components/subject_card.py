import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; border-left: 5px solid #4F46E5; padding: 20px 24px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #E2E8F0; margin-bottom: 16px;">
        <h3 style="margin: 0; color: #0F172A; font-size: 1.25rem; font-weight: 700;">{name}</h3>
        <p style="color: #64748B; margin: 6px 0 12px 0; font-size: 0.9rem;">
            Code : <span style="background: #EEF2FF; color: #4F46E5; padding: 2px 8px; border-radius: 6px; font-weight: 600; font-size: 0.82rem;">{code}</span> 
            &nbsp;|&nbsp; Section : <b style="color: #334155;">{section}</b>
        </p>
        """
    
    if stats:
        html+= """
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 4px 12px; border-radius: 8px; font-size: 0.85rem; color: #475569;">{icon} <b style="color: #0F172A;">{value}</b> {label}</div>'
        
        html+= "</div>"
    
    html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

