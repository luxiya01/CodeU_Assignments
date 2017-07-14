Assignment 4 reviews
---
* Python3 classes: will inherit from **object** anyhow
    ```python 
        class IslandCounter():
    ```
* List copying: 
    ```python 
        #method1: copy the reference of the list, 
        #         both new_list and old_list refer to the SAME LIST!!!
        new_list = old_list

        #method2: use the built-in list() function, now they refer to DIFFERENT lists. 
        new_list = list(old_list)

        #method3: use generic copy.copy(), slower than method2
        new_list = copy.copy(old_list)

        #method4: use generic copy.deepcopy(), slower than method3, but is a must 
        #         if the list contains objects. e.g. if it is a nested list orz... 
        new_list = copy.deepcopy(old_list)
    ```
* Tuple stuffs:
    - immutable data value
    - packing & unpacking
    ```python
        x = (123, 456, 789) #() is optional
        n1, n2, n3 = x
    ```
    - **namedtuple**:
    ```python
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(11, y=22)
        x, y = p #unpacking works as usual
        x_coordinate = p.x #accessing fields by name
    ```
* Testing:
    - split test cases into small ones that check one specific thing. 
