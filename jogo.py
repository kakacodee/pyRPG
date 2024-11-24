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
    inventario= [["Vazio"] *8 for _ in range(1)]
    classes = ["Arqueiro", "Cavaleiro", "Anão", "Mago", "Gladiador"]
    for x, clas in enumerate(classes, 1):
        print(f"{x} >> {clas}")
    select = int(input("Digite o número da classe desejada: "))
    if select == 1:
        print(f"Você é um ARQUEIRO, {name}")
        Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": 100,
        "Exp": 0,
        "Danobase": 30 * level,
        "Danomedio": 40 * level,
        "Danoespecial": 90 * level,
        "Stamina": 80,
        "StaminaMax": 80,
        "HpMax": 280,
        "Hp": 280,
        "Inventário": inventario,
        "Moedas": 0
    }
    elif select == 2:
        print(f"Você é um CAVALEIRO, {name}")
        Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": level * 100,
        "Exp": 0,
        "Danobase": 45 * level,
        "Danomedio": 60 * level,
        "Danoespecial": 75 * level,
        "Stamina": 120,
        "StaminaMax": 120,
        "HpMax": 320,
        "Hp": 320,
        "Inventário": inventario,
        "Moedas": 0
    }
    elif select == 3:
        print(f"Você é um ANÃO, {name}")
        Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": level * 100,
        "Exp": 0,
        "Danobase": 50 * level,
        "Danomedio": 55 * level,
        "Danoespecial": 60 * level,
        "Stamina": 70,
        "StaminaMax": 70,
        "HpMax": 300,
        "Hp": 300,
        "Inventário": inventario,
        "Moedas": 0
    }
    elif select == 4:
        print(f"Você é um MAGO, {name}")
        Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": level * 100,
        "Exp": 0,
        "Danobase": 60 * level,
        "Danomedio": 70 * level,
        "Danoespecial": 90 * level,
        "Stamina": 60,
        "StaminaMax": 60,
        "HpMax": 280,
        "Hp": 280,
        "Inventário": inventario,
        "Moedas": 0
    }
    elif select == 5:
        print(f"Você é um GLADIADOR, {name}")
        Player ={
        "Nome": name,
        "Level": level,
        "ExpMax": level * 100,
        "Exp": 0,
        "Danobase": 30 * level,
        "Danomedio": 45 * level,
        "Danoespecial": 65 * level,
        "Stamina": 110,
        "StaminaMax": 110,
        "HpMax": 310,
        "Hp": 310,
        "Inventário": inventario,
        "Moedas": 0
    }
    if 0 <select >5:
        print("Escolha uma classe válida...")
        criar_Player()
        """Player ={
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
        }"""
    list_player.append(Player)
    print(f"\nStatus do player: {list_player[0]}")
    
   



list_Monstro = []
def Gerar_Monstros():
    levelM = randint(10, 100)
    nomeM = random.choice(['Goblin', 'Orc', 'Serpente', 'Duende', 'Golem', 'Lobo'])
    Monstro={
        "Nome": f"{nomeM} {levelM}",
        "Level": levelM,
        "Dano": 1 * levelM,
        "Hp": 4 * levelM
    }
    list_Monstro.append(Monstro)
    """
    for y in list_Monstro:
        print(f"Nome: {y['Nome']} | Level: {y['Level']} | Dano: {y['Dano']} | Hp {y['Hp']}")
    """
def gerar_M(nummonstro):
    for z in range(nummonstro):
        Gerar_Monstros()
list_boss=[]
def gerar_boss():
    Dano = randint(30, 40)
    Boss = {
        "Nome": "Vezker",
        "Level": "???",
        "Dano": Dano * 4,
        "Hp": 600
    }
    list_boss.append(Boss)
    combate(list_boss[0], list_player[0])


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
    print(f"1 >> Golpe básico: {x['Danobase']} \n2 >> Golpe médio: {x['Danomedio']} \n3 >> Golpe especial: {x['Danoespecial']}")
    atac_sort = int(input('Digite o número do ataque escolhido: '))
    if atac_sort == 1:
        time.sleep(0.5)
        y['Hp'] -= atac[0]
        print(f"Você usou o ataque Básico: {atac[0]}")
        x['Stamina'] -= 2
        zerar_stamina(y,x)
    if atac_sort == 2:
        time.sleep(0.5)
        y['Hp'] -= atac[1]
        print(f"Você usou o ataque Médio: {atac[1]}")
        x['Stamina'] -= 5
        zerar_stamina(y,x)
    if atac_sort == 3:
        time.sleep(0.5)
        y['Hp'] -= atac[2]
        print(f"Você usou o ataque Especial: {atac[2]}")
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
        time.sleep(0.2)
        print(f"Status do Player: Hp: {x['Hp']}/{x['HpMax']}, Stamina: {x['Stamina']}/{x['StaminaMax']} | Status do Monstro: Hp: {y['Hp']}")
        print(f"\n")
        atacar_npc(y,x)
        time.sleep(0.2)
        print(f"Status do Player: Hp: {x['Hp']}/{x['HpMax']}, | Status do Monstro: Hp: {y['Hp']}")
        print(f"\n")
        Morte_vitoria(y,x)

def Reiniciar():
    time.sleep(0.5)
    reiniciar = str(input('Deseja recomeçar? \n [S]Sim \n  ou \n [N]Não: '))
    if reiniciar in ('S', 's'):
        list_player.clear()
        list_Monstro.clear()
        list_boss.clear()
        jogo()
    else:
        time.sleep(0.5)
        print("Até mais, guerreiro(a)")
        exit()
    
def Morte_vitoria(y,x):
    if y['Hp'] <= 0:
        time.sleep(0.5)
        print('Você venceu!!!')
        x['Moedas'] += y['Level'] * 10
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


def selecionar_monstro(difi, player):
    choices = {1: len(list_Monstro), 2: len(list_Monstro), 3: len(list_Monstro), 4: len(list_Monstro)}
    max_choice = choices[difi]
    time.sleep(0.5)
    print('Apareceu um monstro nas sombras...')
    time.sleep(0.5)
    monstro_choice = int(input(f"Escolha um número de 1 a {max_choice -1} e o monstro será revelado: "))
    lista_choice = [monstro_choice]
    if 0 < monstro_choice <= len(list_Monstro):
        time.sleep(0.5)
        print(f"Monstro a enfrentar: {list_Monstro[monstro_choice]}")
        combate(list_Monstro[monstro_choice], list_player[0])
        list_Monstro.pop(monstro_choice)
        if list_Monstro:
            andar(difi, player)
        else:
            print('Você derrotou todos os monstros!!!!!! LEGENDÁRIO')
            print('Prepare-se para enfrentar o Rei dos monstros... \nO implacável, VEZKER!!!')
            gerar_boss()
            escolher_dificuldade()
        #print(list_Monstro.index)
    
    else:
        print(f"Selecione um número válido entre 0 a {len(list_Monstro)}\n")
        selecionar_monstro(difi, player)
    
        



def escolher_dificuldade():
    dificuldade = ['Fácil', 'Normal', 'Difícil', 'INSANO!!']
    print(f"Escolha uma dificuldade entre: ")
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
def bau_tesouro(player, difi): #continuar essa função
    itens = random.choice(['Moedas', 'Poção de cura', 'Poção de exp', 'Monstro bau'])
    time.sleep(0.5)
    print('\nVocê encontrou um baú!!!')
    
    if itens == 'Moedas':
        Moedas = random.choice([10, 20, 30, 40, 50, 60])
        player["Moedas"] += Moedas
        #time.sleep(0.5)
        print(f"Você recebeu {Moedas} moedas.")
        print(f"Você tem {player["Moedas"]} Moedas.")
        andar(difi, player)
    if itens == 'Poção de cura':
        hp = 30
        if player["Hp"] + hp <= 300:
            player["Hp"] += hp
            time.sleep(0.5)
        print("Você encontrou uma poção de cura")
        print(f"\nSeu Hp atual: {player['Hp']}")
    if itens == 'Poção de exp':
        xp=30
        player["Exp"] += xp
        print("Você encontrou uma poção de exp")
        print(f"\nSeu Exp atual: {player['Exp']}")
        if player['Exp'] >= 100:
            player['Exp'] -= 100           
            player['Level'] += 1
            print("Parabéns! Você subiu de nível!!")
    if itens == 'Monstro bau':
        print("Tem algo estranho nesse baú...")
        selecionar_monstro(difi, player)


        

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
        print(f"Moedas: {player["Moedas"]}")
        produtos = int(input('Digite o número do produto que você deseja comprar: '))
        if produtos == 1:
            moedas = 20
            if player['Moedas'] >= moedas:
                player['Moedas'] -= moedas
                for i in range(len(player['Inventário'])):
                    for j in range(len(player['Inventário'][i])):
                        if player['Inventário'][i][j] == 'Vazio':
                            player['Inventário'][i][j] = itens[0]
                            break  
                        else:
                            continue  
                        break
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
                for i in range(len(player['Inventário'])):
                    for j in range(len(player['Inventário'][i])):
                        if player['Inventário'][i][j] == 'Vazio':
                            player['Inventário'][i][j] = itens[1]
                            break  
                        else:
                            continue  
                        break
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
                for i in range(len(player['Inventário'])):
                    for j in range(len(player['Inventário'][i])):
                        if player['Inventário'][i][j] == 'Vazio':
                            player['Inventário'][i][j] = itens[2]
                            break 
                        else:
                            continue  
                        break
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
                for i in range(len(player['Inventário'])):
                    for j in range(len(player['Inventário'][i])):
                        if player['Inventário'][i][j] == 'Vazio':
                            player['Inventário'][i][j] = itens[3]
                            break  # Stop once the first empty slot is filled
                        else:
                            continue  # Continue if no "Vazio" was found in the current row
                        break
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
                for i in range(len(player['Inventário'])):
                    for j in range(len(player['Inventário'][i])):
                        if player['Inventário'][i][j] == 'Vazio':
                            player['Inventário'][i][j] = itens[4]
                            break  # Stop once the first empty slot is filled
                        else:
                            continue  # Continue if no "Vazio" was found in the current row
                        break  # Exi
                print(f"Seu inventário: {player['Inventário']}")
                print(f"Moedas restantes: {player['Moedas']}")
                andar(difi, player)
            else:
                print('Você não tem moedas para realizar tal compra...')
                if player["Moedas"] >= 15:
                    comerciante(difi,player)
                andar(difi, player)
        else:
            print('Escolha um produto válido...')
            comerciante(difi, player)
    elif comprar in ('n', 'N', 'Não', 'não'):
        time.sleep(0.5)
        print('Você irá se arrepender disso...')
        andar(difi, player)




def direita(difi, player):
    sort_right = random.choice([lambda: selecionar_monstro(difi, player), lambda:'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player, difi), lambda: comerciante(difi, player)])
    res = sort_right()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    #sort_right() #continuar essa função
    
def esquerda(difi, player):
    sort_left = random.choice([lambda: selecionar_monstro(difi, player), lambda: 'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player,difi), lambda: comerciante(difi, player)])
    res = sort_left()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    #sort_left()
     #continuar essa função

def em_frente(difi, player):
    sort_front = random.choice([lambda: selecionar_monstro(difi, player), lambda:'Não há nada por aqui... \nProssiga!!', lambda: bau_tesouro(player, difi), lambda: comerciante(difi, player)])
    res = sort_front()
    if res == 'Não há nada por aqui... \nProssiga!!':
        time.sleep(0.5)
        print(res)
        andar(difi, player)
    #sort_front() #continuar essa função

def abrir_inventario(player, difi):
    
    #print(player['Inventário'])
    itens = ['poção de cura: 20x Moedas', 'poção de exp: 25x Moedas', 'poção de stamina: 15x Moedas', 'amuleto de vida: 60x Moedas', 'amuleto de ataque: 80x Moedas']
    opcoes = ["Equipar", "Usar", "Consumir", "Fechar Inventário"]
    for i in range(len(player['Inventário'])):
        for j in range(len(player['Inventário'][i])):
            print(f"{i+j+1}º Slot >> {player["Inventário"][i][j]}")
    usar = str(input("Deseja interagir com algum item?\n [S]Sim [N]Não \n"))
   
    if usar in ('s', 'S', 'sim', 'Sim'):
        item = int(input("Digite o número do item que você deseja interagir: "))
        if 1 <= item < len(player["Inventário"][0]):
            itemS = player["Inventário"][0][item -1]
            if itemS in itens:
                if itemS == itens[0]:
                    hp = 40
                    if player['Hp'] + hp <= player['HpMax']:
                        player['Hp'] += hp
                    print(f"Hp atual: {player['Hp']}/{player['HpMax']}")
                    player["Inventário"][0][item -1] = 'Vazio'
                    andar(difi, player)
                if itemS == itens[1]:
                    exp = 40
                    if player['Exp'] + exp <= player['ExpMax']:
                        player['Exp'] += exp
                    print(f"Exp atual: {player['Exp']}/{player['ExpMax']}")
                    player["Inventário"][0][item -1] = 'Vazio'
                    andar(difi, player)
                if itemS == itens[2]:
                    stamina = 40
                    if player['Stamina'] + stamina <= player['StaminaMax']:
                        player['Stamina'] += stamina
                    print(f"Stamina atual: {player['Stamina']}/{player['StaminaMax']}")
                    player["Inventário"][0][item -1] = 'Vazio'
                    andar(difi, player)
                if itemS == itens[3]:
                    hpmax = 40
                    hp = 20
                    player["HpMax"] += hpmax
                    if player["Hp"] + hp <= player["HpMax"]:
                        player["Hp"] += hp
                    print(f"Hp atual: {player['Hp']}/{player['HpMax']}")
                    player["Inventário"][0][item -1] = 'Vazio'
                    andar(difi, player)
                if itemS == itens[4]:
                    dano = 40
                    player["Danobase"] += dano
                    player["Danomedio"] += dano
                    player["Danoespecial"] += dano
                    print(f"Dano Base: {player["Danobase"]} \nDano Médio: {player["Danomedio"]} \nDano Especial: {player["Danoespecial"]}")
                    player["Inventário"][0][item -1] = 'Vazio'
                    andar(difi, player)
                
            else:
                    print("Não há nenhum item utilizável...")
                    andar(difi, player)
        else:
            print("Opção inválida...")
            abrir_inventario(player, difi)
    elif usar in ('n', 'N', 'Não', 'nao', 'não', 'Nao'):
        andar(difi, player)

    """
    print("Opções: ")
    for num, x in enumerate(opcoes, 1):
        print(f"{num}>> {x}")
    
   

"""

#Continuar daqui


def andar(difi, player): #continuar essa função
    opcoes = ['Ir para DIREITA', 'Ir para ESQUERDA', 'Ir em FRENTE', 'Abrir INVENTÁRIO', 'Status do PLAYER']
    for num, step in enumerate(opcoes, 1):
        time.sleep(0.5)
        print(f"\n{num}>> {step}")
        time.sleep(0.5) 
    op = int(input('\nDigite o número da opção escolhida: '))
    if op == 1:
        direita(difi, player)
        andar(difi, player)
    if op == 2:
        esquerda(difi, player)
        andar(difi, player)
    if op == 3:
        em_frente(difi, player)
        andar(difi, player)
    if op == 4:
        abrir_inventario(player, difi)
        andar(difi,player)
    if op == 5:
        print(list_player[0])
        andar(difi,player)
    else:
        time.sleep(0.5)
        print('Escolha uma opção válida')
        andar(difi, player)
    

        
def jogo():
    pyg.mixer.init()
    pyg.mixer.music.load("medieval.mp3")
    pyg.mixer.music.set_volume(0.22)
    pyg.mixer.music.play()
    criar_Player()
    player = list_player[0]
    dific = escolher_dificuldade()
    print('\nVocê, um guerreiro recém-treinado e ansioso para provar seu valor, foi convocado pelo Conselho dos Anciões para defender o reino e investigar a origem desse mal.\nArmado com coragem e determinação, você sabe que essa é sua chance de se tornar uma lenda — ou desaparecer nas sombras...\n\nPrepare-se para uma jornada de mistérios e batalhas. O destino de Arvendale está em suas mãos.')
    andar(dific, player)
    
jogo()


