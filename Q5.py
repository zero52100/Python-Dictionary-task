try:
    num = int(input("Enter the no of element in dictionary : "))
    user_dict= {}
    total=1
    for i in range(num):
        key = input(f"Enter key {i + 1}: ")
        value = int(input(f"value for {key}:"))
        user_dict[key] = value
    for value in user_dict.values():
        total *= value
    print(f"User entered dictionary: {user_dict}")
    print(f"The sum of all values in the dictionary is: {total}")
except ValueError:
    print("Invalid input !")