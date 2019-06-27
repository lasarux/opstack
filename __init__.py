class Stack(object):
    """number with memory"""
    _stack = []
    _log = []
    _operation = []

    def __init__(self, value=0, log=None):
        self._stack.append(value)
        if log:
            self._log.append(log)
        self._operation.append('=')

    def check_log(self):
        if len(self._log) != len(self._stack):
            self._log.append(None)

    def do_operations(self):
        for i, op in enumerate(self._operation):
            if op == '=':
                res = self._stack[i]
            elif op == '+':
                res += self._stack[i]
            elif op == '-':
                res -= self._stack[i]
            elif op == '*':
                res *= self._stack[i]
            elif op == '/':
                res /= self._stack[i]
        return res

    def __repr__(self):
        res = self.do_operations()
        return ('%0.2f' % res)

    def __add__(self, other):
        res = self.do_operations() + other
        return res

    def __iadd__(self, other):
        self.check_log()
        self._stack.append(other)
        self._operation.append('+')
        return self

    def __radd__(self, other):
        self.check_log()
        self._stack.append(other)
        self._operation.append('+')
        res = self.do_operations()
        return res

    def __sub__(self, other):
        res = self.do_operations() - other
        return res

    def __isub__(self, other):
        self.check_log()
        self._stack.append(other)
        self._operation.append('-')
        return self

    def __rsub__(self, other):
        self.check_log()
        self._stack.append(other)
        self._operation.append('-')
        res = self.do_operations()
        return res

    def __eq__(self, other):
        if type(other) == int:
            return  int(self.do_operations()) == other
        elif type(other) == float:
            return  float(self.do_operations()) == other
        else:
            raise TypeError('Type not supported')  

    def __lt__(self, other):
        if type(other) == int:
            return  int(self.do_operations()) < other
        elif type(other) == float:
            return  float(self.do_operations()) < other
    
    def __gt__(self, other):
        if type(other) == int:
            return  int(self.do_operations()) > other
        elif type(other) == float:
            return  float(self.do_operations()) > other

    def __le__(self, other):
        if type(other) == int:
            return  int(self.do_operations()) <= other
        elif type(other) == float:
            return  float(self.do_operations()) <= other
    
    def __ge__(self, other):
        if type(other) == int:
            return  int(self.do_operations()) >= other
        elif type(other) == float:
            return  float(self.do_operations()) >= other

    def __int__(self):
        return int(self.do_operations())

    def __float__(self):
        return float(self.do_operations())
    
    def log(self, info=None):
        if info:
            if len(self._log) < len(self._stack):
                self._log.append(info)
        else:
            self.check_log()
            return [i for i in zip(self._operation, self._stack, self._log)] 

