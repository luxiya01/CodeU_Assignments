2017-06-08 Coding Like a Professional 
---
* Tips: 
    - Break down implementation into **small steps**
    - **Ask questions** early and often 

* How to code at Google: 
    0. Identify the problem
    1. Design a solution, write design docs and make change lists
        - Design doc shall include: 
            background, goals, non-goals, data formats, APIs, detailed designs
    2. Write production codes and tests and require reviews
    3. Test launch before actually releasing the update

* Code comments: 
    - Don't explain who, what or where (shall be clear from the code)
    - Explain **why** and maybe **how**
        - e.g. suggest future improvements;
          explain previous failures

* Google != Academia: 
    - Writing a program: 
        - Academia: from **scratch**
        - Google: **add** features to codebase
        - **A lot** of programmers working on the same codebase! 
            `Version control is important`
    - Error handling: 
        - A: abort
        - G: fall back to prev version? 
    - Logging: 
        - G: logs are crucial
    - Testing: 
        - G: automated test cases run forever
    - Internationalization: 
        - G: needs to handle multiple languages


