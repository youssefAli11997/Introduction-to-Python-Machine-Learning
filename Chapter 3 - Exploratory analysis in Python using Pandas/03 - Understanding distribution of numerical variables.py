# Training and Testing dataset are loaded in train and test dataframe respectively
# Plot histogram for variable LoanAmount
train.LoanAmount.hist()

# Plot a box plot for variable LoanAmount by variable Gender of training data set
train.boxplot(column='LoanAmount', by = 'Gender')
