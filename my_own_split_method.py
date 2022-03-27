﻿def mysplit(strng):
    new_lst = [] # will be the new list
    new_lst_element = '' # will be used to create new items for the list
    for char in strng:
        if char != (' ' or '/n' or '/t' or '/v' or '/f' or '/r'): #if a whitespace character is not encountered
            new_lst_element = new_lst_element + char # add character to string for later adding to list
        else: #if a white space character is encountered
            if len(new_lst_element) > 0: #if the string has anything in it, it should be added to the list
                new_lst.append(new_lst_element) #DO NOT USE x = x.append(asdfsad). Append already changes the variable!
            new_lst_element = '' #reset the string
    else: #after the 'for' loop is completed, need to account for and add in the last word if the original string does not end with a whitespace character:
        if len(new_lst_element) > 0: #if the string has anything in it, it should be added to the list
                new_lst.append(new_lst_element) #DO NOT USE x = x.append(asdfsad). Append already changes the variable!
        return new_lst
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
