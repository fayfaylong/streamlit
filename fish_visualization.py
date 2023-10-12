import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Fish.csv')

# Create a dropdown menu
species = st.selectbox('Select a species:', data['Species'].unique())

# Filter the data based on the selected species
species_data = data[data['Species'] == species]

# Create a boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data=species_data[['Length1', 'Length2', 'Length3', 'Height', 'Width']])
plt.title(f'1.Boxplot of Length, Height, and Width for {species}')
st.pyplot(plt)

#############################################################


# Create a slider
max_weight = st.slider('Select the maximum weight:', min_value=0, max_value=int(data['Weight'].max()), value=int(data['Weight'].max()))

# Filter the data based on the selected maximum weight
filtered_data = data[data['Weight'] <= max_weight]
counts = filtered_data['Species'].value_counts()

# Define colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'pink']  # Add more colors if needed

# Create a histogram
plt.figure(figsize=(10, 6))
plt.bar(counts.index, counts.values, color=colors[:len(counts)])
plt.title(f'2.Count of Each Species (Weight <= {max_weight})')
plt.xlabel('Species')
plt.ylabel('Count')
plt.xticks(rotation=45)
st.pyplot(plt)

###############################################################

# Create radio buttons
length_type = st.radio('Select length type:', ('Length1', 'Length2', 'Length3'))

# Calculate the average length of each species
average_lengths = data.groupby('Species')[length_type].mean()

# Define colors
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'pink']  # Add more colors if needed

# Create a histogram
plt.figure(figsize=(10, 6))
plt.bar(average_lengths.index, average_lengths.values, color=colors[:len(average_lengths)])
plt.title(f'3.Average {length_type} for Each Species')
plt.xlabel('Species')
plt.ylabel(f'Average {length_type}')
plt.xticks(rotation=45)
st.pyplot(plt)

################################################################

# Calculate the mean length of each species for Length1, Length2, and Length3
mean_lengths = data.groupby('Species')[['Length1', 'Length2', 'Length3']].mean()

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(mean_lengths.index, mean_lengths['Length1'], marker='o', label='Length1', color='blue')
plt.plot(mean_lengths.index, mean_lengths['Length2'], marker='o', label='Length2', color='green')
plt.plot(mean_lengths.index, mean_lengths['Length3'], marker='o', label='Length3', color='red')
plt.title('4.Mean Lengths of Length1, Length2, and Length3 for Each Species')
plt.xlabel('Species')
plt.ylabel('Mean Length')
plt.legend()
plt.xticks(rotation=45)
st.pyplot(plt)

#################################################################

# Calculate the mean of Length1, Length2, and Length3
data['MeanLength'] = data[['Length1', 'Length2', 'Length3']].mean(axis=1)

# Calculate the mean of MeanLength, Height, Width, and Weight per species
mean_values = data.groupby('Species')[['MeanLength', 'Height', 'Width', 'Weight']].mean().sort_values(by='Weight', ascending=False)

# Visualize the histograms and line chart
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(mean_values.index, mean_values['MeanLength'], alpha=0.6, label='Mean Length')
ax1.bar(mean_values.index, mean_values['Height'], alpha=0.6, label='Mean Height', bottom=mean_values['MeanLength'])
ax1.bar(mean_values.index, mean_values['Width'], alpha=0.6, label='Mean Width', bottom=mean_values['MeanLength'] + mean_values['Height'])
ax1.set_ylabel('Size')
ax1.set_xlabel('Species')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(mean_values.index, mean_values['Weight'], label='Mean Weight', color='r', marker='o')
ax2.set_ylabel('Weight')

plt.title('5.Mean Length, Height, Width, and Weight per Species')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(loc='upper right')
st.pyplot(fig)
