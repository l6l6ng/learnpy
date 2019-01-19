def to_camel_case(text):
    if (text == ''):
        return ''

    return text[0] + ''.join(x.capitalize() for x in text.replace('_', '-').split('-'))[1:]

print(to_camel_case('the_stealth_warrior'))
print(to_camel_case('The-Stealth-Warrior'))
print(to_camel_case('A-B-C'))

print(64 ** (1/3))