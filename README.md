7display-draft

# Summary

This version only support console and printing in vertical column.

# Use

Python console

```

>>> from app.main import SevenDisplay
>>> sample = SevenDisplay(10)
>>> sample.generateSevenNumber()
>>> sample.toString()

```

or print value number digital:

```


>>> from app.main import SevenDisplay
>>> sample = SevenDisplay(123)
>>> sample.generateSevenNumber()
>>> sample.printDigitalNumber()
     
  |  
     
  |  
     
 - - 
    |
 - - 
|    
 - - 
 - - 
    |
 - - 
    |
 - - 
     
```

# Testing

 - [x] pytest