n1 = int(input("Digite el primer numero a agregar: "))
n2 = int(input("Digite el segundo numero a agregar: "))
lam=lambda numero1,numero2: 1 if numero1>numero2 else -1
calcular=lam(n1,n2)
print("El primer número es mayor") if calcular == 1 else print("El segundo número es mayor")
