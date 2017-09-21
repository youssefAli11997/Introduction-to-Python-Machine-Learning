#train_modified and test_modified already loaded in the workspace
#Import module for Decision tree
import sklearn.tree

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History', 'Education', 'Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = sklearn.tree.DecisionTreeClassifier()
model.fit(x_train, y_train)

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model.predict(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])
