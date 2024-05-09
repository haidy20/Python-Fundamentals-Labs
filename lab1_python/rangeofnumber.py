number = 4
result = []
for i in range(1, number + 1):
    temp = []
    for j in range(1, i + 1):
        temp.append(j * i)
    result.append(temp)

print(result)