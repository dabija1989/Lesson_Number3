"""
 Extrageți un subșir de caractere
Scrieți un program care primește un șir de caractere ca intrare și extrage un subșir specific din acesta,
 bazat pe pozițiile de început și sfârșit definite de utilizator.
"""
# Solution

sir = input()
start = int(input())
finish = int(input())
subsir =sir[start:finish]
print(subsir)

