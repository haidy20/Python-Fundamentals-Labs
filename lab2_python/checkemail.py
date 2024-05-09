import re
def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

if __name__ == "__main__":
    name = input("Please enter your name: ").strip()
    if name:  
        email = input("Please enter your email: ").strip()
        if check_email(email):
            print(f"Name: {name}, Email: {email}")
        else:
            print("Invalid email format.")
    else:
        print("Name cannot be empty.")
