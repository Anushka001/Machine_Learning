import numpy as np
import pickle

# loading the saved model
load_model = pickle.load(open('G:/Projects/Deployment of ML model/trained_model.sav', 'rb'))

input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)

# changing input data to a numpy array
input_data_array = np.asarray(input_data)

# reshape the data as we are predicting label for only one instance
input_data_reshape = input_data_array.reshape(1,-1) 

prediction = load_model.predict(input_data_reshape)
print(prediction)

if (prediction[0] == 0):
    print('The patient is Non-Diabetic')
else:
    print('The patient is Diabetic')