import re
import unicodedata

# Defining dictionary for character to two digit code mapping
char_map = {
  ' ': '00',
  '0': '00',
  '1': '01',
  '2': '02',
  '3': '03',
  '4': '04',
  '5': '05',
  '6': '06',
  '7': '07',
  '8': '08',
  '9': '09',
  '&': '10',
  'A': '11',
  'B': '12',
  'C': '13',
  'D': '14',
  'E': '15',
  'F': '16',
  'G': '17',
  'H': '18',
  'I': '19',
  'J': '21',
  'K': '22',
  'L': '23',
  'M': '24',
  'N': '25',
  'O': '26',
  'P': '27',
  'Q': '28',
  'R': '29',
  'S': '32',
  'T': '33',
  'U': '34',
  'V': '35',
  'W': '36',
  'X': '37',
  'Y': '38',
  'Z': '39',
  'Ñ': '40'
}

# Defining digits for calculation
digits = '123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'

# Function to normalize input
def normalize(input):
    input = input.upper()
    input = unicodedata.normalize('NFD', input)
    input = re.sub(r'[\u0300-\u0302\u0304-\u036f]', '', input)  # remove accents
    input = input.replace('N\u0303', 'Ñ')  # replace "N" followed by a tilde with "Ñ"
    input = re.sub(r'[-\.,]', '', input)  # remove .'-,
    input = input.replace('-','').replace('.','').replace("'",'').replace(',','')
    return input


# Function to map character to two digit code
def map_character_to_two_digits_code(c):
    m = char_map.get(c)
    if not m:
        raise ValueError(f"No two-digit code mapping for char {c}")
    return m

# Function to calculate sum of pairs of digits
def sum_pairs_of_digits(input):
    sum = 0
    for i in range(len(input) - 1):
        first_pair = int(input[i:i+2])
        second_pair = int(input[i+1:i+2])
        sum += first_pair * second_pair
    return sum

# Function to calculate the code from full name
def calculate_homoclave(full_name):
    mapped_full_name = '0' + ''.join(map_character_to_two_digits_code(c) for c in normalize(full_name))
    sum = sum_pairs_of_digits(mapped_full_name)
    last_three_digits = sum % 1000
    quo = last_three_digits // 34
    reminder = last_three_digits % 34
    return digits[quo] + digits[reminder]
