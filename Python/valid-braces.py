#https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def validBraces(string):    
    endBracketList = [')', ']', '}']
    matches = {')':'(', ']':'[', '}':'{'}
    charList = list(string)
    charStack = [charList.__add__]

    if len(charList) % 2 != 0:
        return False
    

print(validBraces('()'))