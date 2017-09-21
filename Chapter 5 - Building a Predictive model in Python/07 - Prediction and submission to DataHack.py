#test_modified already loaded in the workspace

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History', 'Education', 'Gender']

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model.predict(x_test)
print(predicted)
#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)
print(predicted)
#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])
