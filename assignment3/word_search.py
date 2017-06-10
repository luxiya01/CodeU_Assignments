#! /usr/bin/python3.5

import dictionary
ALL_WORDS = set()
WORD_DICT = None
CHAR_2D_ARRAY = None

def findAllWords(row, col, char2dArray, wordDict):
    global CHAR_2D_ARRAY, WORD_DICT
    CHAR_2D_ARRAY = char2dArray
    WORD_DICT = wordDict
    for i in range(row):
        for j in range(col):
            curr = CHAR_2D_ARRAY[i][j]
            if WORD_DICT.isPrefix(curr):
                visited = set()
                visited.add((row, col))
                findAllWordsFromCell(i, j, curr, visited)
    return ALL_WORDS

def findAllWordsFromCell(i, j, curr, visited):
    if WORD_DICT.isWord(curr):
        ALL_WORDS.add(curr)
    if i > 0:
        checkLeftRight(i-1, j, curr, visited)
        newCurr = curr + CHAR_2D_ARRAY[i-1][j]
        checkCell(i-1, j, newCurr, visited)
    if i < len(CHAR_2D_ARRAY) - 1:
        checkLeftRight(i+1, j, curr, visited)
        newCurr = curr + CHAR_2D_ARRAY[i+1][j]
        checkCell(i+1, j, newCurr, visited)
    checkLeftRight(i, j, curr, visited)

def checkLeftRight(i, j, curr, visited):
    if j > 0:
        newCurr = curr + CHAR_2D_ARRAY[i-1][j-1]
        checkCell(i, j-1, newCurr, visited)
    if j < len(CHAR_2D_ARRAY[i]) - 1:
        newCurr = curr + CHAR_2D_ARRAY[i][j+1]
        checkCell(i, j+1, newCurr, visited)


def checkCell(i, j, curr, visited): 
    if (i, j) not in visited and WORD_DICT.isPrefix(curr):
        visited.add((i, j))
        findAllWordsFromCell(i, j, curr, visited)

