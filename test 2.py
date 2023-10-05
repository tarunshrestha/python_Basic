def bool_to_word(boolean):
    # TODO
    if boolean == True:
        boolean = str(bool_to_word('Yes'))
        
    if boolean == False:
        boolean = str(bool_to_word('No'))
    
print(bool_to_word(True))
print(bool_to_word(False))