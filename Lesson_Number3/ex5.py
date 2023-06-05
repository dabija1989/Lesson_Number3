"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""
# Solution

sir = input()
sir_invers = sir[::-1]
# print(sir_invers)
print(sir == sir_invers)
