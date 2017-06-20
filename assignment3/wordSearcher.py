#! /usr/bin/python3.5

class WordSearcher(object):
    """WordSearcher holds relevant informations of the letter grid, 
    the dictionary and methods to find all valid words in the grid."""

    def __init__(self, row, col, char2dArray, wordDict):
        self.row = row
        self.col = col
        self.char2dArray = char2dArray
        self.wordDict = wordDict
        self.allWords = set()


    def findAllWords(self):
        """Find all valid words that can be formed in the char2dArray. 

        Returns: 
            self.allWords: a set containing all valid words found. 
        """
        for i in range(self.row):
            for j in range(self.col):
                curr = self.char2dArray[i][j]
                if self.wordDict.isPrefix(curr):
                    visited = set()
                    visited.add((self.row, self.col))
                    self.findAllWordsFromCell(i, j, curr, visited)
        return self.allWords


    def findAllWordsFromCell(self, i, j, curr, visited):
        """Find all words that begins with curr. 

        Args:
            i: row index of the current cell
            j: col index of the current cell
            curr: the current prefix string
            visited: all cells visited when forming curr

        Returns: 
            Nothing. Note that self.allWords is modified on the go. 
        """
        if self.wordDict.isWord(curr):
            self.allWords.add(curr)
        if i > 0:
            if j > 0:
                newCurr = curr + self.char2dArray[i-1][j-1]
                self.checkCell(i-1, j-1, newCurr, visited)
            if j < self.col - 1:
                newCurr = curr + self.char2dArray[i-1][j+1]
                self.checkCell(i-1, j+1, newCurr, visited)
            newCurr = curr + self.char2dArray[i-1][j]
            self.checkCell(i-1, j, newCurr, visited)
        if i < self.row - 1:
            if j > 0:
                newCurr = curr + self.char2dArray[i+1][j-1]
                self.checkCell(i+1, j-1, newCurr, visited)
            if j < self.col - 1:
                newCurr = curr + self.char2dArray[i+1][j+1]
                self.checkCell(i+1, j+1, newCurr, visited)
            newCurr = curr + self.char2dArray[i+1][j]
            self.checkCell(i+1, j, newCurr, visited)
        if j > 0:
            newCurr = curr + self.char2dArray[i][j-1]
            self.checkCell(i, j-1, newCurr, visited)
        if j < self.col - 1:
            newCurr = curr + self.char2dArray[i][j+1]
            self.checkCell(i, j+1, newCurr, visited)


    def checkCell(self, i, j, curr, visited): 
        """Check cell self.char2dArray[i][j]. 
        If self.char2dArray[i][j] is unvisited and curr is a valid prefix, 
        recursively call findAllWordsFromCell from cell self.char2dArray[i][j]. 

        Args:
            i: row index of the current cell
            j: col index of the current cell
            curr: the current prefix string
            visited: all cells visited when forming curr

        Returns: 
            Nothing. Note that self.allWords is modified on the go. 
        """
        if (i, j) not in visited and self.wordDict.isPrefix(curr):
            visited.add((i, j))
            self.findAllWordsFromCell(i, j, curr, visited)
