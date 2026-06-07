import random

digitos_random = ''

for digito in range(9):
    digitos_random += str(random.randint(0, 9))

print(digitos_random)

nove_digitos_cpf = digitos_random

# multiplicadores dos digitos 1 e 2
multiplicador_digito_1 = 10
multiplicador_digito_2 = 11

# variaveis definidas fora do loop para guardar o resultado para o calculo posterior
resultado_digito_1 = 0
resultado_digito_2 = 0

for digito in nove_digitos_cpf:

    resultado_digito_1 += int(digito) * multiplicador_digito_1
    multiplicador_digito_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
if digito_1 > 9: 
    digito_1 = 0

for digito in nove_digitos_cpf + str(digito_1): # adicionando o digito 1 para o algoritmo

    resultado_digito_2 += int(digito) * multiplicador_digito_2
    multiplicador_digito_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11

if digito_2 > 9:
    digito_2 = 0

cpf_gerado = f'{nove_digitos_cpf}{digito_1}{digito_2}'

print(f'O CPF gerado foi: {cpf_gerado}')

