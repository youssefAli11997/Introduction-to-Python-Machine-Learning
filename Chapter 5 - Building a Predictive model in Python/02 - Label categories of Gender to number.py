#import module for label encoding
from sklearn.preprocessing import LabelEncoder

#train and test dataset is already loaded in the enviornment
# Perform label encoding for variable 'Married'
number = LabelEncoder()
train['Married_new'] = number.fit_transform(train['Married'].astype(str))
