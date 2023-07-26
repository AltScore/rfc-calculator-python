from src.rfc_calculator.calculate_rfc import calculate_rfc 
from src.rfc_calculator.natural_person import NaturalPerson


def test_calculate_rfc_for_josue_zarzosa_with_particle_in_second_lastname():
    assert calculate_rfc(NaturalPerson(name='Josué', first_last_name='Zarzosa', second_last_name='de la Torre', day=5, month=8, year=1987)) == 'ZATJ870805CK6'

def test_calculate_rfc_for_eliud_orozco():
    assert calculate_rfc(NaturalPerson(name='Eliud', first_last_name='Orozco', second_last_name='Gomez', day=11, month=7, year=1952)) == 'OOGE520711151'

def test_calculate_rfc_for_saturnina_angel():
    assert calculate_rfc(NaturalPerson(name='Saturnina', first_last_name='Angel', second_last_name='Cruz', day=12, month=11, year=1921)) == 'AECS211112JPA'
