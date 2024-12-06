# memanggil file gempa dan import semua method/fungsi
from gempa import *

# membuat objek gempa dengan argumen
gempa1 = Gempa('banten', 1.2)
gempa2 = Gempa('palu', 6.1) 
gempa3 = Gempa('cianjur', 5.6)
gempa4 = Gempa('jayapura', 3.3)
gempa5 = Gempa('garut', 4.0)

# informasi gempa
print('## info gempa maseh ##')
print()
gempa1.dampak()

print('## info gempa maseh ##')
print()
gempa2.dampak()

print('## info gempa maseh ##')
print()
gempa3.dampak()

print('## info gempa maseh ##')
print()
gempa4.dampak()

print('## info gempa maseh ##')
print()
gempa5.dampak()
