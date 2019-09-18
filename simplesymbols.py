#Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

#Use the Parameter Testing feature in the box below to test your code with different arguments.

def SimpleSymbols(str): 

  isItTrue = False
  for i in range(0, len(str)):
    if str[0].isalpha() or str[len(str)-1].isalpha():
      return "false"


    if str[i].isalpha():
      if str[i-1] == "+" and str[i+1] == "+":
        isItTrue = "true"
      else:
        return "false"
  # code goes here 
  return isItTrue
    
# keep this function call here  
print(SimpleSymbols(input()))
