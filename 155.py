class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack != []:
            self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def getMin(self):
        if self.stack == []:
            return -1
        return min(self.stack)


minStack = MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); # return 0
minStack.pop();
minStack.top();    # return 2
minStack.getMin(); # return 1