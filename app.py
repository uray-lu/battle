import streamlit as st
from shuffle import battle


st.write("#輸入名字")
people_num = st.selectbox('人數', [7,10,13])

if people_num == 13:
    col1, col2, col3, col4 = st.columns(4)

    a = col1.text_input('Name 1:')
    b = col2.text_input('Name 2:')
    c = col3.text_input('Name 3:')
    d = col4.text_input('Name 4:')
    e = col1.text_input('Name 5:')
    f = col2.text_input('Name 6:')
    g = col3.text_input('Name 7:')
    h = col4.text_input('Name 8:')
    i = col1.text_input('Name 9:')
    j = col2.text_input('Name 10:')
    k = col3.text_input('Name 11:')
    l = col4.text_input('Name 12:')
    m = col1.text_input('Name 13:')

    list = [a,b,c,d,e,f,g,h,i,j,k,l,m]
    list = [ x for x in list if x != ""]

elif people_num == 10:
    col1, col2, col3, col4 = st.columns(4)

    a = col1.text_input('Name 1:')
    b = col2.text_input('Name 2:')
    c = col3.text_input('Name 3:')
    d = col4.text_input('Name 4:')
    e = col1.text_input('Name 5:')
    f = col2.text_input('Name 6:')
    g = col3.text_input('Name 7:')
    h = col4.text_input('Name 8:')
    i = col1.text_input('Name 9:')
    j = col2.text_input('Name 10:')


    list = [a,b,c,d,e,f,g,h,i,j]
    list = [ x for x in list if x != ""]

elif people_num == 7:
    col1, col2, col3, col4 = st.columns(4)

    a = col1.text_input('Name 1:')
    b = col2.text_input('Name 2:')
    c = col3.text_input('Name 3:')
    d = col4.text_input('Name 4:')
    e = col1.text_input('Name 5:')
    f = col2.text_input('Name 6:')
    g = col3.text_input('Name 7:')



    list = [a,b,c,d,e,f,g]
    list = [ x for x in list if x != ""]

if st.button('輸入完點我一下，感恩!'):
    df = battle(list)
    st.dataframe(data = df)

