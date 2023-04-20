# Crie um programa que leia os nomes dentro de uma lista e que imprima se
# cada número é primo ou não.
# Cria uma lista com o nome da variável "listas" e os números armazenados nela.
listas = [3, 4, 5, 6, 7, 59, 101, 107, 159]


# Define uma função eh_primo que recebe n como argumento.
def eh_primo(n):
    # Verifica se o número n é maior que 1.
    if n <= 1:
        # Se o número for igual a 1, a função retorna sem fazer nada.
        return
    # Se um número for maior do que 1, a função executa um loop for que percorre os
    # números de 2 até a raiz quadrada de n + 1.
    for i in range(2, int(n**0.5) +1):
        # Dentro do loop for a função verifica se n é divisível por i usando o operador %(módulo)
        if n % i == 0:
            # Se n for divisível por i, a função retorna False (o número não é primo)
            return False
    # Se o loop for terminar sem encontrar nenhum divisor para n, a função retorna True (o número é primo).
    return True

# Executa um loop for percorrendo  cada número da lista "Listas" e atribui cada um  a variável n.
for n in listas:
    if eh_primo(n):
        print(f'{n} é um número primo')
    else:
        print(f'{n} não é primo')
