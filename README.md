# Extra Exceptions
Extra Exceptions - library for those who lack the usual python exceptions.  
Documentation will be soon...

#### To install `pip install extraexceptions` 

#### To import `import extraexceptions` or `from extraexceptons import *`  

----
# Library give a new exceptions:

Logical Fallacies - new 74 excepts.  
Cognitive Biases - new 56 excepts.  



----
# Don't Stop Code Decorator:
Library can catch exceptions and output only text with error, but if it will be, for example:
```python
from extraexceptions import *


@ignore_exc_decorator
def div(x, y):
    return x / y


print(div(5, 0))
```

you will receive:
```
Exception>>> division by zero
None
```
None - because x/y return traceback, but decorator catch his and function cant assign a value to return.