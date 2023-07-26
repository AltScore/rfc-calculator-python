from src.rfc_calculator.homoclave import calculate_homoclave
from src.rfc_calculator.verification_digit import calculate_verification_digit
from src.rfc_calculator.natural_person import NaturalPerson


def calculate_rfc(person: NaturalPerson) -> str:
    """
    Calculates the RFC for a given Mexican person
    """
    ten_digit_code = person.natural_person_ten_digits_code()
    homoclave = calculate_homoclave(person.full_name())
    verification_digit = calculate_verification_digit(ten_digit_code + homoclave)
    return ten_digit_code + homoclave + verification_digit
