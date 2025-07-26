def english_ordinal(text):
    return sum(ord(c.lower()) - 96 for c in text if c.isalpha())

def full_reduction(text):
    values = [ord(c.lower()) - 96 for c in text if c.isalpha()]
    return sum((v - 1) % 9 + 1 for v in values)

def reverse_ordinal(text):
    return sum(27 - (ord(c.lower()) - 96) for c in text if c.isalpha())

def calculate_all_ciphers(text):
    return {
        "English Ordinal": english_ordinal(text),
        "Full Reduction": full_reduction(text),
        "Reverse Ordinal": reverse_ordinal(text)
    }

def match_symbols(gematria_values, symbol_db):
    matches = {}
    for cipher, value in gematria_values.items():
        matches[cipher] = [term for term, val in symbol_db.items() if val == value]
    return matches