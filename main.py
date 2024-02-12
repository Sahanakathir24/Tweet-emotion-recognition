import streamlit as st
import text_emotion_app
import speech_emotion_app
import live_emotion_app
from PIL import Image


def main():

    # Create a sidebar menu to choose an option
    st.sidebar.header("Choose an option")
    option = st.sidebar.selectbox("", ["Home", "Text", "Speech", "Live Streaming","About model"])

    # Check the selected option and display the corresponding app
    if option == "Home":
        st.text("This project aims to analyze and classify emotions expressed in various forms of communication. We've divided this project \ninto three distinct categories:\n\n1.TEXT EMOTION RECOGNITION: Explore the emotional tone of written text. Our model will help you understand the underlying\n emotions in the text you provide.\n\n2.SPEECH EMOTION RECOGNITION: Analyze the emotions conveyed through spoken words. Upload an audio file, and our system \nwill identify and classify the emotions expressed in the speech.\n\n3.LIVE STREAM EMOTION RECOGNITION: Stay tuned for our emotion analysis capabilities, where we'll analyze emotions\n in live streams.\n\n   Choose an option from the sidebar to get started and experience the power of emotion classification in different \ncommunication mediums.\n\n   Let's uncover the emotions behind the words, voices and expressions!")
    elif option == "Text":
        text_emotion_app.text_emotion_recognition_app()
    elif option == "Speech":
        speech_emotion_app.speech_emotion_recognition_app()
    elif option == "Live Streaming":
        st.title("Live Emotion Recognition")
        if st.button("\n\nStart capturing"):
            live_emotion_app.live_emotion_recognition_app()
        image = Image.open(r"C:\Users\91944\Downloads\tweets\images\live.jpg")
        custom_width = 500  
        st.image(image, width=custom_width)
    elif option == "About model":
        st.title("PERFORMANCE METRICS")
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                if st.button("\n\nBag of Words Model"):
                   st.markdown('<span style="font-size: 24px;">BAG OF WORDS MODEL</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">SHAPE OF DATA:20000</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">DATA FOR TRAINING:16000</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">DATA FOR TESTING:2000</span>', unsafe_allow_html=True)
        #if st.button("\n\nBag of Words Model"):
                   src=Image.open(r"C:\Users\91944\Downloads\tweets\images\bagsofwordspiechart.png")
                   custom_width =300  
                   st.image(src, width=custom_width)
                   srcc=Image.open(r"C:\Users\91944\Downloads\tweets\images\histogram.png")
                   custom_width =300  
                   st.image(srcc, width=custom_width)
                   srccc=Image.open(r"C:\Users\91944\Downloads\tweets\images\confusionmatrix.png")
                   custom_width =300  
                   st.image(srccc, width=custom_width)
            with col2:
                if st.button("\n\nBert Model"):
                   st.markdown('<span style="font-size: 24px;">BERT MODEL</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">SHAPE OF DATA:11327</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">DATA FOR TRAINING:7934</span>', unsafe_allow_html=True)
                   st.write('<span style="font-size: 18px;">DATA FOR TESTING:3393</span>', unsafe_allow_html=True)
                   srce=Image.open(r"C:\Users\91944\Downloads\tweets\images\bert model pie.png")
                   custom_width =300  
                   st.image(srce, width=custom_width)
                   srcce=Image.open(r"C:\Users\91944\Downloads\tweets\images\histobert.png")
                   custom_width =300  
                   st.image(srcce, width=custom_width)
                   srcee=Image.open(r"C:\Users\91944\Downloads\tweets\images\confubert.png")
                   custom_width =300  
                   st.image(srcee, width=custom_width)
        
                
           


if __name__ == '__main__':
    main()

