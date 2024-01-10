# Extra Exceptions
Extra Exceptions - library for those who lack the usual python exceptions.  
 [Documentation](https://gitbook)

#### To install `pip install extraexceptions` 

#### To import `import extraexceptions` or `from extraexceptons import *`  

----
# Library give a new exceptions:

### Logical Fallacies

----
# also Dont Stop Code:
Library can catch exceptions and output only text with error, but if it will be, for example:
```python
from extraexc import *


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