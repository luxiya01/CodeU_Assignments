2017-06-22 Code Health & Debugging
---
* Healthy code = easy to understand, maintain & add features
* Use **functions** to make code more reusable

##### Understandable code
* **Code is read much more often than it is written!**
* Three steps: 
    1. Use [style guide](google.github.io/styleguide)!
    2. Write it for the reader:
        - Careful with **naming**
            Don't use empty words like *helper*, *manager*, 
            make it more concrete to avoid bad extention! 
        - Single responsibility principle! 
            Avoid functions/classes that will have *and* in docs. 
        - Keep it simple, don't over-optimize
        - Don't implement things you don't need immediately!!!
        - Comments: 
            - explain **why**
            - remember to document the **classes**!!!
            - explain external **context**
    3. Code review

##### Code Debugging
* Use **enums** and **flags**. 
* Introduce classes instead of primitive datatypes to 
  abstract certain ideas. 
   -  E.g. Introduce classes _Point_ 
   and _Color_ for a class _DrawCircle_ to use. 
* Refactoring
