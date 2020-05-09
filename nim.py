def computador_escolhe_jogada(n,m):
    pc_remove = 1
    while pc_remove != m:
        if(n - pc_remove) % (m+1) == 0:
            return pc_remove
        else:
            pc_remove +=1
    return pc_remove

def usuario_escolhe_jogada(n,m):
    jogada_user = False
    while not jogada_user:
        remove_user = int(input("Quantas peças você vai tirar?"))
        if remove_user > n or remove_user > m or remove_user <= 0:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            jogada_user = True
    return remove_user

def campeonato():
    rodadas_camp = 1
    win_user = 0 ; win_pc = 0
    while rodadas_camp <= 3:
        print()
        print("**** Rodada {} ****" .format(rodadas_camp))
        print()
        if partida() == "pc_win":
            win_pc +=1 #soma 1 ponto para o computador
        elif partida() == "user_win":
            win_user +=1 #soma 1 ponto para o computador
        rodadas_camp +=1
    print()
    print("**** Final do campeonato! ****")
    print("Placar: Você {} X {} Computador" .format(win_user,win_pc))

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    inicio_user = False
    if n % (m+1) == 0:
        print()
        print("Você começa!")
        inicio_user = True
    else:
        print()
        print("Computador começa!")

    while n > 0:
        if inicio_user:
            remove_user = usuario_escolhe_jogada(n,m)
            n = n-remove_user
            if remove_user == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou {} peças" .format(remove_user))
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n !=0 and n !=1:
                print("Agora restam apenas {} peça no tabuleiro.".format(n))
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return "user_win" #ponto do usuario
            inicio_user = False
 
        else:
            remove_pc = computador_escolhe_jogada(n,m)
            n = n-remove_pc
            if remove_pc == 1:
                print()
                print("O computador tirou uma peça.")
            else:
                print()
                print("O computador tirou {} peças" .format(remove_pc))            
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n !=0 and n !=1:
                print("Agora restam apenas {} peça no tabuleiro.".format(n))
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return "pc_win"     #ponto do computador     
            inicio_user = True

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    start_game = int(input("2 - para jogar um campeonato "))
    if start_game == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        print("Você escolheu um campeonato!")
        campeonato()

main()
