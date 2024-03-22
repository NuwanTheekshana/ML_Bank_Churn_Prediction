import streamlit as st
import pickle
import requests

url = 'BC_model.pkl'
response = requests.get(url)
with open('BC_model.pkl', 'wb') as f:
    f.write(response.content)

model = pickle.load(open('BC_model.pkl', 'rb'))


def predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    pred = model.predict([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])
    return pred

# Streamlit app
st.title('Bank Churn Prediction')


CreditScore = st.number_input('Credit Score:')
Geography = st.selectbox('Geography', ['France', 'Germany', 'Spain'])
Gender = st.selectbox('Gender', ['Female', 'Male'])
Age = st.number_input('Age:')
Tenure = st.number_input('Tenure:')
Balance = st.number_input('Balance:')
NumOfProducts = st.number_input('Number of Products:', min_value=1, max_value=4, value=1)
HasCrCard = st.selectbox('Has Credit Card?', ['No', 'Yes'])
IsActiveMember = st.selectbox('Is Active Member?', ['No', 'Yes'])
EstimatedSalary = st.number_input('Estimated Salary:')


if st.button('Predict'):
    geography_mapping = {'France': 0, 'Germany': 1, 'Spain': 2}
    gender_mapping = {'Female': 0, 'Male': 1}
    has_cr_card_mapping = {'No': 0, 'Yes': 1}
    is_active_member_mapping = {'No': 0, 'Yes': 1}
    
    Geography = geography_mapping[Geography]
    Gender = gender_mapping[Gender]
    HasCrCard = has_cr_card_mapping[HasCrCard]
    IsActiveMember = is_active_member_mapping[IsActiveMember]
    
    pred = predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
    
    if pred == 0:
        st.write("Exited")
    else:
        st.write("Not Exited")
