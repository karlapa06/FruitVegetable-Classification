from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('mi_modelo.keras')

class_labels = ['Apple_Healthy', 'Apple_Rotten', 'Banana_Healthy', 'Banana_Rotten', 
    'Bellpepper_Healthy', 'Bellpepper_Rotten', 'Carrot_Healthy', 'Carrot_Rotten',
    'Cucumber_Healthy', 'Cucumber_Rotten','Grape_Healthy', 'Grape_Rotten',
    'Guava_Healthy', 'Guava_Rotten', 'Jujube_Healthy', 'Jujube_Rotten',
    'Mango_Healthy', 'Mango_Rotten', 'Orange_Healthy', 'Orange_Rotten', 
    'Pomegranate_Healthy', 'Pomegranate_Rotten','Potato_Healthy', 'Potato_Rotten',
    'Strawberry_Healthy', 'Strawberry_Rotten', 'Tomato_Healthy', 'Tomato_Rotten'] 


def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    class_idx = np.argmax(prediction)
    label = class_labels[class_idx]
    return label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join('static/uploads', file.filename)
        file.save(filepath)

        label = predict(filepath)
        return render_template('index.html', label=label, filename=file.filename)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)
