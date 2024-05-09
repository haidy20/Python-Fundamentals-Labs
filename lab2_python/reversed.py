def rev_str(word):
    return word[::-1]

if __name__ == "__main__":
    word = input("enter a word ")
    if (word.isalpha()):
        print(f"reversed word : {rev_str(word)}")