# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) in Python through a home-server storage-monitoring example. The completed program demonstrated inheritance, class and instance namespaces, shallow and deep copying, input validation, and error handling.

## Learning Objectives

- Create parent and child classes.
- Use inheritance to extend functionality.
- Understand class and instance namespaces.
- Demonstrate shallow and deep copying.
- Apply object-oriented design principles.

## Requirements Completed

1. **Parent class (TODO 1):** Created `ParentClass` with the class variable `device_category`, instance variables `name` and `status`, a constructor, and `get_info()`. Also implemented `__str__()` to provide a readable device representation.
2. **Child class (TODO 2):** Created `ChildClass(ParentClass)` with the class variables `device_type` and `valid_drive_states`, and instance variables `capacity_tb` and `drives`. Reused initialization through `super()`, overrode `get_info()`, and added `health_summary()`.
3. **Namespaces (TODO 3):** Created two child objects, accessed `device_type` through both the class and an instance, added `rack_location` only to the first object, and displayed the instance and class dictionaries using `__dict__`.
4. **Object copying (TODO 4):** Created a storage-server object holding a list of drive dictionaries, made copies using `copy()` and `deepcopy()`, and changed a nested drive status in the original object. The shallow copy reflected the change; the deep copy retained the original nested values.
5. **Main function (TODO 5):** Created parent and child objects, displayed their information, checked inheritance, and called the namespace and copying demonstrations.
6. **Student-created extension:** Added `update_drive_status()` to change an existing drive's health. The method validated the bay and health input, raised `ValueError` for invalid inputs, and raised `KeyError` for an unknown bay. The `main()` function caught the unknown-bay error so the demonstration continued.

## How the Program Was Run

The program was run from the `unit1_oop` folder using Python 3:

```bash
python3 -B unit1_discussion.py
```

The `-B` option prevented Python from writing bytecode cache files. The observed output displayed all five TODO demonstrations and the extension without a runtime exception. The initial invalid drive-bay operation was handled and reported in the output.

## Design, Memory Use, and Overhead

The parent class kept common device information and behavior together, while the child class added storage-specific behavior without duplicating the parent constructor. The child constructor used `deepcopy(drives)` to prevent later modifications to a caller's original list from changing the instance's drive records. Input validation rejected unsupported drive states, duplicate or empty bay names, and invalid storage capacity values in the implemented checks.

The `drives` attribute stored a list of dictionaries. Holding more drive records required additional memory that generally grew with the number of records. A shallow copy made a new outer object but continued to reference the existing nested drive list. A deep copy recursively duplicated the nested data, usually consuming more memory and CPU time as the data set grew. The example showed why sharing mutable data could be efficient but could also produce unexpected side effects.

## Discussion Board Reflection (150–200 words)

While completing this assignment, I learned how to organize Python code into parent and child classes and use inheritance to share common functionality. I practiced overriding a method, examining class and instance namespaces with `__dict__`, and comparing shallow and deep copies of nested objects. I also added a drive-status update method with validation and exception handling.

One challenge was getting the complete code into the correct Python file. I initially ran unfinished starter sections, then corrected the file and tested each TODO separately. Another challenge was understanding why changing a nested drive record also affected the shallow copy. Comparing the original and copied objects helped me see how shared references work.

Procedural programming mainly organizes a task into functions and steps, while OOP groups related data and behavior into objects. OOP can make larger systems easier to maintain and extend because common functionality can be reused. However, extra classes, object state, and deep copying can introduce complexity and processing or memory overhead. The storage-server example showed how these tradeoffs apply to practical monitoring software. I could use the same approach in future server-automation or locally hosted AI projects.

## GitHub Repository

https://github.com/agent007moss/CMSC315-Discussions

The completed Python source and this README were intended to be committed together in the existing `unit1_oop` directory.
