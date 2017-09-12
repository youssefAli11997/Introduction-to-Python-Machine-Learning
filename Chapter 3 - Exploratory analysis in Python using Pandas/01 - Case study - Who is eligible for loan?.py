# import library pandas
import pandas as pd

# Import training data as train
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing data as test
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

# Print top 5 observation of train dataset
print (train.head(5) )

# Store total number of observation in training dataset
train_length = len (train)

# Store total number of columns in testing data set
test_col = len ( test.columns)

print(len(test), test_col)
print(test.shape)
