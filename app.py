# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 00:12:52 2022

@author: mike
"""

import streamlit as st
import pandas as pd
import os


def separate_into_cols(string):
  col_list = [col.strip() for col in string.split('*')]
  return col_list

def main_logic():
  
  file_path = st.file_uploader("Upload your file")

  if  file_path is not None:
      df = pd.read_csv(file_path)
      st.write("Column names")
      st.write(df.columns)
      x_cols = st.text_input("input the new column names from bottom to top, each separated by *: example 'Age*Place of Birth*Generation ")
      y_cols = st.text_input("input the new row names from right to left, each separated by *: example 'Age*Place of Birth*Generation ")

      submit = st.button('Done?')
      
      if submit == True:
          st.dataframe(pd.crosstab([df[i] for i in separate_into_cols(x_cols)], 
                             [df[i] for i in separate_into_cols(y_cols)]))


if __name__ == '__main__':
    main_logic()