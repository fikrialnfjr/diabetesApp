import streamlit as st
from prediction import performPrediction
from clustering import performClustering
from visualization import showVisualization
import pandas as pd

def loadData():
    df = pd.read_csv('diabetes.csv')
    return df

def showRawData():
    df = loadData()
    st.subheader('Raw Data')
    st.dataframe(df)

def main():
    st.title('Data Science Web App')
    st.sidebar.subheader('Menu')
    menu_options = ['Prediction', 'Clustering', 'Visualization']
    selected_menu = st.sidebar.selectbox('Select Option', menu_options)

    if selected_menu == 'Prediction':
        showRawData()
        performPrediction()
    elif selected_menu == 'Clustering':
        showRawData()
        performClustering()
    elif selected_menu == 'Visualization':
        showVisualization()

if __name__ == '__main__':
    main()
    st.set_option('deprecation.showPyplotGlobalUse', False)