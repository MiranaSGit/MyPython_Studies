import streamlit as st
% % writefile app.py

st.title("Şiir Formatını Kıta'ya Dönüştürücü Uygulama")

path = None
path = st.file_uploader("Upload your txt file: ", type=["txt"])

if path:
    with open(path, "r", encoding="utf-8") as ff:
        lines = ff.readlines()

    counter = 0
    with open("Istiklal_Marsi.txt", "w", encoding="utf-8") as f:
        for i in lines:
            counter += 1
            if counter % 4 == 0:
                f.write(i + "\n")
            else:
                f.write(i)
