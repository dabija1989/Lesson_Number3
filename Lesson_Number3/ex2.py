"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""
# Solution
sir = str(input())
# Calcularea numarului total de caractere
print(len(sir))
# Calcularea numarului total de vocale in sir

# Method1
print((sir.count('A')) + (sir.count('a')) +
      (sir.count('E')) + (sir.count('e')) +
      (sir.count('I')) + (sir.count('i')) +
      (sir.count('O')) + (sir.count('o')) +
      (sir.count('U')) + (sir.count('u')) +
      (sir.count('Ă')) + (sir.count('ă')) +
      (sir.count('Ȃ')) + (sir.count('ȃ')) +
      (sir.count('Î')) + (sir.count('î')))
# Calcularea numarului total de vocale in sir

# Method2
print((sir.upper().count('A')) + (sir.upper().count('E')) +
      (sir.upper().count('I')) + (sir.upper().count('O')) +
      (sir.upper().count('U')) + (sir.upper().count('Ă')) +
      (sir.upper().count('Ȃ')) + (sir.upper().count('Î')))

# Calcularea numarului total de consoane in sir
print((sir.lower().count('b')) + (sir.lower().count('c')) +
      (sir.lower().count('d')) + (sir.lower().count('f')) +
      (sir.lower().count('h')) + (sir.lower().count('j')) +
      (sir.lower().count('k')) + (sir.lower().count('l')) +
      (sir.lower().count('m')) + (sir.lower().count('n')) +
      (sir.lower().count('p')) + (sir.lower().count('q')) +
      (sir.lower().count('r')) + (sir.lower().count('s')) +
      (sir.lower().count('ş')) + (sir.lower().count('t')) +
      (sir.lower().count('ț')) + (sir.lower().count('v')) +
      (sir.lower().count('w')) + (sir.lower().count('x')) +
      (sir.lower().count('z')) + (sir.lower().count('y')))



