#create pieces_lists such that the first (0th) element will have the display for that row for zero, etc.
first_row_pieces = ['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###']
second_row_pieces = ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #']
third_row_pieces = ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###']
fourth_row_pieces = ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #']
fifth_row_pieces = ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']

# print(first_row_pieces)
# print(second_row_pieces)
# print(third_row_pieces)
# print(fourth_row_pieces)
# print(fifth_row_pieces)

def seven_segment_display(number):
    #create strings to build the display out of:
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
    fifth_row = ''
    try: 
        number = str(number) #turn it into a string so we can get its length
    except:
        pass #do nothing if it is already a string
    
    remaining_length = len(number) # dummy variable so I can treat digits after the first differently with regards to spacing
    #print(remaining_length)
    for digit in number:
        if remaining_length > 1: #to put spaces in if another digit is coming after this one
            # print(len(first_row_pieces))
            # print(first_row_pieces[8])
            # print('remaining_length > 1: ', remaining_length )
            first_row = first_row + first_row_pieces[int(digit)] + '   '
            second_row = second_row + second_row_pieces[int(digit)] + '   '
            third_row = third_row + third_row_pieces[int(digit)] + '   '
            fourth_row = fourth_row + fourth_row_pieces[int(digit)] + '   '
            fifth_row = fifth_row + fifth_row_pieces[int(digit)] + '   '
            remaining_length -= 1
        else: #to only put in the #'s with no spaces afterwards for the last digit
            #print('remaining_length == 1: ', remaining_length )
            first_row = first_row + first_row_pieces[int(digit)]
            second_row = second_row + second_row_pieces[int(digit)]
            third_row = third_row + third_row_pieces[int(digit)]
            fourth_row = fourth_row + fourth_row_pieces[int(digit)]
            fifth_row = fifth_row + fifth_row_pieces[int(digit)]
        
    #to better handle the \n line breaks, set the desired print out to a variable and then return the variable
    statement = first_row + '\n' + second_row + '\n' + third_row + '\n' + fourth_row + '\n' + fifth_row + '\n'
    return statement
    

print(seven_segment_display(1234567890))