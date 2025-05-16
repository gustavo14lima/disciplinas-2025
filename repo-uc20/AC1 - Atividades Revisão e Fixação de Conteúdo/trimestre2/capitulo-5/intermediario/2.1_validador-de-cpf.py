'''
2.1 Validação de CPF
Crie uma função validar_cpf(cpf) que retorna True se o CPF estiver no formato 999.999.999-99 usando expressão regular (re.fullmatch()).
'''

import re

def validar_cpf(cpf):
    return bool(re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf))

cpf = input("Digite um CPF (formato 999.999.999-99): ")
print("CPF válido?" , validar_cpf(cpf))
