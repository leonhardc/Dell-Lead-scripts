class Animal:
    def __init__(self, nome='', especie=''):
        self.nome = nome
        self.especie = especie
        self.fome = 0

    def __str__(self):
        return 'Meu nome é {}, minha espécie é {}, meu nivel de fome é {}'.format(self.nome, self.especie, self.fome)

    def andar(self):
        self.fome += 1

    def comer(self, comida):
        if comida > self.fome:
            self.fome = 0
            raise Exception('Seu animalzinho comeu e ficou saciado, sobrou comida no prato!')
        else:
            self.fome -= comida

animal = Animal('Betoven', 'Cachorro')

while True:
    print('O que você quer fazer?\n')
    print('1 - Alimentar seu animalzinho.')
    print('2 - Andar com seu animalzinho.')
    print('3 - Mostrar o estado do seu animalzinho.')
    print('1 - Sair.\n')

    op = input('Escolha uma das opções acima: ')

    if op == '1':
        # dar comida para o animal
        try:
            comida = int(input('Quanto de comida você quer dar? '))
            animal.comer(comida)
        except Exception as e:
            print(e)

    elif op == '2':
        # andar com o animal
        animal.andar()

    elif op == '3':
        # mostrar o animal
        print(animal)

    elif op == '4':
        break
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!\n\n')

    print(animal)
