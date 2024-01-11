import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.title("This is Home")


# -------------password authenticator
# name = ["Tom Wang","Yuri Wang"]
# usernames = ["twang", "Ywang"]
# passwords = ["def123","abc123"]

# hashed_passwords = stauth.Hasher(passwords).generate()

# file_path = Path(__file__).parent / "hasded_pw.pkl"
# with file_path.open('wb') as file:
#     pickle.dump(hashed_passwords,file)