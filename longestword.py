# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
#
# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LongestWord(sen):

  words = {}
  word = ""
  length = 0
  for i in range(0, len(sen)):
    if sen[i].isalpha():
      word += sen[i]
      length += 1
      if i == len(sen)-1:
        if length > 0:
          words[word] = length

    if not sen[i].isalpha():
      words[word] = length
      length = 0
      word = ""
  length =0
  for key, value in words.items():
    if length < value:
      length = value
      sen = key

  return sen

# keep this function call here
print(LongestWord(input()))
