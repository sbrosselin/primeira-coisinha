print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro!")
print("Atributos do personagem:\nForça: 6\nNadar: 9\nInteligência: 1,5\nAgilidade: 7\nPonto fraco: Alergia a vespas")
first_path = input("Você tem dois caminhos que pode escolher para seguir, você quer ir pela direita ou pela esquerda?\n")

if first_path == "esquerda":
    second_path = input("Boa escolha, porém você se depara com um rio a sua frente, você prefere esperar o barco que atravessa ou nadar agora?\n")
    if second_path == "esperar":
        third_path = input("Você chegou ao outro lado do rio e agora se depara com três portas a sua frente: verde, laranja e azul, qual porta irá entrar?\n")
        if third_path == "verde":
            print("PARABENS!!!!!\nVocê achou o tesouro que contém milhares de riquezas e um portal de volta para casa.\nYOU WIN")
        elif third_path == "laranja":
            print("Atrás da porta tinha um enxame de vespas, você foi picado e está agozinando até a morte.\nGAME OVER")
        elif third_path == "azul":
            print("Você entra na porta e ela automaticamente fecha, e fogo começa a vir por todos os lados e você é queimado vivo.\nGAME OVER")
        else:
            print("GAME OVER")
    else:
        print("Você foi atacado por um tubarão\nGAME OVER")

else:
    print("Indo pela direita você não percebeu e agora está em uma areia movediça apenas esperando pela inevitável morte.\nGAME OVER") 

input("pressione ENTER para sair")   




