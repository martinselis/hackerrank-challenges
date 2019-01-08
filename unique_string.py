class UniqueChars():
    def __init__(self, string):
        self.string = string

    def has_unique_chars(self):
        for i in list(self.string):
            if list(self.string).count(i) > 1:
                return False
        return True

a = UniqueChars('abd')
print(a.has_unique_chars())



##unique_string = 'this is where its at'
##
##unique_string = list(unique_string)
##unique_letters = []
##for i in unique_string:
##    if unique_string.count(i) == 1:
##        unique_letters.append(i)
##    
##print (unique_letters)
##
##    
##        
