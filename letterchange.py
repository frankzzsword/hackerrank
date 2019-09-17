#https://coderbyte.com/results/emsqre:Letter%20Changes:Python3

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
