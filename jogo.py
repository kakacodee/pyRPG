import time
from random import randint
from random import choice
import random
import pygame as pyg
import sys


list_player = []
def criar_Player():
    name = input('Digite o nome do player: ')
    level = 1
    inventario= [[] *4 for _ in range(2)]
    Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": level * 100,
        "Exp": 0,
        "Danobase": 25 * level,
        "Danomedio": 40 * level,
        "Danoespecial": 60 * level,
        "Stamina": 100,
        "StaminaMax": 100,
        "HpMax": 300,
        "Hp": 300,
        "Inventário": inventario,
        "Moedas": 0
    }
    list_player.append(Player)
    print(f"\nStatus do player: {list_player[0]}")
    time.sleep(0.5)


   



list_Monstro = []
def Gerar_Monstros():
    levelM = randint(1, 50)
    nomeM = random.choice(['Goblin', 'Orc', 'Serpente', 'Duende'])
    Monstro={
        "Nome": f"{nomeM} {levelM}",
        "Level": levelM,
        "Dano": 1 * levelM,
        "Hp": 3 * levelM
    }
    list_Monstro.append(Monstro)
    """
    for y in list_Monstro:
        print(f"Nome: {y['Nome']} | Level: {y['Level']} | Dano: {y['Dano']} | Hp {y['Hp']}")
    """
def gerar_M(nummonstro):
    for z in range(nummonstro):
        Gerar_Monstros()
        time.sleep(0.1)


def somar_stamina(x):
    if x['Stamina']+50 <= 120:
            x['Stamina'] +=50
def zerar_stamina(y,x):
    if x['Stamina'] <= 0:
            atacar_player(y,x)
            atacar_player(y,x)
            x['Stamina'] +=50

def atacar_npc(y, x):
    atac=[x['Danobase'] , x['Danomedio'], x['Danoespecial']]
    print('Lista de ataques: ')
    print(f"1 >> Chute: {x['Danobase']} \n2 >> Murro: {x['Danomedio']} \n3 >> Golpe karateca: {x['Danoespecial']}")
    atac_sort = int(input('Digite o número do ataque escolhido: '))
    if atac_sort == 1:
        time.sleep(0.5)
        y['Hp'] -= atac[0]
        print(f"Você usou o ataque Chute: {atac[0]}")
        x['Stamina'] -= 2
        zerar_stamina(y,x)
    if atac_sort == 2:
        time.sleep(0.5)
        y['Hp'] -= atac[1]
        print(f"Você usou o ataque Murro: {atac[1]}")
        x['Stamina'] -= 5
        zerar_stamina(y,x)
    if atac_sort == 3:
        time.sleep(0.5)
        y['Hp'] -= atac[2]
        print(f"Você usou o ataque Golpe Karateca: {atac[2]}")
        x['Stamina'] -= 20
        zerar_stamina(y,x)
    elif  0<atac_sort>3:
        time.sleep(0.5)
        print('Escolha um ataque válido')
        atacar_npc(y, x)
    if y['Hp'] <= 0:
        print("Você venceu!!!")
        return True
    return False
def atacar_player(y, x):
    x['Hp'] -= y['Dano']
    if x['Hp'] <= 0:
        time.sleep(0.5)
        print("Você morreu...")
        Reiniciar()
        return True
    return False

def combate(y,x):
    while y['Hp'] > 0 and x['Hp'] > 0:
        atacar_player(y,x)
        time.sleep(0.5)
        print(f"Status do Player: Hp: {x['Hp']}/{x['HpMax']}, Stamina: {x['Stamina']}/{x['StaminaMax']} | Status do Monstro: Hp: {y['Hp']}")
        print(f"\n")
        atacar_npc(y,x)
        time.sleep(0.5)
        print(f"Status do Player: Hp: {x['Hp']}/{x['HpMax']}, | Status do Monstro: Hp: {y['Hp']}")
        print(f"\n")
        Morte_vitoria(y,x)

def Reiniciar():
    time.sleep(0.5)
    reiniciar = str(input('Deseja recomeçar? \n [S]Sim \n  ou \n [N]Não: '))
    if reiniciar in ('S', 's'):
        list_player.clear()
        list_Monstro.clear()
        criar_Player()
        escolher_dificuldade()
    else:
        time.sleep(0.5)
        print("Até mais, guerreiro(a)")
        breakpoint
    
def Morte_vitoria(y,x):
    if y['Hp'] <= 0:
        time.sleep(0.5)
        print('Você venceu!!!')
        if x['Hp'] + 50 <=300:
            x['Hp'] += 50
        x['Exp'] += 10
        if x['Exp'] == 100:
            x['Exp'] = 0           
            x['Level'] += 1
        somar_stamina(x)
        print(list_player[0])
    elif x['Hp'] <= 0:
        time.sleep(0.5)
        print('Você Morreu...')
        Reiniciar()


def selecionar_monstro(difi):
    choices = {1: 9, 2: 19, 3: 29, 4: 99}
    max_choice = choices[difi]
    time.sleep(0.5)
    print('Apareceu um monstro nas sombras...')
    time.sleep(0.5)
    monstro_choice = int(input(f"Escolha um número de 0 a {max_choice} e o monstro será revelado: "))
    lista_choice = [monstro_choice]
    if 0 <= monstro_choice < len(list_Monstro):
        time.sleep(0.5)
        combate(list_Monstro[monstro_choice], list_player[0])
        list_Monstro.pop(monstro_choice)
        choices[difi] -=1
        
        #print(list_Monstro.index)
        
        andar(difi, list_player[0])
    elif list_Monstro is None:
        time.sleep(0.5)
        print('Você derrotou todos os monstros!!!!!! LEGENDÁRIO')
        escolher_dificuldade()
    elif monstro_choice > len(list_Monstro):
        time.sleep(0.5)
        print('Esse número já foi utilizado...')
        time.sleep(0.5)
        print(f"Números já escolhidos: {lista_choice}")
        selecionar_monstro(difi)
    else:
        time.sleep(0.5)
        print('Selecione um número válido... \n')
        
        selecionar_monstro(difi)



def escolher_dificuldade():
    dificuldade = ['Fácil', 'Normal', 'Difícil', 'INSANO!!']
    #print(f"Escolha uma dificuldade entre: \n {dificuldade[0]} \n {dificuldade[1]} \n {dificuldade[2]} \n {dificuldade[3]}")
    for num, dif in enumerate(dificuldade, 1):
        print(num, '>>', dif)
        time.sleep(0.5)
    difi = int(input('Digite o número da dificuldade escolhida: '))
    if 1<=difi<=4:
        gerar_M(12*difi)
        return difi
    else:
        time.sleep(0.5)
        print("Selecione uma dificuldade válida...")
        return escolher_dificuldade()   
    #selecionar_monstro(difi)

#escolher_dificuldade()

"""print('Monstros no mapa: ')
for y in list_Monstro:
        print(f"Nome: {y['Nome']} | Level: {y['Level']} | Dano: {y['Dano']} | Hp {y['Hp']}")
   """     
def bau_tesouro(x): #continuar essa função
    itens = random.choice(['Moedas', 'Poção de cura', 'Poção de exp'])
    time.sleep(0.5)
    print('\nVocê encontrou um baú!!!')
    
    if itens == 'Moedas':
        Moedas = random.choice([10, 20, 30, 40, 50, 60])
        x["Moedas"] += Moedas
        #time.sleep(0.5)
        print(f"Você recebeu {x['Moedas']} moedas.")
    elif itens == 'Poção de cura':
        hp = 30
        if x["Hp"] + hp <= 300:
            x["Hp"] += hp
            time.sleep(0.5)
        print(f"\nSeu Hp: {x['Hp']}")
    elif itens == 'Poção de exp':
        xp=30
        x["Exp"] += xp
        print(f"\nSeu Exp: {x['Exp']}")
        if x['Exp'] == 100:
            x['Exp'] = 0           
            x['Level'] += 1

        

def comerciante(difi, player):
    time.sleep(0.5)
    print("Você encontrou uma pessoa pela sua jornada:")
    time.sleep(0.5)
    print(f"\nSaudações guerreiro!!\nEu sou o comerciante local...")
    time.sleep(0.5)
    print(f"Tenho alguns itens que talvez você goste hehe...\n")

    itens = ['poção de cura: 20x Moedas', 'poção de exp: 25x Moedas', 'poção de stamina: 15x Moedas', 'amuleto de vida: 60x Moedas', 'amuleto de ataque: 80x Moedas']
    #print(f"Produtos disponíveis: \n1>>{itens[0]} \n2>>{itens[1]} \n3>>{itens[2]} \n4>>{itens[3]} \n5>>{itens[4]}")
    time.sleep(0.5)
    comprar = str(input('Deseja comprar? \n[S]sim \n[N]não: '))
    if comprar in ('s', 'S', 'sim', 'Sim'):
        time.sleep(0.5)
        print(f"Produtos disponíveis: \n1>>{itens[0]} \n2>>{itens[1]} \n3>>{itens[2]} \n4>>{itens[3]} \n5>>{itens[4]}")
        time.sleep(0.5)
        produtos = int(input('Digite o número do produto que você deseja comprar: '))
        if produtos == 1:
            moedas = 20
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                player['Inventário'].append(itens[0])
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                andar(difi, player)
        if produtos == 2:
            moedas = 25
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                player['Inventário'].append(itens[1])
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                andar(difi, player)
        if produtos == 3:
            moedas = 15
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                player['Inventário'].append(itens[2])
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                andar(difi, player)
        if produtos == 4:
            moedas = 60
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                player['Inventário'].append(itens[3])
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                andar(difi, player)
        if produtos == 5:
            moedas = 80
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                player['Inventário'].append(itens[4])
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                andar(difi, player)
        else:
            print('Escolha um produto válido...')
            comerciante(difi, player)
    elif comprar in ('n', 'N', 'Não', 'não'):
        time.sleep(0.5)
        print('Você irá se arrepender disso...')
        andar(difi, player)




def direita(difi, player):
    sort_right = random.choice([lambda: selecionar_monstro(difi), lambda:'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player), lambda: comerciante(difi, player)])
    res = sort_right()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    sort_right() #continuar essa função
    
def esquerda(difi, player):
    sort_left = random.choice([lambda: selecionar_monstro(difi), lambda: 'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player), lambda: comerciante(difi, player)])
    res = sort_left()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    sort_left()
     #continuar essa função

def em_frente(difi, player):
    sort_front = random.choice([lambda: selecionar_monstro(difi), lambda:'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player), lambda: comerciante(difi, player)])
    res = sort_front()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    sort_front() #continuar essa função

def abrir_inventario(player):
        print(player['Inventário'])
"""
   else:
        print(player['Inventário'])
        Usar = str(input("Deseja usar/equipar algum item? \n[S]sim \n[N]não: "))"""
#Continuar daqui


def andar(difi, player): #continuar essa função
    opcoes = ['Ir para DIREITA', 'Ir para ESQUERDA', 'Ir em FRENTE', 'Abrir INVENTÁRIO']
    for num, step in enumerate(opcoes, 1):
        time.sleep(0.5)
        print(f"\n{num}>> {step}")
        time.sleep(0.5)
    op = int(input('\nDigite o número da opção escolhida: '))
    if op == 1:
        direita(difi, player)
        andar(difi, player)
    elif op == 2:
        esquerda(difi, player)
        andar(difi, player)
    elif op == 3:
        em_frente(difi, player)
        andar(difi, player)
    elif op == 4:
        abrir_inventario(player)
        andar(difi,player)
    else:
        time.sleep(0.5)
        print('Escolha uma opção válida')
        andar(difi, player)

        
def jogo():
    pyg.mixer.init()
    pyg.mixer.music.load("medieval.mp3")
    pyg.mixer.music.set_volume(0.25)
    pyg.mixer.music.play()
    criar_Player()
    player = list_player[0]
    dific = escolher_dificuldade()
    print('\nVocê, um guerreiro recém-treinado e ansioso para provar seu valor, foi convocado pelo Conselho dos Anciãos para defender o reino e investigar a origem desse mal.\nArmado com coragem e determinação, você sabe que essa é sua chance de se tornar uma lenda — ou desaparecer nas sombras...\n\nPrepare-se para uma jornada de mistérios e batalhas. O destino de Arvendale está em suas mãos.')
    andar(dific, player)
    
jogo()


