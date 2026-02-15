import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

print("Initializing Application")

# dir = 'E:\\Programs\\Images\\PetImages'

# categories = ['Cat', 'Dog']

# data = []

# for category in categories:
#     path = os.path.join(dir, category)
#     label = categories.index(category)

#     for img in os.listdir(path):
#         imgpath = os.path.join(path, img)
#         pet_img = cv2.imread(imgpath, 0)  # Load image in grayscale
#         try:
#             pet_img = cv2.resize(pet_img, (50, 50))  # Resize to 50x50
#             image = np.array(pet_img).flatten()  # Flatten the image
#             data.append([image, label])  # Append to the data list
#         except Exception as e:
#             pass  # Ignore images that can't be processed

# # Save the data to a pickle file
# with open('data1.pickle', 'wb') as pick_in:
#     pickle.dump(data, pick_in)

def detect_pet():
    
    with open('data1.pickle', 'rb') as pick_in:
        data = pickle.load(pick_in)

    random.shuffle(data)  

   
    features = []
    labels = []

    for feature, label in data:
        features.append(feature)
        labels.append(label)

  
    xtrain, xtest, ytrain, ytest = train_test_split(features, labels, test_size=0.02)

   
    with open('model.sav', 'rb') as pick:
        model = pickle.load(pick)

 
    prediction = model.predict(xtest)
    accuracy = model.score(xtest, ytest)

    categories = ['Cat', 'Dog']
    prediction_label = categories[prediction[0]]

    
    prediction_image = np.array(xtest[0]).reshape(50, 50) * 255
    prediction_image = prediction_image.astype(np.uint8)

    print('Accuracy:', accuracy)
    print('Prediction is:', prediction_label)

   
    return prediction_image, accuracy, prediction_label


