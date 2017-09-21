#train_modified and test_modified already loaded in the workspace
#Import module for Logistic regression
import sklearn.linear_model

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History', 'Education', 'Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = sklearn.linear_model.LogisticRegression()
model.fit(x_train, y_train)
