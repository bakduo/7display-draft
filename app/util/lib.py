##Source https://www.geeksforgeeks.org/print-numbers-digital-form/

##Modify for works with string without print
def prints(mat):     
    # If in matrix row number is even then
    # prints "-" otherwise prints "|"
    queue = []
    for i in range(5):
        for j in range(5):
            if (i % 2 == 0):
                if (mat[i][j] == 1):
                   queue.append('-')
                else:
                    queue.append(' ')
            else:
                if (mat[i][j] == 1):
                    queue.append('|')
                else:                   
                    queue.append(' ')
 
        queue.append('\n')
    
    return queue
     
def digit0():
     
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit1():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 0, 0, 0, 0 ],
            [ 0, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0 ],
            [ 0, 0, 1, 0, 0 ],
            [ 0, 0, 0, 0, 0 ] ]
             
    return prints(mat)
 
def digit2():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 0 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit3():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit4():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 0, 0, 0, 0 ] ]
             
    return prints(mat)
 
def digit5():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 0 ],
            [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit6():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 0 ],
            [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit7():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 0, 0, 0, 0 ] ]
             
    return prints(mat)
 
def digit8():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
def digit9():
 
    # In matrix 0 used for space
    # and 1 for either - or |
    mat = [ [ 0, 1, 0, 1, 0 ],
            [ 1, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 1 ],
            [ 0, 1, 0, 1, 0 ] ]
             
    return prints(mat)
 
  
# Function to check number
def checkDigit(num):
 
    # For digit 0
    if (num == 0):
      return digit0()
  
    # For digit 1
    elif (num == 1):
      return digit1()
  
    # For digit 2
    elif (num == 2):
        return digit2()
  
    # For digit 3
    elif (num == 3):
        return digit3()
  
    # For digit 4
    elif (num == 4):
        return digit4()
  
    # For digit 5
    elif (num == 5):
        return digit5()
  
    # For digit 6
    elif (num == 6):
       return digit6()
  
    # For digit 7
    elif (num == 7):
       return digit7()
  
    # For digit 8
    elif (num == 8):
       return digit8()
  
    # For digit 9
    elif (num == 9):
       return digit9()
  
# This code is contributed by rutvik_56
# And modify by bakduo 06-2022