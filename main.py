import data.data as dd
import data.queries as dq
import data.graphique as dg
import streamlit as st
import streamlit.web.bootstrap as stb
import os

def main():
    df=dd.get_data(dq.queryst1)
    option = st.selectbox('Choisissez votre usine', df['usine'].unique())
    st.dataframe(df[df['usine'] == option].reset_index(drop=True).drop('usine', axis=1))

    dg.graph1()
    dg.graph2()

if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        streamlit_script_path = os.path.join(os.getcwd(), "main.py")
        stb.run(streamlit_script_path,'',[],flag_options=[])
        main()