import re


def convert_uppercase_to(name, symbol='_'):
    split = re.sub('(?!^)([A-Z][a-z]+)', r' \1', name).split()
    return symbol.join(split).lower()
