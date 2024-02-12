import streamlit as st
import pandas as pd
import numpy as np
import pickle #to serialize and deserialize data
import tensorflow as tf #framework to build models 
from preprocess import *


def text_emotion_recognition_app():
    st.title("Text Emotion Recognition")

   

    st.sidebar.header('User Input')




    def user_input():
         text = st.sidebar.text_input('Enter your sentence: ')

         return text
    input = user_input()

    st.write(input)
    encoder = pickle.load(open(r'C:\Users\91944\Downloads\tweets\encoder.pkl', 'rb'))
    cv = pickle.load(open(r'C:\Users\91944\Downloads\tweets\CountVectorizer.pkl', 'rb'))


    model=tf.keras.models.load_model(r'C:\Users\91944\Downloads\tweets\my_model.h5')
    input=preprocess(input)

    array = cv.transform([input]).toarray()

    pred = model.predict(array)
    a=np.argmax(pred, axis=1)
    prediction = encoder.inverse_transform(a)[0]


    st.subheader('Prediction')
    if input == '':
        st.write('The emotion of this text is...')
    else:
        st.write(prediction)
if __name__ == "__main__":
    text_emotion_recognition_app()

