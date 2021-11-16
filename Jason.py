import time
import random

# Tela principal

def main():
    print('                          Fuja do Jason              ')
    print("              ===========================================")
    time.sleep(1)
    print(' Nest jogo você é um jovem que vai trabalhar no acampamento Crystal Lake em'
          '\n suas férias da faculdade, mas o que não sabe ainda, é que neste acampamento '
          '\n          reside o mais puro mal, um espírito vingativo...')
    time.sleep(1)
    print('          Será que você consegue sobreviver a uma noite ?\n\n')
    time.sleep(1)

    jason_head = ['                           ██████████████            ',
                  '                       ████              ████        ',
                  '                     ██    ██          ██    ██      ',
                  '                   ██                          ██    ',
                  '                   ██      ██          ██      ██    ',
                  '                 ██  ██                      ██  ██  ',
                  '                 ██  ██                      ██  ██  ',
                  '                 ██  ██                      ██  ██  ',
                  '                 ██        ██          ██        ██  ',
                  '                 ██  ██        ██  ██        ██  ██  ',
                  '               ██          ▒▒▒▒      ▒▒▒▒          ██',
                  '               ██              ▒▒▒▒▒▒              ██',
                  '               ██      ████████  ▒▒  ████████      ██',
                  '               ██      ████████      ████████      ██',
                  '                 ██                              ██  ',
                  '                 ██                              ██  ',
                  '                   ██      ▒▒          ▒▒      ██    ',
                  '                   ██    ▒▒    ██  ██    ▒▒    ██    ',
                  '                     ██▒▒  ██          ██  ▒▒██      ',
                  '                     ██        ██  ██        ██      ',
                  '                       ██                  ██        ',
                  '                         ██    ██  ██    ██          ',
                  '                           ██          ██            ',
                  '                             ██████████              ']

    for jason_head_part in jason_head:
        print(jason_head_part)

    print('\n\nInstruções: Digite as opções mostradas quando solicitado.\n')
    print('         https://www.youtube.com/watch?v=NAFEiBzMXxc')
    print('            Trilha sonora obrigatória no game !')
    comeco = (input('Quando quiser começar, digite a palavra jogar:')).casefold()
    while comeco == 'jogar':
        selecao_personagem()
    else:
        print('Até logo então :)')

# Seleção de personagens

def selecao_personagem():
    user_in = int(input("Selecione seu personagem:\n 1 - Marcie\n 2 - Jack\n 3 - Annie \nDigite 1, 2 ou 3:"))
    if user_in == 1:
        print('Você escolheu a Marcie.')
        game1()
    elif user_in == 2:
        print('Você escolheu o Jack.')
        game2()
    elif user_in == 3:
        print('Você escolheu a Annie.')
        game3()
    else:
        print("Digite uma opção válida !")
        selecao_personagem()

# Possibilidades de morte

def jogador_morreu():
    print('======================================================================')
    print("Jason acabou pegando você, que fim horrível, você está morto!.")
    resposta = (input("Game Over!\n\nDigite N para jogar denovo! :")).upper()
    while resposta == 'N':
        main()
    else:
        print("Então tá, até a próxima.")

def jogador_morreu_facao():
    print('======================================================================')
    print("Jason estava armado com seu clássico facão, e cortou a sua mão no processo, você acabou sangrando\naté a morte !")
    resposta = (input("Game Over!\n\nDigite N para jogar denovo! :")).upper()
    while resposta == 'N':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")

def jogador_morreu_pe():
    print('======================================================================')
    print('Você consegue se rastejar, mas Jason consegue correr, é fácil pra ele te pegar. Você virou exemplo para outros monitores inocentes\n Você está morto!')
    resposta = (input("Game Over!\n\nDigite N para jogar denovo! :")).upper()
    while resposta == 'N':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")

def jogador_morre_machado():
    print('======================================================================')
    print('Jason está com o machado na mão, e com um só golpe parte sua cabeça em duas partes.\n Fim da linha pra você!')
    resposta = input("Game Over!\n\nDigite N para jogar denovo! :").upper()
    while resposta == 'N':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")

# Jogo da Marcie

def game1():
    print('======================================================================')
    resposta = input("Você está trabalhando como monitor, está de noite e você"
                     "\navista um movimento estranho na floresta ao seu lado,"
                     "\no que você faz ?\n A - Verifica os arbustos\n B - Ignore e entra em sua cabana \nDigite A ou B:").upper()
    if resposta == 'A':
        print("Infelizmente Jason estava te esperando atrás da árvore.")
        jogador_morreu()
    elif resposta == 'B':
        print("Você entra em sua cabana com segurança.")
        jogador_cabana_marcie()
    else:
        print("Por favor, digite uma opção válida !")
        game1()

def jogador_cabana_marcie():
    print('======================================================================')
    resposta = input("Você entra na cabana, mas sente que tem alguém te observando pela janela,"
                     "\no que você faz ?\n A - Verifica a Janela\n B - Tenta se esconder e esquecer do problema \nDigite A ou B:").upper()
    if resposta == 'A':
        print("Infelizmente Jason estava te observando e decide te atacar, quebrando a janela e agarrando seu pescoço.")
        jogador_morreu()
    elif resposta == 'B':
        print("Você sente que aquela presença acabou sumindo, e você ouve batidas em sua porta")
        jogador_verifica_porta_marcie()
    else:
        print("Digite uma opção válida!")
        jogador_cabana_marcie()

def jogador_verifica_porta_marcie():
    print('======================================================================')
    resposta = input("Após ouvir as batidas na porta, o que você fará? \nA - Abro a porta. \nB - Pergunto quem está"
                     " batendo \nC - Saio pelos fundos correndo. \nDigite A ou B:").upper()
    if resposta == 'A':
        print("Nunca assistiu filme de terror ?")
        jogador_morreu()
    elif resposta == 'B':
        print("Você ouve batidas mais fortes, até que uma delas quebra a porta e Jason entra na cabana com tudo.")
        jogador_corre_jason_marcie()
    elif resposta == 'C':
        print("No momento em que você corre, Jason quebra a porta, agora ele corre atrás de você !")
        jogador_corre_jason_marcie()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_verifica_porta_marcie()

def jogador_corre_jason_marcie():
    print('======================================================================')
    resposta = input("Você está correndo de Jason e vê um machado na parede dos fundos, você para pra pegar ele ? "
                     "\nA - Sim \nB - Não \nDigite A ou B:").upper()
    if resposta == 'A':
        print("Você foi lento demais para pegar o machado, e Jason está na sua cola agora :(")
        jogador_morreu()
    elif resposta == 'B':
        print("Boa escolha, agora você está correndo direto para a saída do acampamento")
        jogador_foge()
    else:
        print('Por favor, digite uma opção válida!')
        jogador_corre_jason_marcie()

def jogador_foge():
    print('======================================================================')
    resposta = input("Parabéns! Você conseguiu escapar do assassino com sucesso, deseja jogar denovo ?(sim/nao)").upper()
    while resposta == 'sim':
        main()
    else:
        print("Obrigado por jogar !")

# Jogo do Jack

def game2():
    print('======================================================================')
    resposta = input("Você está aproveitando o fim de expediente com seus colegas no cais,próximo ao lago,\nquando você precisa ir ao banheiro, assim que chega lá, você sente uma presença estranha, como se\nfosse alguém te observando, o que você faz ?\n A - Ignora os barulhos e a presença e volta pra confraternização\n B - Adentra na floresta pra procurar a origem do barulho \nDigite A ou B:").upper()
    if resposta == 'A':
        print("Ótima escolha, você volta pro grupo de amigos e continua a comemorar como se nada tivesse acontecido.")
        voltou_amigos_jack()
    elif resposta == 'B':
        print("Voce entra mais fundo na floresta para procurar a origem do som")
        entrou_floresta_jack()
    else:
        print("Por favor, digite uma opção válida !")
        game2()

def entrou_floresta_jack():
    print('======================================================================')
    print('Pelo visto você nunca viu filmes de terror, pode pagar o preço com sua vida,\npois Jason estava na floresta em cima de uma árvore, e pulou em você.')
    jogador_morreu()

def voltou_amigos_jack():
    print('======================================================================')
    resposta = input('Você chega são e salvo ao cais, mas com o passar das horas você acaba ficando\nbêbado e desorientado, e ao fim de noite decide ir para sua cabana,\ndurante o caminho, nota alguém te seguindo, uma figura mascarada, o que você faz ?\n A - Já olha pro lado e pega a primeira coisa que vê pra se defender\n B - Se vira e grita qualquer coisa pra espantar a figura\n Digite A ou B:').upper()
    if resposta == 'A':
        print('Você achou um taco de baseball que estava encostado em um dos barcos do acampamento !')
        jogador_taco_jack()
    if resposta == 'B':
        print(
            'Faz sentido, afinal você está bêbado e não sabe aonde suas ações vão te \nlevar, mas nesse caso quando vira pra frente, Jason está de pé ali.')
        jogador_morreu()
    else:
        print("Por favor, digite uma opção válida !")
        voltou_amigos_jack()

def jogador_taco_jack():
    print('======================================================================')
    resposta = input('Após pegar o taco de baseball, você está precavido, pois você percebe que Jason saiu da\n mata ao seu lado e veio correndo em sua direção, o que você faz ?\n A - Tenta acertar ele com o taco\n B - Eu corro para frente, em direção a cabana\n Digite A ou B: ').upper()
    if resposta == 'A':
        print('Infelizmente você deveria saber que ele é forte, a batida não tem efeito e ele agora está na sua cola')
        jogador_morreu_facao()
    elif resposta == 'B':
        print('Você acaba sendo mais rápido que ele e entrando em sua cabana.')
        jogador_entra_jack()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_taco_jack()

def jogador_entra_jack():
    print('======================================================================')
    resposta = input(
        'Você entra em sua cabana, e percebe que Jason quebrou a janela do seu\nlado, você avista um pé de cabra encostado na parede, o que você faz ?\n A - Larga o taco e pega o pé de cabra para se defender\n B - Tenta bater no Jason com o taco.\n Digite A ou B: ').upper()
    if resposta == 'A':
        print(
            'Boa escolha, você pega o pé de cabra e aguarda ele entrar na cabana pela janela, e em um golpe você o acerta\nbem na cabeça, quebrando sua máscara e o fazendo cambalear para trás, e isso te dá tempo de correr\npara a saída do acampamento.')
        jogador_foge()
    elif resposta == 'B':
        print('O taco estava desgastado e velho, e quebra na mais fraca batida, já sabe o que acontece agora né ?')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_entra_jack()

# Jogo da Annie

def game3():
    print('======================================================================')
    resposta = input(
        'Você foi a última dos monitores ao entrar no trabalho, e percebe que o ambiente possui um aspecto estranho, nunca antes\n visto, apesar de já ter visto filmes de terror, decide por ignorar esse fato.\n  Esta noite você está descansando após um longo expediente vigiando as crianças do acampamento, quando\n do nada, o corpo de seu amigo Jack é lançado pela sua janela, sem um dos pés.\n Você fica aterrorizada e vê que logo em seguida, uma figura mascarada entra pela janela quebrada, e começa\n a te perseguir.\n Nota-se que exite uma escada dentro do chalé, o que você faz ?\n A - Tenta subir a escada pra escapar do mal iminente\n B - Acaba optando por procurar outra saída dentro do chalé.\n Digite A ou B: ').upper()
    if resposta == 'A':
        print('Agora você sobe as escadas, talvez você encontre algo na parte de cima que te ajude nessa fuga.')
        jogador_escada_annie()
    elif resposta == 'B':
        print(
            'Você nota que o chalé só tem uma porta, e Jason está no caminho, não restando outra saída além da morte.')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        game3()

def jogador_escada_annie():
    print('======================================================================')
    resposta = input(
        'Você nota que na parte de cima do chalé, bem próximo a sacada, existe uma estante cheia de livros, você no desespero faz a estante tombar,\n e os livros pesados que caem fazem Jason ficar desnorteado por alguns segundos, te dando uma brecha para escapar.\n Ao fundo do corredor do segundo andar, você nota que existe uma porta que dá para o armário de vassouras, e ao seu lado,\n uma janela para sair do chalé. O que você faz ?\n A - Decide que é melhor pular a janela para tentar escapar\n B - Corre para se esconder dentro do armário de vassouras.\n Digite A ou B:').upper()
    if resposta == 'A':
        print(
            'Pular da janela do segundo andar de um chalé não parece uma má ideia, porém assim que você pula, pode ouvir um estalo no seu\n calcanhar e fêmur, você acaba de torcer seu tornozelo e está sentindo muita dor, não conseguindo andar direito.')
        jogador_morreu_pe()
    elif resposta == 'B':
        print('Você consegue ir até o fim do corredor e se esconder dentro do armário com sucesso.')
        jogador_armario_annie()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_escada_annie()

def jogador_armario_annie():
    print('======================================================================')
    resposta = input(
        'Após se esconder dentro do armário, você começa a escutar passos pesados que vem da escada por onde você subiu, e dentro\n do armário, percebe que tem algumas roupas e tecidos pendurados, mas nota que existe um volume estranho atrás deles, o que você faz ?\n A - Verifica o que existe atrás dos tecidos.\n B - Decide por ignorar tudo a sua volta e esperar o pior passar.\n Digite A ou B: ').upper()
    if resposta == 'A':
        print(
            'Ao remexer nos tecidos, o corpo de sua amiga Marcie cai no seu colo, com a cabeça dilacerada e uma faca cravada nas costas.')
        jogador_corpo_annie()
    elif resposta == 'B':
        print(
            'Ignorar nesses casos não é uma boa escolha, Jason acaba quebrando a porta com machadadas e pegando você pelo pescoço, é o fim.')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_armario_annie()

def jogador_corpo_annie():
    print('======================================================================')
    resposta = input(
        'Após o corpo cair no seu colo, Jason bate com tudo na porta do closet, e ao perceber que estava fechada, começa a quebrar ela com\n o machado, o que você faz?\n A - Decide pegar a faca das costas do corpo para se defender.\n B - Apenas entra em pânico, pois não existe outra saída.\n Digite A ou B: ').upper()
    if resposta == 'A':
        print(
            'Você retira a faca do cadáver, com um pouco de nojo, e assim que Jason consegue entrar, você crava a faca em sua perna e corre para a porta.\n Eventualmente você corre pela floresta até chegar a saída do acampamento.')
        jogador_foge()
    elif resposta == 'B':
        print('Porque ao menos não tentar lutar pra sobreviver ? Está na cara que ele vai te matar, e é o que acontece')
        jogador_morre_machado()

main()