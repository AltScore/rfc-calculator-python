from src.rfc_calculator.natural_person import NaturalPerson


def test_simple_case():
    person = NaturalPerson(name='Juan', first_last_name='Barrios', second_last_name='Fernandez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'BAFJ701213'

def test_one_digit_month_day():
    person = NaturalPerson(name='Juan', first_last_name='Barrios', second_last_name='Fernandez', day=1, month=2, year=1970)
    assert person.natural_person_ten_digits_code() == 'BAFJ700201'

def test_date_after_year_2000():
    person = NaturalPerson(name='Juan', first_last_name='Barrios', second_last_name='Fernandez', day=1, month=12, year=2001)
    assert person.natural_person_ten_digits_code() == 'BAFJ011201'

def test_exclude_special_particles_in_both_last_names():
    person = NaturalPerson(name='Eric', first_last_name='Mc Gregor', second_last_name='Von Juarez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'GEJE701213'

def test_exclude_special_particles_in_first_last_name():
    person = NaturalPerson(name='Josue', first_last_name='de la Torre', second_last_name='Zarzosa', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'TOZJ701213'

def test_exclude_special_particles_in_second_last_name():
    person = NaturalPerson(name='Josue', first_last_name='Zarzosa', second_last_name='de la Torre', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'ZATJ701213'

def test_use_first_word_of_compound_first_last_name():
    person = NaturalPerson(name='Antonio', first_last_name='Ponce de León', second_last_name='Juarez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'POJA701213'

def test_use_first_two_letters_of_name_if_first_last_name_has_just_one_letter():
    person = NaturalPerson(name='Alvaro', first_last_name='de la O', second_last_name='Lozano', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'OLAL701213'

def test_use_first_two_letters_of_name_if_first_last_name_has_just_two_letters():
    person = NaturalPerson(name='Ernesto', first_last_name='Ek', second_last_name='Rivera', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'ERER701213'

def test_use_first_name_if_person_has_multiple_names():
    person = NaturalPerson(name='Luz María', first_last_name='Fernández', second_last_name='Juárez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'FEJL701213'

def test_use_second_name_if_person_has_multiple_names_and_first_name_is_jose():
    person = NaturalPerson(name='José Antonio', first_last_name='Camargo', second_last_name='Hernández', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'CAHA701213'

def test_use_second_name_if_person_has_multiple_names_and_first_name_is_maria():
    person = NaturalPerson(name='María Luisa', first_last_name='Ramírez', second_last_name='Sánchez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'RASL701213'

def test_use_second_name_if_person_has_multiple_names_and_first_name_is_ma():
    person = NaturalPerson(name='Ma Luisa', first_last_name='Ramírez', second_last_name='Sánchez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'RASL701213'

def test_use_second_name_if_person_has_multiple_names_and_first_name_is_ma_dot():
    person = NaturalPerson(name='Ma. Luisa', first_last_name='Ramírez', second_last_name='Sánchez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'RASL701213'

def test_use_first_two_letters_of_second_last_name_if_first_last_name_is_empty():
    person = NaturalPerson(name='Juan', first_last_name='', second_last_name='Martínez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'MAJU701213'

def test_use_first_two_letters_of_second_last_name_if_first_last_name_is_null():
    person = NaturalPerson(name='Juan', first_last_name=None, second_last_name='Martínez', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'MAJU701213'

def test_use_first_two_letters_of_first_last_name_if_second_last_name_is_empty():
    person = NaturalPerson(name='Gerarda', first_last_name='Zafra', second_last_name='', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'ZAGE701213'

def test_use_first_two_letters_of_first_last_name_if_second_last_name_is_null():
    person = NaturalPerson(name='Gerarda', first_last_name='Zafra', second_last_name=None, day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'ZAGE701213'

def test_replace_final_letter_with_x_if_name_code_makes_a_forbidden_word_buei():
    person = NaturalPerson(name='Ingrid', first_last_name='Bueno', second_last_name='Ezquerra', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'BUEX701213'

def test_replace_final_letter_with_x_if_name_code_makes_a_forbidden_word_buey():
    person = NaturalPerson(name='Yngrid', first_last_name='Bueno', second_last_name='Ezquerra', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'BUEX701213'

def test_use_ma_when_first_name_starts_with_ma_but_is_not_maria():
    person = NaturalPerson(name='Marco Antonio', first_last_name='Cano', second_last_name='Barraza', day=13, month=12, year=1970)
    assert person.natural_person_ten_digits_code() == 'CABM701213'
