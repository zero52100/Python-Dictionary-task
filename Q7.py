try:
    num = int(input("Enter the no of element in dictionary : "))
    user_dict= {}
    total=1
    for i in range(num):
        key = input(f"Enter key {i + 1}: ")
        value = int(input(f"value for {key}:"))
        user_dict[key] = value
    print("Original Dictionary:", user_dict)
    keys_to_delete = input("Enter keys to delete (comma-separated): ").split(',')
    for key in keys_to_delete:
        user_dict.pop(key, None)
    print("Dictionary after deleting keys:", user_dict)
except ValueError:
    print("Invalid input !")