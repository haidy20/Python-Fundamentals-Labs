def checknum(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    
    else:
        return "not a fizz or buzz "
    
if __name__ == "__main__":
    num = input("enter a number ")
    if (num.isdigit()):
        num = int(num)
        print(f" word : {checknum(num)}");