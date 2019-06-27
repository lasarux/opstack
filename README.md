# Stack

```$ ipython
Python 3.7.3 (default, May  1 2019, 11:43:13) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from stack import Stack                                                                                                

In [2]: a = Stack(10)                                                                                                          

In [3]: a.log('first value')                                                                                                   

In [4]: a += 5                                                                                                                 

In [5]: a.log('add 5 apples')                                                                                                  

In [6]: a.log()                                                                                                                
Out[6]: [('=', 10, 'first value'), ('+', 5, 'add 5 apples')]

In [7]: a -= 2                                                                                                                 

In [8]: a.log()                                                                                                                
Out[8]: [('=', 10, 'first value'), ('+', 5, 'add 5 apples'), ('-', 2, None)]

In [9]: int(a)                                                                                                                 
Out[9]: 13
```
