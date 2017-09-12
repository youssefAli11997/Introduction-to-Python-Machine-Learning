# Training and Testing dataset are loaded in train and test dataframe respectively

# Approved Loan in absolute numbers
loan_approval = train['Loan_Status'].value_counts()['Y']

# Two-way comparison: Credit History and Loan Status
twowaytable = pd.crosstab(train ["Credit_History"], train ["Loan_Status"], margins=True)
