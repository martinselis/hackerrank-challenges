## staircase
#    # 
#   ##
#  ###
# ####

def stair(num):
    diff = num - 1
    space = " "
    hashtag = '#'
    counter = 1
    for i in range(num):
        print ('{}{}'.format(space*diff,hashtag*counter))
        diff = diff -1
        counter += 1

stair(5)
