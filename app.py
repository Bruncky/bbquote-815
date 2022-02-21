import streamlit as st

from bbquote.lib import get_quote

response = get_quote()  # assuming the function returns an author and a quote

st.write(f"{response['quote']} ---> {response['author']}")
