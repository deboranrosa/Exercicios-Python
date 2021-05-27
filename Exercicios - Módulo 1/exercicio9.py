# -*- coding: utf-8 -*-

import re

# a) converta a string para maiúsculo
s = 'Mentorama';
print(s);

s = s.upper();
print(s);

# b) imprima-a de trás para frente
for letra in s[::-1]: 
    # s[::-1] -- usando um slice para imprimir a palavra de trás para frente
    print(letra);

# c) imprima somente as vogais

print(re.findall(r"[aeiou]", s, re.IGNORECASE));
