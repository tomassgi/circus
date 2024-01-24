# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
print("Welcome to circus!")
import random

position1 = 1 #sākuma kvadrāts abiem spēlētājiem
position2 = 1 

min_value=1 #metamā kauliņa mazākā un lielākā vērtība
max_value=6

player1_roll=random.randint(min_value, max_value) #abu spēlētāju matamie kauliņi 
player2_roll=random.randint(min_value, max_value)

for x in range(25):  #cikls
 
    pass

    player1_choice = input("Player 1 type 'roll' to roll the dice!")#pirmais speletajs met kaulinu

    if player1_choice == 'roll':
        position1= position1 + player1_roll
        print(player1_roll)
    print("Player1, you are on square:" + str(position1))

    player2_choice = input("Player 2, type 'roll' to roll the dice!")#otrais speletajs met kaulinu

    if player2_choice == 'roll':
        position2= position2 + player2_roll
        print(player2_roll)
        print("Player1, you are on square:" + str(position2))

    if position1 == 18:#trepes
        position1 == 7
        print("Player1, you have dropped down to square 7!")

    if position2 == 18:
        position2 == 7
        print("Player2, you have dropped down to square 7!")
    if position1 == 67:
        position1 == 46
        print("Player1, you have dropped down to square 46!")

    if position2 == 67:
        position2 == 46
        print("Player2, you have dropped down to square 46!")

    if position1 == 80:
        position1 == 69
        print("Player1, you have dropped down to square 69!")

    if position2 == 80:
        position2 == 69
        print("Player2, you have dropped down to square 69!")

    if position1 == 74:
        position1 == 63
        print("Player1, you have dropped down to square 63!")

    if position2 == 74:
        position2 == 63
        print("Player2, you have dropped down to square 63!")

    if position1 == 15:
        position1 == 24
        print("Player1, you have climbed up to square 24!")

    if position2 == 15:
        position2 == 24
        print("Player2, you have climbed up to square 24!")
    if position1 == 39:
        position1 == 48
        print("Player1, you have climbed up to square 48!")

    if position2 == 39:
        position2 == 48
        print("Player2, you have climbed up to square 48!")

    if position1 == 33:
        position1 == 52
        print("Player1, you have climbed up to square 52!")

    if position2 == 33:
        position2 == 52
        print("Player2, you have climbed up to square 52!")

    if position1 == 87:
        position1 == 96
        print("Player1, you have climbed up to square 96!")

    if position2 == 87:
        position2 == 96
        print("Player2, you have climbed up to square 96!")

    if position1 == 100:
        print("Player1, you have won!")


    if position2 == 100:
        print("Player2, you have won!") 

