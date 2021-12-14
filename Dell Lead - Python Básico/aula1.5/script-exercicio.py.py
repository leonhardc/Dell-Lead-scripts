# imprime os numeros primos de 2 a 100

print("Numeros primos de 2 a 100")

for n in range(2, 100):
    n_eh_primo = True

    for x in range(2,n):
        if n%x == 0:
            # se existe um numero x entre 2 e n-1 em que n é divisível por x, 
            # então n não é primo
            n_eh_primo = False
            break

    if n_eh_primo:
        print(n, end = '; ')
