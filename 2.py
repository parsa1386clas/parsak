lines = "fars.text"
count = 0
with open(lines, 'r') as f:
    for line in f:
        count +=1
print("number of your line is:" , count)
