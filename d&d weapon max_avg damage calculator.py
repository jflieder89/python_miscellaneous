def dmg_calc():
    dmg_input = input('Enter the damage with base damage first, with different damage types separated by a comma: ').lower()
    #dmg_input = '1d1 2, 1d6 +1 fire, 3d 6 electrical, 2d8+ 12 pois on'
    dmg_input = dmg_input.replace(' ', '') #remove all spaces
    # print(dmg_input)
    dmg_lst = dmg_input.split(',')
    # print(dmg_lst)
    dmg_dict = {} #create empty dictionary to be filled with damage info
    
    #first identify damage type if there is one (fire, poison, etc.) or if it's base damage:
    for dmg_type in dmg_lst: #iterate through damge types
        #print(dmg_type)
        alpha_counter = 0 #get a running count of alphabetic characters
        char_index = 0 #keep tabs on the index of the character
        for character in dmg_type: #iterate through characters of damage type
            if alpha_counter > 1 : #if there are is at least one more alphabetic character than the 'd' for dice
                #print('starting char_index is : ', char_index)
                dmg_type_name = dmg_type[char_index - 1:].strip()
                dmg_type_damage = dmg_type[:char_index - 1].strip()
                dmg_dict[dmg_type_name] = dmg_type_damage
                break #stop this for loop that is iterating through characters of the dmg_type
            if character.isalpha():
                alpha_counter += 1 # count up alphabetic characters
                char_index += 1 #increase the char_index for every iteration, including if the char was alphabetic
                #print("Character is: ", character, 'and alpha_counter is: ', alpha_counter)
            else: 
                char_index +=1 #increase the char_index for every iteration, including if the char was not alphabetic
        else: # this is for the case of base damage where only 1 alpha character is present
            if alpha_counter == 1: #need to specify this condition as this else statement will occur always after the for loop as it is in line with that for loop
             dmg_dict['base'] = dmg_type #since this base dmg_type is only the damage part, with no name/label
    #print(dmg_dict)
    dmg_max = 0
    dmg_avg = 0
    dmg_max_statement = []
    dmg_avg_statement = []

    for dmg_type in dmg_dict:
        bonus = penalty = 0 # (re)set the bonus or penalty damage to zero at the start of each damage type iteration
        if '+' in dmg_dict[dmg_type]: #if there is a bonus to the dice damage
            dmg_type_split = dmg_dict[dmg_type].split('+')
            bonus = int(dmg_type_split[-1])
            del dmg_type_split[-1] # remove the last element (bonus damage) so only dice damage is left
            # print(dmg_type_split)
            # print(type(dmg_type_split))
            dmg_type_dice_dmg = dmg_type_split[0].split('d') #identify dice damage
        elif '-' in dmg_dict[dmg_type]: #if there is a bonus to the dice damage
            dmg_type_split = dmg_dict[dmg_type].split('-')
            penalty = int(dmg_type_split[-1])
            del dmg_type_split[-1] # so only dice damage is left
            dmg_type_dice_dmg = dmg_type_split[0].split('d') #identify dice damage
        else: #there is only dice damage
            dmg_type_dice_dmg = dmg_dict[dmg_type].split('d')
        # print(dmg_type_dice_dmg)
        # print(bonus)
        dice_count = int(dmg_type_dice_dmg[0])
        dice_range = int(dmg_type_dice_dmg[1])
        
        dmg_type_max_dmg = (dice_count * dice_range ) + bonus - penalty
        # print(dmg_type_max_dmg)
        dmg_max += dmg_type_max_dmg
        blurb = 'The max ' + dmg_type + ' damage is ' + str(dmg_type_max_dmg) + '.'
        dmg_max_statement.append(blurb)
        
        dmg_type_avg_dmg = ( ( ( dice_range + 1 ) / 2 ) * dice_count ) + bonus - penalty
        dmg_avg += dmg_type_avg_dmg
        stuff = 'The avg ' + dmg_type + ' damage is ' + str(dmg_type_avg_dmg) + '.'
        dmg_avg_statement.append(stuff)
    
    # print(dmg_max)
    dmg_max_statement.insert(0, 'The total max damage is ' + str(dmg_max) + '.')
    #print(' '.join(dmg_max_statement))
    max_statement = ' '.join(dmg_max_statement)
    
    dmg_avg_statement.insert(0, 'The total avg damage is ' + str(dmg_avg) + '.')
    #print(' '.join(dmg_avg_statement))
    avg_statement = ' '.join(dmg_avg_statement)
    
    total_statement = max_statement + '\n' + avg_statement
    return total_statement
    
print(dmg_calc())



