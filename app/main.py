from app.util.lib import checkDigit
from app.util.stack import StackUsingArray

class SevenDisplay(object):
    
    def __init__(self,list_of_number):
        super()
        self.number_str = int(list_of_number)
        self.stack = StackUsingArray()
    
    def generateSevenNumber(self):
        modulo = 10
        rest = self.number_str
        while rest != 0 :
            value = checkDigit(rest % modulo)
            self.stack.push(value)
            rest = rest // modulo

    def printDigitalNumber(self):

        while not self.stack.isEmpty():
            queue_tmp = self.stack.pop()
            while len(queue_tmp) > 0:
                ascii = queue_tmp.pop(0)
                if (ascii != "\n"):
                  print(ascii,end='')
                else:
                  print()
            
    def toString(self):

        text = ""
        while not self.stack.isEmpty():
            queue_tmp = self.stack.pop()
            while len(queue_tmp) > 0:
                ascii = queue_tmp.pop(0)
                text = text + ascii

        return text