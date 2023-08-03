from rfc_calculator.homoclave import calculate_homoclave


def test_case_0():
    assert calculate_homoclave('Perez Garcia Juan') == 'LN'

def test_case_1():
    assert calculate_homoclave('Del real Anzures Jose Antonio') == 'N9'

def test_case_2():
    assert calculate_homoclave('Muñoz Ortega Juan') == 'T6'

def test_case_3():
    assert calculate_homoclave('Muñoz Muñoz Juan') == 'RZ'

def test_case_4():
    assert calculate_homoclave('Argüelles Ortega Jesus') == 'JF'

def test_case_5():
    assert (calculate_homoclave('Argüelles Ortega Jesus') == calculate_homoclave('Arguelles Ortega Jesus')) == True

def test_case_6():
    assert calculate_homoclave('Perez&Gomez Garcia Juan') == '2R'
    
# Add more test cases here following the same pattern
