2017-07-06 Code testing
---
* When collaborating, how to make each other unblocked:
    - Brainstorm with the team: 
        Define shared data structures and public function signatures
    - Check the data structures
    - Write **stubs** for public functions: 
        - Define method signatures: input and output(write a dummy *return* for now)

* After finishing the **stubs**, think about **testing** **before** writing the production code: 
    - Black box method: separate everything that can be separated into functions
    - For Java: **@visibleForTesting**
    - Each test shall only cover **one single case**, write **informative test names**:
        e.g. testReadInternDataInternal_emptyListPasses()
             naming convention = test + function name + "_" + input + result
    - Use **setUp** function for unit testing! 
        - think about how many functions will need the setUp code
        - if only small amount of functions need a certain setUp code,
          then put then into separate test cases instead. 

* During your interview, use **test driven development** thinking: 
    - split functionalities as much as you can, go to **core functionalities**
    - don't try to write the entire code top-down
    - for less important parts like reading inputs etc, just write stubs
