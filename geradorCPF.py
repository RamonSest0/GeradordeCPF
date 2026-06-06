"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

proximo passo - validar um CPF inteiro
"""

cpf = '746824890'
multiplicador_digito_1 = 10
multiplicador_digito_2 = 11
resultado_digito_1 = 0
resultado_digito_2 = 0

for digito in cpf:

    resultado_digito_1 += int(digito) * multiplicador_digito_1
    multiplicador_digito_1 -= 1
    print(resultado_digito_1)

digito_1 = (resultado_digito_1 * 10) % 11
if digito_1 > 9:
    digito_1 = 0

print(f'O primeiro digito do CPF é: {digito_1}')

for digito in cpf + str(digito_1):

    resultado_digito_2 += int(digito) * multiplicador_digito_2
    multiplicador_digito_2 -= 1
    print(resultado_digito_2)
    
digito_2 = (resultado_digito_2 * 10) % 11

if digito_2 > 9:
    digito_2 = 0

print(f'O segundo digito do CPF é: {digito_2}')