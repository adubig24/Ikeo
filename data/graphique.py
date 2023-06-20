import matplotlib.pyplot as plt
import streamlit as st
import data.data as dd
import data.queries as dq

def graph1():
    df=dd.get_data(dq.query9)
    st.title("Commandes par produit :")
    fig=plt.figure(figsize=[20,8])
    plt.barh(df['nom'], df['Quantité commandée'])
    plt.ylabel('Produit')
    plt.xlabel('Quantité commandée')
    plt.title('Histogramme des commandes')
    plt.xticks(rotation=45)
    st.pyplot(fig)

def graph2():
    df=dd.get_data(dq.queryst4)
    st.title("Commandes par client :")
    fig=plt.figure(figsize=[20,8])
    plt.barh(df['raison_sociale']+" "+df['ville_c'], df['Quantité commandée'])
    plt.ylabel('Client')
    plt.xlabel('Quantité commandée')
    plt.title('Histogramme des commandes')
    plt.xticks(rotation=45)
    st.pyplot(fig)