try:
    num = int(input("Enter the no of element in dictionary : "))
    user_dict= {}
    total=1
    for i in range(num):
        key = input(f"Enter key {i + 1}: ")
        value = int(input(f"value for {key}:"))
        user_dict[key] = value
    max_value = float('-inf')
    min_value = float('inf')
    for value in user_dict.values():
        if value > max_value:
            max_value=value
        if value < min_value:
            min_value=value
    print(f"User entered dictionary: {user_dict}")
    print(f"The Maximum value:{max_value}  and The Minimum value:{min_value}")
except ValueError:
    print("Invalid input !")