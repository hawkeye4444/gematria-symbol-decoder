import streamlit as st
from gematria import calculate_all_ciphers, match_symbols
import json

st.set_page_config(page_title="Gematria & Symbol Analyzer", layout="wide")

st.title("🔢 Gematria & Symbol Match Analyzer")

phrase = st.text_input("Enter a phrase, name, or place to decode:")

if phrase:
    gematria_values = calculate_all_ciphers(phrase)
    st.subheader("Gematria Values")
    st.json(gematria_values)

    with open("symbol_db.json", "r") as f:
        symbol_db = json.load(f)

    matches = match_symbols(gematria_values, symbol_db)
    st.subheader("🔍 Symbolic Matches")
    st.write(matches)
else:
    st.info("Enter a phrase above to see gematria values and symbolic matches.")