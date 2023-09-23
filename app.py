import streamlit as st
import numpy as np

import pickle
from PIL import Image
rfc = pickle.load(open('rfc.pkl', 'rb'))



st.title('Forest Cover Classification')
image = Image.open('img.png')

st.image(image, caption='myimage', use_column_width=True)
user_input = st.text_input('Input Features')


if user_input:
    user_input = user_input.split(',')
    features = np.array([user_input], dtype=np.float64)
    output = rfc.predict(features).reshape(1, -1)


   
   
    cover_type_dict = {
        1: {"name": "Spruce/Fir", "image": "img_01.png"},
        2: {"name": "Lodgepole Pine", "image": "img_02.png"},
        3: {"name": "Ponderosa Pine", "image": "img_03.png"},
        4: {"name": "Cottonwood/Willow", "image": "img_04.png"},
        5: {"name": "Aspen", "image": "img_05.png"},
        6: {"name": "Douglas-fir", "image": "img_06.png"},
        7: {"name": "Krummholz", "image": "img_07.png"}
    }

    
    predicted_cover_type = int(output[0])
    cover_type_info = cover_type_dict.get(predicted_cover_type)

    if cover_type_info is not None:
        cover_type_name = cover_type_info["name"]
        cover_type_image_path = cover_type_info["image"]

        
        col1, col2 = st.columns([2, 3])

        with col1:
            st.write("Predicted Cover Type:")
            st.write(f"<h1 style='font-size: 40px; font-weight: bold;'>{cover_type_name}</h1>", unsafe_allow_html=True)

        with col2:
            cover_type_image = Image.open(cover_type_image_path)
            st.image(cover_type_image, caption=cover_type_name, use_column_width=True)
    else:
        st.write("Unable to make a prediction")