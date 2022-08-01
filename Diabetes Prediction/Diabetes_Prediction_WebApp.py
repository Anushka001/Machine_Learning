import numpy as np
import pickle
import streamlit as st

# loading the saved model
load_model = pickle.load(open('G:/Projects/Deployment of ML model/trained_model.sav', 'rb'))

# creating a function for prediction
def diabetes_pred(input_data):

    # changing input data to a numpy array
    input_data_array = np.asarray(input_data)

    # reshape the data as we are predicting label for only one instance
    input_data_reshape = input_data_array.reshape(1,-1) 

    prediction = load_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return 'The patient is Non-Diabetic'
    else:
        return 'The patient is Diabetic'


def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')

    # getting input data from user
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,
    pregnancies = st.text_input('Number of Pregnancies')
    glucose = st.text_input('Blood Glucose Level')
    blood_pressure = st.text_input('Blood Pressure value')
    skin_thickness = st.text_input('Thickness of Skin')
    insulin = st.text_input('Insulin level')
    bmi = st.text_input('Body Mass Index value')
    diabetespedegreefunction = st.text_input('Diabetes Pedigree Function Value')
    age = st.text_input('Age of the person')

    # prediction
    diagnosis = ''

    # creating a button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_pred([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetespedegreefunction, age])

    st.success(diagnosis)



if __name__ == '__main__':
    main()
