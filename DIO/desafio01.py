n = int(input())
fib1 = 0
fib2 = 1
n = n - 1
fib_list = [fib1]

for i in range(0,n):
  soma = fib1 + fib2
  fib1 = fib2
  fib2 = soma
  fib_list.append(fib1)

fib_string = (' '.join(str(x) for x in fib_list))
print(fib_string)