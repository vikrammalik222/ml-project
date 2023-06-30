import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_(movie_id):
    res=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a3ae35747979dc53b41f294a1fb3b046&language=en-US'.format(movie_id))
    data=res.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
    ind=movies[movies['title']==movie].index[0]
    distance=similars[ind]
    list_movies=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    L=[]
    Posters=[]
    for i in list_movies:
        movie_id=movies.iloc[i[0]].movie_id
        L.append(movies.iloc[i[0]].title)
        Posters.append(fetch_(movie_id))
    return L,Posters

movie_l=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_l)
similars=pickle.load(open('similars.pkl','rb'))

st.snow()

base="dark"


st.title('Film Recommendations')
st.markdown('this is a Movie recommender system which suggest movies based on your search')
sel_movie= st.selectbox(
    'Search movies',
    movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(sel_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


