def fibonacci(n):
    numeros = []
    a, b = 0, 1

    for i in range(n):
        numeros.append(a)
        a, b = b, a + b

    return numeros


n = 10
print(fibonacci(n))