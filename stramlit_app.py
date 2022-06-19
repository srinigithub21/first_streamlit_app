
import streamlit
streamlit.title('My Moms New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rcoket Smoothie')
streamlit.text('🥚 Hard boiled Free Range Egg')
streamlit.text('🥑🍞 Avacado Fest')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
Fruits_sel=streamlit.multiselect("Pick Some Fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show=my_fruit_list.loc[Fruits_sel]
streamlit.dataframe(Fruits_to_show)

streamlit.header('Fruitwise Fruit Advice')
fruit_choice=streamlit.text_input('What fruit information you would like to add ?','Kiwi')
streamlit.write('The user entered',fruit_choice)
import requests

frutycide_response=requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)

fruityvice_normalized=pandas.json_normalize(frutycide_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text('Hello from Snowflake:')
streamlit.text(my_data_row)
