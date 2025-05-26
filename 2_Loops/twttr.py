#Practice Set 2 Problem 3

#define list of vowels
vowel_list = ['a', 'e', 'i', 'o', 'u']

#take input, and turn into list
user_input = input("Input: ")
user_input_list = list(user_input)

#loop through list, and remove any vowels
offset = 0 #offset used to ensure indexes are correct even when parts of the lists are deleted

for i in range(len(user_input_list)):
    for vowel in vowel_list:
        if user_input_list[i-offset].lower() == vowel:
            user_input_list.pop(i-offset)
            offset += 1
            break

#print list as output
print("Output: ", end="")
for letter in user_input_list:
    print(letter, end="")