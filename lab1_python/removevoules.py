string = input("enter your string :")
vowels = ['a', 'e', 'i', 'o', 'u']
result = ""
for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]
print("\nyour string after removing the voules",result )        