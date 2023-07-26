import pytest
from src.rfc_calculator.verification_digit import calculate_verification_digit


@pytest.mark.parametrize("rfc12Digits, expected", [
    ('GODE561231GR', '8'),
    ('AECS211112JP', 'A'),
    ('OOGE52071115', '1'),
])
def test_calculate(rfc12Digits, expected):
    result = calculate_verification_digit(rfc12Digits)
    assert result == expected