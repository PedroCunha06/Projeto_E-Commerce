import re

def valida_cpf(cpf):
    cpf = str(cpf)
    
    if not cpf or len(cpf) != 11:
        print('Problema')
        return False
    
    nine_numbers = cpf[:9]
    factory_1 = 10
    result_1 = 0
    digit_1 = 0
    
    if cpf == cpf[0] * len(cpf):
        return False
    
    for item in nine_numbers:
        result_1 += (int(item)*factory_1)
        factory_1 -= 1
        
    digit_1 = (result_1 * 10) % 11
    digit_1 = 0 if digit_1 > 9 else digit_1
    
    ten_numbers = cpf[:9] + str(digit_1)
    factory_2 = 11
    result_2 = 0
    digit_2 = 0

    for item in ten_numbers:
        result_2 += (int(item) * factory_2)
        factory_2 -= 1

    digit_2 = (result_2 * 10) % 11
    digit_2 = 0 if digit_2 > 9 else digit_2
    
    new_cpf = f'{nine_numbers}{digit_1}{digit_2}'
    
    
    if new_cpf == cpf:
        return True
        
while True:
    cpf = input('Manda ...')
    teste = valida_cpf(cpf)
    print(teste)
    if teste:
        break