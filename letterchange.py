#https://coderbyte.com/results/emsqre:Letter%20Changes:Python3
#Have the function LetterChanges(str)
#take the str parameter being passed and modify it using the following algorithm. 
#Replace every letter in the string with the letter following it in the alphabet 
#(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and 
#finally return this modified string. 
#Use the Parameter Testing feature in the box below to test your code with different arguments.

def LetterChanges(str): 

    # code goes here 
    incrementedValue = ""
    for x in range (0,len(str)):
      if str[x].isalpha():
        checkCharacter = (chr(ord(str[x])+1))
        if checkCharacter in ('a', 'e', 'i', 'o', 'u'):
          checkCharacter = checkCharacter.upper()
        incrementedValue += checkCharacter
      else:
        incrementedValue += str[x]

    str = incrementedValue
    return str
    
# keep this function call here  
print(LetterChanges(input()))
