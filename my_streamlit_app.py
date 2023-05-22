import streamlit as st
import pandas as pz
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("L'APPLI DU SIÈCLE")
data = pz.read_csv(r'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
st.write("Aperçu des données :")
st.write(data.head(50))
correlation = data.corr()
st.write("Matrice de corrélation :")
st.write(correlation)
st.write("Heatmap de corrélation :")
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot()
st.write("Distribution des variables numériques :")
numerical_columns = data.select_dtypes(include=[float, int]).columns
for column in numerical_columns:
    st.write(f"Variable : {column}")
    sns.histplot(data=data, x=column, kde=True)
    st.pyplot()
selected_continent = st.sidebar.radio("Choisissez un continent", ('US.', 'Europe.', 'Japan.'))
filtered_data = data[data['continent'] == selected_continent]
if filtered_data.empty:
    st.write("Aucune donnée ne correspond au filtre.")
else:
    st.write("Données filtrées par continent :")
    st.write(filtered_data)