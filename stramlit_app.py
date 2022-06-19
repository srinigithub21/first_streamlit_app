
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
import requests
frutycide_response=requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlist.text(frutycide_response.json())


