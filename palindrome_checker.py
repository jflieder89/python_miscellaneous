text = input('Enter some text to see if it is a palindrome: ').lower() #use lower to standardize all upper and lower case so differences in case will be ignored
#text = 'A man a plan a canal Panama'.lower()
text_stripped = '' #a string in which the text input minus the whitespace characters will be entered
for char in text:
    if char.isspace():
        pass #do nothing with whitespace characters
    else:
        text_stripped +=char #add non-whitespace characters to the text_stripped string

text_lst = [] #create empty list that will used to store individual characters of text
for char in text_stripped:
    text_lst.append(char) #add characters to the text_lst

reversed_lst = [] #empty lst of reversed text to compare with text
for element in text_lst:
    reversed_lst.insert(0, element) #so they are reversed compared to each other. Insert method can only be used on lists (not strings!)

reversed_str = '' #empty string of reversed text from reversed_lst elements
for element in reversed_lst:
    reversed_str = reversed_str + element

# print(text)
# print(text_stripped)
# print(text_lst) 
# print(reversed_lst)
# print(reversed_str)

if text_stripped == reversed_str:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
    
