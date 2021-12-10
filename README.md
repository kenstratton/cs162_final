# Simple Calculator

## Tools:
    python 3.10.0
    tkinter 8.6.11
    pytest 6.2.5

## Overview
### ▼GUI Design
<img width="200" alt="Screen Shot 2021-12-10 at 2 19 08" src="https://user-images.githubusercontent.com/77530003/145444727-3215dbb1-5e41-47eb-8fa7-66ae44ee25af.png">

### ▼Design Tree
・Application class includes and manipulate Frame1, Frame2, LabelOutput, LabelInput, Calculator, and ErrorHandler.</br>
・The basic Exception is Error, and ZeroDivisionError inherits Error and overrides its method.

<img width="400" alt="Screen Shot 2021-12-10 at 3 25 50" src="https://user-images.githubusercontent.com/77530003/145454171-39eae5e2-6ef6-4420-a8f5-2539d6dc8636.png">

### ▼GUI components and events
・GUI of the application composes of Frame and Label from tkinter.</br>
・There are Frame1, Frame2, LabelOutput, and LabelInput. </br>
・Each Frame contains Label components which recive user input and display output for it.</br>
・Frame1 -> set warnign messages and user output on LabelOutput instances</br>
・Frame2 -> contains a set of LabelInput instances whicn recieve user input</br>
・LabelOutput -> actually display warning messages and user output</br>
・LabelInput -> actually recieve user input</br>

<img width="420" alt="Screen Shot 2021-12-10 at 3 12 39" src="https://user-images.githubusercontent.com/77530003/145452435-78dd7d22-0e9b-4b3b-be6c-7d1a71403244.png"><img width="439" alt="Screen Shot 2021-12-10 at 3 10 33" src="https://user-images.githubusercontent.com/77530003/145452232-c83dfedd-99b6-48b3-9401-308c6e3e1cb1.png"><img width="409" alt="Screen Shot 2021-12-10 at 3 10 04" src="https://user-images.githubusercontent.com/77530003/145452185-05c5249d-6a8a-4801-98db-3645ff6fc2a7.png"><img width="309" alt="Screen Shot 2021-12-10 at 3 44 53" src="https://user-images.githubusercontent.com/77530003/145456809-be83a314-1900-4f21-aa4e-6c71ed449ad9.png">

### ▼Code decomposition and organization
・In my program, basically codes are comprehended in a class form, and their roles are divided to methods.</br>
・In terms of module, there are app.py, components.py, and exceptions.py, and each organizes codes with a different aim.</br>
・app.py -> set up the whole program with class parts from components.py and exceptions.py (Application)</br>
・components.py -> have classes with classified methods to achive one role (Frame1, Frame2, LabelOutput, LabelInput, and Calculator)</br>
・exceptions.py -> have exception classes and a handler for them (Error, ZeroDivisionError, and ErrorHandler)

### ▼User IO
・A user can simply input by clicking input labels.</br>
・An output display shows a result of input so far by clicking the equal-mark label.

![cal](https://user-images.githubusercontent.com/77530003/145455448-a95c0ecf-547b-4517-a5de-19267df9cb50.gif)

### ▼Exceptions and Validation
・Generic Exception -> Error</br>
・Sub Exception -> ZeroDivisionError</br>
・ZeroDivisionError overides *warning()* of Error and rewrites a return value.</br>
・ErrorHandler holds two methods to validate and raise errors when wrong an input comes.

<img width="602" alt="Screen Shot 2021-12-10 at 2 26 50" src="https://user-images.githubusercontent.com/77530003/145445848-fb6b0ba0-172d-4dde-b86c-1f60f811dabd.png">

### ▼Inheritance
・LabelOutput and LabelOutput derives from Label of tkinter</br>
・Both classes set their attributes with *super().____init____()* </br>
・Despite inheriting the ability of Label, LabelOutput has identical methods *bg_press()* and *bg_release()*.</br>
・*bg_press()* -> change the background color when its instance is pressed</br>
・*bg_release()* -> turn in the original color when its instance is released

<img width="420" alt="Screen Shot 2021-12-10 at 3 12 39" src="https://user-images.githubusercontent.com/77530003/145452435-78dd7d22-0e9b-4b3b-be6c-7d1a71403244.png">


### ▼Tests
・The tests were aimed at three courses: </br>
・1 Whether Label components have proper attributes,</br>
・2 Whether validation and calculation are executed in a mainstream processing,</br>
・3 and Whether exceptions are raised and handled expectedly.</br>
・Required data is set in conftest.py supported by the *fixture()* decorator.</br>
・Use the pytest-mock plugin to use mock objects.</br>
・Mock helps alter output of methods for a while and test if interdependent methods or classes can properly work.</br>
・Fake a method for specific tests by mocker fixture -> *mocker.patch()* , 1st arg = a method path, 2nd = return_value</br>
・Test whether a mocked method has been called only once -> *assert_called_once_with()*, 1st arg = a method path, 2nd.. = args of the method

<img width="1000" alt="Screen Shot 2021-12-10 at 4 12 41" src="https://user-images.githubusercontent.com/77530003/145461127-ef5ea506-60ce-4d0d-b962-cc38512886b3.png">

