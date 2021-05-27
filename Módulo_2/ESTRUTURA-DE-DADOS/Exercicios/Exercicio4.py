# Crie 3 conjuntos conforme estrutura a seguir:
# setx = set(["apple", "mango"])
# sety = set(["mango", "orange"])
# setz = set(["mango"])
# Faça as seguintes operações sobre conjuntos:
# a) Faça a união dos três conjuntos e imprima o resultado
# b) Verifique quais os elementos comuns do conjunto setx e sety e imprima o resultado
# c) Verifique se o conjunto setx é subconjunto do conjunto sety e setz utilizando
# issubset()
# d) Verifique quais elementos do conjunto setx não existem em sety

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

# a) Faça a união dos três conjuntos e imprima o resultado
uniaoSets = setx | sety | setz
print(uniaoSets)

# b) Verifique quais os elementos comuns do conjunto setx e sety e imprima o resultado
comumSetxSety = setx & sety
print(comumSetxSety)
# c) Verifique se o conjunto setx é subconjunto do conjunto sety e setz utilizando issubset()
subconjSetXY = setx.issubset(sety)
subconjSetXZ = setx.issubset(setz)
print(subconjSetXY)
print(subconjSetXZ)

# d) Verifique quais elementos do conjunto setx não existem em sety
difSetXeSetY = setx - sety
print(difSetXeSetY)