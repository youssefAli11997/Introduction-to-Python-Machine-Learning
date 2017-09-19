# Impute missing value of Gender (Male is more frequent category)
train['Gender'].fillna('Male',inplace=True)


# Impute missing value of Credit_History ( 1 is more frequent category)
train['Credit_History'].fillna(1,inplace=True)
