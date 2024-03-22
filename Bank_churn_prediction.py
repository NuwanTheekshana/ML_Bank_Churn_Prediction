import pickle

model = pickle.load(open('https://github.com/NuwanTheekshana/ML_Bank_Churn_Prediction/blob/main/BC_model.pkl', 'rb'))

CreditScore = int(input('Please enter CreditScore: '))
Geography = int(input('Please enter Geography (0-France, 1-Germany, 2-Spain): '))
Gender = int(input('Please enter Gender (0-Female, 1-Male): '))
Age = int(input('Please enter Age: '))
Tenure = int(input('Please enter Tenure: '))
Balance = float(input('Please enter Balance: '))
NumOfProducts = int(input('Please enter NumOfProducts: '))
HasCrCard = int(input('Please enter HasCrCard: '))
IsActiveMember = int(input('Please enter IsActiveMember: '))
EstimatedSalary = float(input('Please enter EstimatedSalary: '))

pred = model.predict([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])


if(pred == 0):
    print("Exited")
else:
    print("Not Exited")
    