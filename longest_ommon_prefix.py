'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
The linke for this question in leetcode: https://leetcode.com/problems/longest-common-prefix/
'''



def is_valid_list(list_strings):
    new_list_strings = []
    if len(list_strings) >= 1 and len(list_strings) <= 200:
        for string in list_strings:
            if len(string) >= 0 and len(string) <= 200:
                new_list_strings.append(string.lower())

            else:
                return False
        list_strings = new_list_strings
        return True,list_strings
    return False

def longest_common_prefix(list_strings):
    list_strings = sorted(list_strings, key=len, reverse=0)
    for index in range(len(list_strings[0])):
        for element in list_strings:
            if list_strings[0][index] != element[index]:
                return indexww

input_strings = input()   # takes the whole line of n numbers
list_strings = list(map(str, input_strings.split(' ')))
isvalid_liststrings = is_valid_list(list_strings)
is_valid = isvalid_liststrings[0]
list_strings = isvalid_liststrings[1]

print(list_strings)
print(is_valid)