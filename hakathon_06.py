import streamlit as st

def elec_para(v,r,t):
    i=v/r
    p=(i**2)*r
    h=(i**2)*r*t
    return i,p,h

st.title("2305a21l06-ps1")

st.write("this application is useful for calculating current through a load,power drawn by a load,and heat energy generated.")
col1, col2 = st.columns(2)
with col1:
        v = st.number_input("input voltage:v")
        r = st.number_input("load resistance:r")
        t = st.number_input("time in hours:t")
        cal = st.button('Compute')
with col2:
    if cal:
            i,p,h = elec_para(v,r,t)
            st.write(f"load current= = {i:.2f} a")
            st.write(f"load power = {p:.2f} w")
            st.write(f"heat energy = {h:.2f} kwhs")
