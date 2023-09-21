import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('USA_Housing.csv')

labels = ['NE', 'CA', 'WI', 'AP', 'AE']
sizes = [4.09, 3.09, 5.13, 3.26, 4.23]

fig = px.pie(data_frame=pd.DataFrame({'labels': labels, 'sizes': sizes}), 
             names='labels', 
             values='sizes', 
             title='Address_piechart')

st.plotly_chart(fig)