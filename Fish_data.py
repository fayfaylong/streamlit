import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv('Fish.csv')

# Count the occurrences of each species in the dataset
species_counts = data['Species'].value_counts()

# Get the species names (labels) and their counts (sizes)
labels = species_counts.index
sizes = species_counts.values

# Create a DataFrame for the table
df = pd.DataFrame({'Species': labels, 'Count': sizes})

# Create the pie chart
fig = px.pie(data_frame=pd.DataFrame({'labels': labels, 'sizes': sizes}), 
             names='labels', 
             values='sizes', 
             title='Pie Chart of Species')

# Display the title, pie chart, and the table in the Streamlit app
st.header('Pie Chart of Species')
st.plotly_chart(fig)

st.header('Table of Species Counts')
st.table(df)
