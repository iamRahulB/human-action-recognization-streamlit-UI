import cv2
import numpy as np
import math
from collections import deque
import tensorflow as tf
from tensorflow import keras
from collections import OrderedDict


from keras.models import load_model

LCRN_model = load_model('LRCN_model.h5')

class Predict:

    def __init__(self) :
        pass

       
    def prediction(self,input_path, output_path,frames_needed):
        video_reader=cv2.VideoCapture(input_path)

        original_video_width=int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_video_hight=int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

        video_writer=cv2.VideoWriter(output_path,cv2.VideoWriter_fourcc('V', 'P', '9', '0'),video_reader.get(cv2.CAP_PROP_FPS),(original_video_width,original_video_hight))
        frames_deque=deque(maxlen=frames_needed)

        predicted_class_name=""
        IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64
        classes_to_be_used=["HorseRace","BenchPress","PullUps","PushUps","HorseRiding","HighJump","Swing"]

        while video_reader.isOpened():
            ok, frame = video_reader.read()

            if not ok:
                break

            resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
            normalized_frame = resized_frame / 255

            frames_deque.append(normalized_frame)

            if len(frames_deque) == frames_needed:
                input_sequence = np.expand_dims(frames_deque, axis=0)  # Add batch dimension
                predicted_labels_probabilities = LCRN_model.predict(input_sequence)[0]  # Get rid of outer batch dimension

                predicted_label = np.argmax(predicted_labels_probabilities)
                predicted_class_name = classes_to_be_used[predicted_label]

                cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                video_writer.write(frame)

        video_reader.release()
        video_writer.release()