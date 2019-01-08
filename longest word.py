def LongestWord(sen):
    longest_word = ''
    word_list = sen.split(" ")
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    
    sen = longest_word
    return sen
    
# keep this function call here  
print (LongestWord('I love dogs'))






