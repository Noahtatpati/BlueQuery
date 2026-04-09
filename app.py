import streamlit as st
import random
import time
from model import generate_sql
from database import run_query
import os

if not os.path.exists("data.db"):
    import setup_db
    
st.set_page_config(page_title="BlueQuery", layout="centered")



st.markdown("""
<style>
.stApp {
    transition: background-color 0.4s ease, color 0.4s ease;
}
.fade {
    animation: fadeIn 0.4s ease-in;
}
@keyframes fadeIn {
    from { opacity: 0.6; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
div[data-testid="stButton"] button {
    transition: all 0.25s ease;
    border-radius: 10px;
}
div[data-testid="stButton"] button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

col1, col2 = st.columns([10, 1])

with col2:
    icon = "🌙" if st.session_state.dark_mode else "☀️"
    if st.button(icon):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

if st.session_state.dark_mode:
    bg_color = "#0E1117"
    card_color = "#1E1E1E"
    text_color = "#FFFFFF"
    header_bg = "#1E1E1E"
else:
    bg_color = "#AFC7E8"
    card_color = "#E3EFFC"
    text_color = "#1A1A1A"
    header_bg = "#E3EFFC"

st.markdown(f"""
<style>
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

p, h1, h2, h3, h4, h5, h6, span, label, div {{
    color: {text_color} !important;
}}

div[data-testid="stTextInput"] input {{
    background-color: {card_color};
    color: {text_color} !important;
}}

div[data-testid="stMarkdownContainer"] {{
    color: {text_color} !important;
}}

div[data-testid="stButton"] button {{
    background-color: #7FA7D9;
    color: {text_color} !important;
}}

div[data-testid="stDataFrame"] {{
    color: {text_color} !important;
}}

thead tr th {{
    background-color: {card_color} !important;
    color: {text_color} !important;
}}

tbody tr td {{
    background-color: {card_color} !important;
    color: {text_color} !important;
}}

section[data-testid="stSidebar"] * {{
    color: {text_color} !important;
}}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="
    background-color:{header_bg};
    padding:15px;
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
    border-radius: 16px;
    border-bottom:2px #8da9e0;
    text-align:center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
">
    <h2 style="margin:0; color:{text_color};">BlueQuery</h2>
    <p style="margin:0; color:{text_color};">Ask your data. Get SQL instantly.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="fade">', unsafe_allow_html=True)

examples = [
    "show all customers",
    "top 3 products by price",
    "customers with spending greater than 1000"
]

query = st.text_input(
    "Enter your query:",
    placeholder=f"e.g. {random.choice(examples)}"
)

if st.button("Generate SQL"):
    if query:
        st.toast("Processing query...")

        with st.spinner("Generating SQL..."):
            time.sleep(1)
            sql = generate_sql(query)

        result = run_query(sql)

        st.markdown(f"""
        <div style="
            background-color:{card_color};
            padding:20px;
            border:2px solid black;
            border-radius:12px;
        ">
        <h4>Generated SQL</h4>
        </div>
        """, unsafe_allow_html=True)

        st.code(sql, language="sql")

        st.markdown(f"""
        <div style="
            background-color:{card_color};
            padding:20px;
            border:2px solid black;
            border-radius:12px;
            margin-top:10px;
        ">
        <h4>Result</h4>
        </div>
        """, unsafe_allow_html=True)

        if isinstance(result, str):
            st.error("Invalid query generated")
        else:
            st.dataframe(result)

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("View Database Schema"):
    st.write("""
    customers(id, name, total_spent)  
    products(id, name, price)  
    orders(id, year)
    """)

st.markdown('</div>', unsafe_allow_html=True)
