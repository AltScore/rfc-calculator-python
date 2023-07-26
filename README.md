# AltScore Python SDK

This is the Python SDK for AltScore. It provides a simple interface to the AltScore API.

# RFC Calculator

This Python package provides a simple and intuitive way to calculate the Mexican tax id (Registro Federal de Contribuyentes - RFC) for a natural person. The RFC is a unique code for each individual and legal entity in Mexico.

## Installation

To install the package, you can simply use pip:

```bash
pip install rfc_calculator
```

## Usage

To use the package, you first need to import the `NaturalPerson` class and the `calculate_rfc` function:

```python
from rfc_calculator import NaturalPerson, calculate_rfc
```

Then, create a `NaturalPerson` instance with the person's full name and birth date, and pass this instance to the `calculate_rfc` function to calculate the RFC.

```python
rfc = calculate_rfc(NaturalPerson(name='Saturnina', first_last_name='Angel', second_last_name='Cruz', day=12, month=11, year=1921))
print(rfc)  # Outputs: 'AECS211112JPA'
```

In this example, 'Saturnina' is the person's name, 'Angel' is the first last name (or paternal surname), 'Cruz' is the second last name (or maternal surname), and the date of birth is November 12, 1921.

That's it! You now know how to calculate the RFC for a natural person in Python using the `rfc_calculator` package.
