Assignment3: Find all words in a dictionary
---
```python
    # iterate over neighbouring cells! 
    for i in xrange(max(row - 1, 0), min(row + 2, ROW)):
        for j in xrange(max(col - 1, 0), min(col + 2, COL)):
```
- `xrange` vs `range`:
    * Time: `xrange` is slightly slower
    * Space: `xrange` uses A LOT LESS space!!!

### Important stuffs to think about 
- marking *visited* nodes correctly
- enumerate neighbors cleanly! (see above)
- code duplication in recursion
- analyzing complexity step by step
