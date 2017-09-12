# Create a list of first five numbers
ls=[]
for x in range(5):
    ls.append(x)

sum=0
# Store sum all the even numbers of the list ls in sum

for x in ls:
    if x%2 == 0:
        sum += x

print (sum)
