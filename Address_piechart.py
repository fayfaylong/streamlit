import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('USA_Housing.csv')

labels = 'NE', 'CA', 'WI', 'AP', 'AE'
sizes = [4.09, 3.09, 5.13, 3.26, 4.23]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.set_title('Address_piechart')

st.pyplot(fig)
