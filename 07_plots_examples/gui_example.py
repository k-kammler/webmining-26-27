import streamlit as st
import matplotlib.pyplot as plt

st.title('Bar Plot mit Streamlit und Matplotlib')

zahl1 = st.number_input('Zahl 1', min_value=0, value=10)
zahl2 = st.number_input('Zahl 2', min_value=0, value=20)
zahl3 = st.number_input('Zahl 3', min_value=0, value=30)

fig, ax = plt.subplots()
ax.bar(['Zahl 1', 'Zahl 2', 'Zahl 3'], [zahl1, zahl2, zahl3])
#plt.yscale('log')

st.pyplot(fig)
