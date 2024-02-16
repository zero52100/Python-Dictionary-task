num = int(input("Enter the no of element in dictionary : "))
user_dict= {}
keys = []
for i in range(num):
    key = input(f"Enter key {i + 1}: ")
    value = input(f"value for {key}:")
    user_dict[key] = value
keys_list=[]
for i in user_dict:
    keys_list.append(i)
print("User entered Dictionary:", user_dict)
print("Keys of the Dictionary:", keys_list)
