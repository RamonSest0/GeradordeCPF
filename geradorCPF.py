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
"""

# 188.956.410-94
cpf = '188956410'
multiplicador_digito_1 = 10
multiplicador_digito_1 = 11
digitos_multiplicados_1 = []
digitos_multiplicados_2 = []
soma_digitos_1 = 0
soma_digitos_2 = 0


for digito in cpf:

    resultado_digito = int(digito) * multiplicador_digito_1
    digitos_multiplicados_1.append(resultado_digito)
    
    multiplicador_digito_1 -= 1

print(digitos_multiplicados_1)

for digito in digitos_multiplicados_1:
    soma_digitos = digito + soma_digitos

resultado_multiplicado = soma_digitos * 10
resultado_final = resultado_multiplicado % 11

if resultado_final > 9:
    resultado_final = 0

print(f'O primeiro digito do CPF é: {resultado_final}')


