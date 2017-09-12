#Training and Testing data set are loaded in train and test dataframe respectively

# Look at the summary of numerical variables for train data set
df= train.describe()
print (df)
print("-------------------------")

# Print the unique values and their frequency of variable Property_Area
df1=train.Property_Area.value_counts()
print (df1)
