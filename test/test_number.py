from app.main import SevenDisplay

def test_its_string():

    efimerSeven = SevenDisplay("1234567890")
    assert efimerSeven.toString() == ""

def test_null():

    efimerSeven = SevenDisplay("")
    assert efimerSeven.toString() == ""

def test_its_a_number():

    efimerSeven = SevenDisplay(1234567890)
    assert efimerSeven.toString() != ""


def test_one_digital_number():

    efimerSeven = SevenDisplay(9)
    assert efimerSeven.toString() != ""

def test_list_digital_number():

    efimerSeven = SevenDisplay(91)
    assert efimerSeven.toString() != ""

def test_max_digital_number():

    efimerSeven = SevenDisplay(65535)
    assert efimerSeven.toString() != ""


def test_initial_digital_number():

    efimerSeven = SevenDisplay(0)
    assert efimerSeven.toString() != ""