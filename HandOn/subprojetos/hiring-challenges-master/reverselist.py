
# Lista Inversa com a função reverse
numbers = [1, 4, 8 ,0, 10, 20]
numbers.reverse()
print(numbers)

# Lista Inversa Usando Slice
numbers = [1, 4, 8 ,0, 10, 20]
print(numbers[::-1])

#Lista Inversa Ordenada com sort + reverse
numbers = [1, 4, 8 ,0, 10, 20]
numbers.sort(reverse=True)
print(numbers)

# Lista Inversa Usando função reversed
numbers = [1, 4, 8 ,0, 10, 20]
print(list(reversed(numbers)))

# -------- return ! 
[20, 10, 0, 8, 4, 1]
[20, 10, 0, 8, 4, 1]
[20, 10, 8, 4, 1, 0]
[20, 10, 0, 8, 4, 1]
