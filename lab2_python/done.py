if __name__ == "__main__":
    list_num = []
    total = 0
    num_count = 0
    num_avarg = 0

    print("Enter numbers. Type 'done' when finished.")
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break

        if user_input.isdigit():
            user_input = int(user_input)
            list_num.append(user_input)
            total += user_input
            num_count += 1
            num_avarg = total / num_count
        else:
            print(f"Invalid input: '{user_input}'. Please enter a number.")

    if num_count > 0:
        print(f"Total: {total}, Count: {num_count}, Average: {num_avarg}")
    else:
        print("No numbers entered.")
