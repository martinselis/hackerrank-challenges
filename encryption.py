import math
def encryption(string):

    str_without_spaces = string.replace(" ", "")
    true_length = len(str_without_spaces)
    sqr_root_of_str = math.sqrt(true_length)
    rows = math.floor(sqr_root_of_str)
    columns = math.ceil(sqr_root_of_str)
           
    new_string_placeholder = ''
    counter = 0
    for i in str_without_spaces:
        counter += 1
        if counter > columns:
            new_string_placeholder = new_string_placeholder + ' '
            counter = 0
            counter += 1
        new_string_placeholder = new_string_placeholder + i
        
    list_to_encode = new_string_placeholder.split(" ")

    new_list = [None] * len(list_to_encode[0])

    for item in list_to_encode:
        row_counter = -1
        for letter in item:
            row_counter += 1
            try:
                new_list[row_counter] = new_list[row_counter] + letter
            except:
                new_list[row_counter] = letter

    encoded_string = " ".join(new_list)
    print (encoded_string)
    
my_string_test = 'chillout'
encryption(my_string_test)




        
