# Write a function that checks if a given sentence is a palindrome.
#
# A palindrome is a word, phrase, verse, or sentence that reads the same backward or forward.
# Only the order of English alphabet letters (A-Z and a-z) should be considered, other characters should be ignored.
#
# For example, is_palindrome("Noel sees Leon.") should return true.
# Ignoring spaces, period, and case results in "noelseesleon", which is a palindrome since it reads same backward and forward.
 
# "Noel sees Leon."

def is_palindrome(text):
    start = 0
    end = len(text)-1
    if text == "":
        return True
    while start < end:
        if text[start].isalpha() and text[end].isalpha():
            startstr = text[start].lower()
            endstr = text[end].lower()
            if startstr == endstr:
                start+=1
                end-=1
            else:
                return False
        elif text[start].isalpha():
            end-=1
        else:
            start+=1
                
    return True
 
# print(is_palindrome("Noel sees Leon."))
# print(is_palindrome("NoelseesLon"))
print(is_palindrome(""))
print(is_palindrome("123457876543567"))
print(is_palindrome("Noel12see44sLeon"))
# print(is_palindrome("Noel!2see&sLeon"))