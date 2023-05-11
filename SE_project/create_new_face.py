import face_recognition
from database import add_record
import numpy as np
import os

dir_name = os.path.dirname(__file__)

def new_entry(img_name, img_id, gender):
    img_file = face_recognition.load_image_file(os.path.join(dir_name, 'photos\{}.jpeg').format(str(img_id)))
    img_encoding = face_recognition.face_encodings(img_file)
    print('Face encoding created.')
    #img_encoding_arr = np.array(img_encoding).reshape(1, 128)
    img_encoding_str = ','.join(map(str, img_encoding))
    # Adding the new record to database.
    add_record(img_name, gender, img_id, img_encoding_str)