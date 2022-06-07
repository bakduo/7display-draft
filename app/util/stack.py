class StackUsingArray:
    def __init__(self):
        self.stack = []

    #Method to append the element in the stack at top position.
    def push(self, element):
        self.stack.append(element)

    #Method to Pop last element from the top of the stack
    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1] #Save the last element to return
            del(self.stack[-1]) #Remove the last element
            return lastElement
        else:
            return("Stack Already Empty")

    #Method to check if stack is empty or not
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)