# 188.956.410-94
cpf = '188956410'
multiplicador = 10
digitos_multiplicados = []

for i, digito in enumerate(cpf):

    resultado_digito = int(digito) * multiplicador
    digitos_multiplicados.append(resultado_digito)
    
    multiplicador -= 1

print(digitos_multiplicados)

for digito in digitos_multiplicados:
    ...