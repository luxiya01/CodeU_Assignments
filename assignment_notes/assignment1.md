Style comments
---
* Do all checks up front and then proceed with the main part of 
the function body as top-level code. 
    ```python
    if not (blabla):
        raise ValueError(...)
     main-logic
     ```
* Use docstring to explain special assumptions made by the funciton. 
* Utilize **built-in** functions: 
    ```python
    all(iterable)
    collections.defaultdict([default_factory[,...]])
    ```
* **Test cases**: 
    - a bit more code duplication is allowed
    - most important: test cases are straight forward to follow
