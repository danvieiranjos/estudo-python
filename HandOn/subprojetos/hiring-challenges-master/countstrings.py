word = str(input("Digite a frase a ser analisada: "))
letter = str(input("Informe qual caractere deseja consultar a quantidade "))
final_result = word.count(letter)

if letter in word:
  print(f'há {final_result} ocorrência(s) desse caractere')
else:
  print("Não há esse(s) caractere(s)")

