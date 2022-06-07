from app.main import SevenDisplay

def test_its_string():

    efimerSeven = SevenDisplay("1234567890")
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == ""

def test_null():

    efimerSeven = SevenDisplay("")
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == ""

def test_its_a_number():

    efimerSeven = SevenDisplay(1234567890)
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() != "'     \n  |  \n     \n  |  \n     \n - - \n    |\n - - \n|    \n - - \n - - \n    |\n - - \n    |\n - - \n     \n|   |\n - - \n    |\n     \n - - \n|    \n - - \n    |\n - - \n - - \n|    \n - - \n|   |\n - - \n - - \n    |\n     \n    |\n     \n - - \n|   |\n - - \n|   |\n - - \n - - \n|   |\n - - \n    |\n - - \n - - \n|   |\n     \n|   |\n - - \n'"


def test_one_digital_number():

    efimerSeven = SevenDisplay(9)
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == ' - - \n|   |\n - - \n    |\n - - \n'

def test_list_digital_number():

    efimerSeven = SevenDisplay(91)
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == " - - \n|   |\n - - \n    |\n - - \n     \n  |  \n     \n  |  \n     \n"

def test_max_digital_number():

    efimerSeven = SevenDisplay(65535)
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == ' - - \n|    \n - - \n|   |\n - - \n - - \n|    \n - - \n    |\n - - \n - - \n|    \n - - \n    |\n - - \n - - \n    |\n - - \n    |\n - - \n - - \n|    \n - - \n    |\n - - \n'


def test_initial_digital_number():

    efimerSeven = SevenDisplay(0)
    efimerSeven.generateSevenNumber()
    assert efimerSeven.toString() == ' - - \n|   |\n     \n|   |\n - - \n'