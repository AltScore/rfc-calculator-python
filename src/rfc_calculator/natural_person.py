import re
from dataclasses import dataclass
from typing import Optional

import unicodedata

def remove_accents(input_str: str) -> str:
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def date_code(day: int, month: int, year: int) -> str:
    return str(year)[-2:] + zero_padded(month) + zero_padded(day)

def zero_padded(n: int) -> str:
    return str(n).zfill(2)



SPECIAL_PARTICLES = ['DE', 'LA', 'LAS', 'MC', 'VON', 'DEL', 'LOS', 'Y', 'MAC', 'VAN', 'MI']

SPECIAL_PARTICLES_REGEX = re.compile(
    '(?:' +
    '|'.join(f'^{p} | {p} | {p}$' for p in SPECIAL_PARTICLES) +
    ')',
    re.IGNORECASE
)

@dataclass
class NaturalPerson:
    name: str
    first_last_name: str
    second_last_name: str
    day: int
    month: int
    year: int

    def natural_person_ten_digits_code(self) -> str:
        return self._obfuscate_forbidden_words(self._name_code()) + self._birthday_code()

    def full_name(self):
        return f"{self.first_last_name} {self.second_last_name} {self.name}"

    def _birthday_code(self) -> str:
        return date_code(self.day, self.month, self.year)  # Assuming this function is implemented elsewhere

    def _name_code(self) -> str:
        filtered_person_name = self._get_filtered_person_name()

        if self._is_empty(self.first_last_name):
            return self._normalize(self.second_last_name)[:2] + filtered_person_name[:2]
        elif self._is_empty(self.second_last_name):
            return self._normalize(self.first_last_name)[:2] + filtered_person_name[:2]
        elif self._is_first_last_name_too_short():
            return self._normalize(self.first_last_name)[0] + self._normalize(self.second_last_name)[0] + filtered_person_name[:2]
        else:
            return self._normalize(self.first_last_name)[0] + self._first_vowel_excluding_first_character_of(self._normalize(self.first_last_name)) + self._normalize(self.second_last_name)[0] + filtered_person_name[0]

    def _obfuscate_forbidden_words(self, s: str) -> str:
        forbidden_words = ["BUEI", "BUEY", "CACO", "CACA", "CAGA", "KOGE", "KAKA", "MAME", 
                        "KOJO", "KULO", "QULO", "CAGO", "COGE", "COJE", "FETO", "JOTO", 
                        "KAGO", "KACO", "MAMO", "MEAR", "MEON", "MION", "MOCO", "MULA", 
                        "PEDO", "PEDA", "PENE", "PUTO", "PUTA", "RATA", "RUIN"]

        if any(s.startswith(word) for word in forbidden_words):
            return s[:3] + 'X'
        else:
            return s


    def _get_filtered_person_name(self) -> str:
        normalized = self._normalize(self.name)
        if len(self.name.split(' ')) > 1:
            return re.sub(r'^(JOSE|MARIA|MA|MA\.)\s+', '', normalized, flags=re.IGNORECASE)
        else:
            return normalized

    def _normalize(self, s: str) -> str:
        return re.sub(r'\s+', ' ', re.sub(SPECIAL_PARTICLES_REGEX, '', re.sub(r'\s+', '  ', remove_accents(s.upper())))).strip()
    

    def _first_vowel_excluding_first_character_of(self, s: str) -> str:
        result = re.search(r'[aeiou]', s[1:], flags=re.IGNORECASE)
        if not result:
            raise Exception('')
        return result.group()

    def _is_first_last_name_too_short(self) -> bool:
        return len(self._normalize(self.first_last_name)) <= 2

    def _is_empty(self, s: str) -> bool:
        return not s or len(self._normalize(s)) == 0
        