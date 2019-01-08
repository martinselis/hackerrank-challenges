##'k' = 'm'
##'o' = 'q'
##'e' = 'g'

def checker():
    global strng
    strng = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    for i in strng:
        if i == 'k':
            strng = strng.replace('k','m')
            return strng
        if i == 'o':
            strng = strng.replace('o','q')
            return strng
        if i == 'e':
            strng = strng.replace('e','g')
            return strng

checker()    
print (strng)
