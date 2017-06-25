# Author: Li Ling
# Last modified: 2017-06-25

class IslandCounter(object):
    """Used to count the amount of islands in a 2d landscape
    of water and land.

    Instance variables:
        row: no.rows in the 2d array *landscape*
        col: no.cols in the 2d array *landscape*
        landscape: the 2d array of booleans denoting the structure of the map,
                   True=land, False=water
    """

    def __init__(self, row, col, landscape):
        self.row = row
        self.col = col
        self.landscape = landscape

    def count_islands(self):
        """ Loop through the landscape and count islands.
        A copy of the original landscape is made and modified on the go,
        but the original landscape is maintained. This means that the method
        can be called multiple times and the correct result will always be obtained.

        Return:
            number of islands in the original landscape.
        """
        islands = 0
        modified_landscape = self.landscape
        for i in range(self.row):
            for j in range(self.col):
                if modified_landscape[i][j]:
                    self.update_visited_tiles(modified_landscape, i, j)
                    islands += 1
        return islands

    def update_visited_tiles(self, modified_landscape, i, j):
        """Update the modified_landscape by recursive flood filling method."""
        curr_island = list()
        modified_landscape[i][j] = False
        curr_island.append((i, j))
        while curr_island:
            curr_tile = curr_island.pop()
            curr_i, curr_j = curr_tile[0], curr_tile[1]
            if curr_i > 0 and modified_landscape[curr_i-1][curr_j]:
                modified_landscape[curr_i-1][curr_j] = False
                curr_island.append((curr_i-1, curr_j))
            if curr_i < self.row-1 and modified_landscape[curr_i+1][curr_j]:
                modified_landscape[curr_i+1][curr_j] = False
                curr_island.append((curr_i+1, curr_j))
            if curr_j > 0 and modified_landscape[curr_i][curr_j-1]:
                modified_landscape[curr_i][curr_j-1] = False
                curr_island.append((curr_i, curr_j-1))
            if curr_j < self.col-1 and modified_landscape[curr_i][curr_j+1]:
                modified_landscape[curr_i][curr_j+1] = False
                curr_island.append((curr_i, curr_j+1))
