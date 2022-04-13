'''
I: a string or string of words assuming all the characters
O: most occuring element in the string 
E: empty string > 0/one character > 1/no repeating > -1
C: not more than 256 ASCII characters, 1) case insensitive and 2) case sensitive
'''

def find_occuring(str):
    ch = ''
    d  = {}
    for s in str:
        if s.isalpha():
            s = s.lower()
            d[s] = d.get(s,0)+1
        else:
            d[s] = d.get(s,0)+1

    ch = max(d, key=d.get)
    oc = max(d.values())
    return ch, oc


word = "aaa11111234Aqbb"
print(find_occuring(word))
print(word.isalpha())

