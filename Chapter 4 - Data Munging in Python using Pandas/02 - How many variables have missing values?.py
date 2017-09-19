# Check variables have missing values in test data set
number_missing_values_test_data = test.isnull().sum()

print(number_missing_values_test_data)
