def generateArr(start_arr, len_arr):
    arr = list(range(start_arr, start_arr + len_arr))
    print(arr)
    
if __name__ == "__main__":
    start_arr = input("Please enter array start: ")
    len_arr = input("Please enter array length: ")
    if start_arr.isdigit() and len_arr.isdigit():
        start_arr = int(start_arr)
        len_arr = int(len_arr)
        generateArr(start_arr, len_arr)
