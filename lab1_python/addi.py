string = input ("enter your string :")
arr = []
for i in range(len (string)):
    if string[i] == "i":
        arr.append((i))
print("the character 'i' is at ", arr )        