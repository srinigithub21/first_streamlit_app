
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
streamlit.multiselect("Pick Some Fruit:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
