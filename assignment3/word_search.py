#! /usr/bin/python3.5

import dictionary
ALL_WORDS = set()
WORD_DICT = None
CHAR_2D_ARRAY = None

def findAllWords(row, col, char2dArray, wordDict):
    """Find all valid words that can be formed in the char2dArray. 
    Note that CHAR_2D_ARRAY, WORD_DICT and ALL_WORDS are global variables. 

    Args:
        row: no.rows in char2dArray
        col: no.col in char2dArray
        char2dArray: the grid of letters where words are to be searched for
        wordDict: a dictionary containing methods isWord(string) and isPrefix(string)

    Returns: 
        ALL_WORDS: a set containing all valid words found. 
    """
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
    """Find all words that begins with curr. 

    Args:
        i: row index of the current cell
        j: col index of the current cell
        curr: the current prefix string
        visited: all cells visited when forming curr

    Returns: 
        Nothing. Note that ALL_WORDS is modified on the go. 
    """
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
    """Check cells to the left and right of CHAR_2D_ARRAY[i][j]. 

    Args:
        i: row index of the current cell
        j: col index of the current cell
        curr: the current prefix string
        visited: all cells visited when forming curr

    Returns: 
        Nothing. Note that ALL_WORDS is modified on the go. 
    """
    if j > 0:
        newCurr = curr + CHAR_2D_ARRAY[i-1][j-1]
        checkCell(i, j-1, newCurr, visited)
    if j < len(CHAR_2D_ARRAY[i]) - 1:
        newCurr = curr + CHAR_2D_ARRAY[i][j+1]
        checkCell(i, j+1, newCurr, visited)

def checkCell(i, j, curr, visited): 
    """Check cell CHAR_2D_ARRAY[i][j]. 
    If CHAR_2D_ARRAY[i][j] is unvisited and curr is a valid prefix, 
    recursively call findAllWordsFromCell from cell CHAR_2D_ARRAY[i][j]. 

    Args:
        i: row index of the current cell
        j: col index of the current cell
        curr: the current prefix string
        visited: all cells visited when forming curr

    Returns: 
        Nothing. Note that ALL_WORDS is modified on the go. 
    """
    if (i, j) not in visited and WORD_DICT.isPrefix(curr):
        visited.add((i, j))
        findAllWordsFromCell(i, j, curr, visited)

