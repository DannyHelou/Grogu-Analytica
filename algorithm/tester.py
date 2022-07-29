
x = 121
x = str(x)
placeHolder = list(x)
newArr = []
for i in range(len(x)):
    newArr.append(placeHolder.pop())
print(x)