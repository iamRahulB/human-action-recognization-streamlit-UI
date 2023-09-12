import streamlit as st
from PIL import Image

from youtube_downloader import Download
from collections import deque
from prediction import Predict

downld=Download()

st.title("Human Action Recognization [DL]")
with st.expander("Details", expanded=False):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random''')
    

url= st.text_input("Insert Youtube Url as instructed above ")

if st.button("submit"):
    title, output_dir=downld.youtube_d(url)
    col1, col2 = st.columns([2, 2])

    with col1:
        st.success('Video Downloaded!', icon="✅")
        print(output_dir)
        st.video(f"{output_dir}/{title}.mp4")

        
        


    with col2:
        st.info("Wait a while Model is Performing its Task")
        pred =Predict()
        frames_needed=25
        input_path=f"{output_dir}/{title}.mp4"
        output_path=f"test_videos/{title}_output.mp4"
        pred.prediction(input_path,output_path ,frames_needed)
        

        st.video(output_path)
        st.balloons()


