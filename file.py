n = int(input("Digite o número:"))

# Verifica se o número é maior que 1
if n > 1:
    # Testa divisibilidade do número por todos os inteiros de 2 até n-1
    for i in range(2, n):
        if n % i == 0:
            print("O número", n, "não é primo")
            break
    else:
        print("O número", n, "é primo")
else:
    print("O número", n, "não é primo")
