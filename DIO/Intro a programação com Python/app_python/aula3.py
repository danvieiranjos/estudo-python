a = int(input ('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Segundo valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
    result = a
elif b > a and b > c:
    print("O maior número é {}" .fomart(b))
    result = b
else:
    print('O maior número é {}'.format(c))
    result = c
print('Fim do teste de maior numero...\n')

if result % 2 == 0:
    print ("Este numero é par: \n{}" .format(result))
else:
    print ("Este numero é impar: \n{}" .format(result))
print("\n ...FIM")