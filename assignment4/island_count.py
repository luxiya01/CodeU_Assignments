# Author: Li Ling
# Last modified: 2017-06-25
import copy

class IslandCounter():
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
        modified_landscape = copy.deepcopy(self.landscape)
        for i in range(self.row):
            for j in range(self.col):
                if modified_landscape[i][j]:
                    self._update_visited_tiles(modified_landscape, i, j)
                    islands += 1
        return islands

    def _update_visited_tiles(self, modified_landscape, i, j):
        """Update the modified_landscape by recursive flood filling method."""
        island = list()
        modified_landscape[i][j] = False
        island.append((i, j))
        while island:
            i, j = island.pop()
            for i_offset, j_offset in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if self._is_unvisited_land_tile(modified_landscape, i + i_offset, j + j_offset):
                    modified_landscape[i + i_offset][j + j_offset] = False
                    island.append((i + i_offset, j + j_offset))


    def _is_unvisited_land_tile(self, modified_landscape, i, j):
        return 0 <= i < self.row and 0 <= j < self.col and modified_landscape[i][j]
