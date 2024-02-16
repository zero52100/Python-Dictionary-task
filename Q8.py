def count(input_string):
    count = {}
    for char in input_string:
        if char.isalpha():
            count[char] = count.get(char, 0)+1
    return count
user_input = input("Enter a string: ")
result= count(user_input)
print("Letter count in the string:", result)
if all(value == 1 for value in result.values()):
    print("All letters are unique in the string.")
else:
    print("Some letters are not unique in the string.")
