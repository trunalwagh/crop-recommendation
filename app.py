# from flask import Flask, render_template, request ,redirect, url_for
# import pickle
# import numpy as np
# import os
#
#
# crop_recommendation_model_path = 'models/RandomForest.pkl'
# crop_recommendation_model = pickle.load(open('E:/BTech/projects/Crop-recommendation-system-main/models/RandomForest.pkl', 'rb'))
#
#
# app = Flask(__name__)
#
# picFolder = os.path.join('static','images')
# app.config['UPLOAD_FOLDER'] = picFolder
#
# @ app.route('/')
# def home():
#     title = 'Home Page'
#     pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'pexels-pixabay-207247 (1).jpg')
#     return render_template('index.html', user_image=pic1 ,title=title)
#
# @ app.route('/iot')
# def iot():
#     title = 'IOT Page'
#     return render_template('iot.html', title=title)
#
# @ app.route('/about')
# def about():
#     title = 'About Page'
#     return render_template('about.html', title=title)
#
#
# # here the form is present.
# @ app.route('/success',methods=['POST','GET'])
# def crop_recommend():
#     title = 'Crop Recommendation'
#     if request.method == 'POST':
#         N = int(request.form['nitrogen'])
#         P = int(request.form['phosphorous'])
#         K = int(request.form['potasium'])
#         ph = float(request.form['ph'])
#         T = float(request.form['temprature'])
#         H = float(request.form['moisture'])
#         #rainfall = float(request.form['rainfall'])
#
#         T = ((1007-T)/(1007-107))*100
#
#         data = np.array([[N, P, K, T, H, ph, np.random.randint(80,250)]])
#         my_prediction = crop_recommendation_model.predict(data)
#         final_prediction = my_prediction[0]
#
#         return render_template('crop-result.html', prediction=final_prediction)
#
#     # if request is not post then this template will be sent.
#     return render_template('crop.html', title=title)
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os

# Get the absolute path of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define relative path for the model
crop_recommendation_model_path = os.path.join(BASE_DIR, 'models', 'RandomForest.pkl')
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))

app = Flask(__name__)

picFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picFolder


@app.route('/')
def home():
    title = 'Home Page'
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'pexels-pixabay-207247 (1).jpg')
    return render_template('index.html', user_image=pic1, title=title)


@app.route('/iot')
def iot():
    title = 'IOT Page'
    return render_template('iot.html', title=title)


@app.route('/about')
def about():
    title = 'About Page'
    return render_template('about.html', title=title)


# Crop recommendation route
@app.route('/success', methods=['POST', 'GET'])
def crop_recommend():
    title = 'Crop Recommendation'
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potasium'])
        ph = float(request.form['ph'])
        T = float(request.form['temprature'])
        H = float(request.form['moisture'])

        # Normalize temperature
        T = ((1007 - T) / (1007 - 107)) * 100

        data = np.array([[N, P, K, T, H, ph, np.random.randint(80, 250)]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('crop-result.html', prediction=final_prediction)

    return render_template('crop.html', title=title)


# if __name__ == '__main__':
#     app.run(debug=True)
