from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    listALines = []
    listBLines = []
    stringA = ""
    stringB = ""

    """loop through each character and store it in a string then store that string into a list once the line is complete"""
    for index in range(len(a)):
        if a[index] != "\n":
            stringA += a[index]
        if a[index] == "\n":
            listALines.append(stringA)
            stringA = ""
    if not listALines:
        if len(stringA) > 0:
            listALines.append(stringA)
            stringA = ""
    elif len(stringA) > 0:
        listALines.append(stringA)
        stringA = ""

    """loop through each character and store it in a string then store that string into a list once the line is complete"""
    for index in range(len(b)):
        if b[index] != "\n":
            stringB += b[index]
        if b[index] == "\n":
            listBLines.append(stringB)
            stringB = ""
    if not listBLines:
        if len(stringB) > 0:
            listBLines.append(stringB)
    elif len(stringB) > 0:
        listBLines.append(stringB)
        stringB = ""

    return set(listALines).intersection(listBLines)


def sentences(a, b):
    """Return sentences in both a and b"""
    # TODO
    sentencesA = sent_tokenize(a)
    sentencesB = sent_tokenize(b)

    return set(sentencesA) & set(sentencesB)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    listALines = []
    listBLines = []
    stringA = ""
    stringB = ""

    for index in range(len(a)):
        if a[index] == "\n":
            continue
        substring = a[index:index+n]
        if len(substring) == n:
            listALines.append(substring)
    for index in range(len(b)):
        if b[index] == "\n":
            continue
        substring = b[index:index+n]
        if len(substring) == n:
            listBLines.append(substring)

    return set(listALines).intersection(listBLines)
