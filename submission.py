
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('DataFinal.csv', encoding='ascii')
    return data

data = load_data()

st.title('Bike Sharing Demand Analysis')
st.header('Entire Data')
st.write(data.head(15))


st.sidebar.header('Welcome')
season = st.sidebar.selectbox('Select Season', data['season'].unique())
filtered_data = data[data['season'] == season]

st.header('Filtered Data')
st.write(filtered_data)

sns.set_style("whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(x="weekday", y="cnt", data=data, ci=None)
plt.title("Bike Sharing Graphic based on Day")
plt.xlabel("Day")
plt.ylabel("Total Count")
st.pyplot(plt)

plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth", y="cnt", data=data, ci=None)
plt.title("Bike Sharing Graphic based on Month")
plt.xlabel("Month")
plt.ylabel("Total Count")
st.pyplot(plt)

plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth", y="cnt", data=filtered_data, ci=None)
plt.title("Filtered Month Graphic by Season")
plt.xlabel("Month")
plt.ylabel("Total Count")
st.pyplot(plt)


sns.set_style("whitegrid")
d = sns.FacetGrid(data, col="yr", height=8, aspect=1.5)
d.map(sns.barplot, "season", "cnt")
d.set_axis_labels("Season", "Total Count", fontsize=25) 
d.set_titles(fontsize=25)  

st.pyplot(plt)


