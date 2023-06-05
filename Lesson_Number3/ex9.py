"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""
# Solution
# Pentru alte semne de bunctuatie ce nu sunt incluse procedam la fel.
propozitie = input()
print(propozitie.replace('.', '')
                .replace(',', '')
                .replace('?', '')
                .replace('!', '')
                .replace("'", '')
                .replace('"', '')
                .replace(':', '')
                .replace(';', '')
                .replace('-', '')
                .replace('...', '')
                .replace('())', '')
                .replace('{}', ''))
