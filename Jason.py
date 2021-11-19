import time
import sys

# Tela principal - OK

def main():
    print('                          Fuja do Jason              ')
    print("              ===========================================")
    time.sleep(1)
    print_slow(' Neste jogo você é um jovem que vai trabalhar no acampamento Crystal Lake em'
          '\n suas férias da faculdade, mas o que não sabe ainda, é que neste acampamento '
          '\n          reside o mais puro mal, um espírito vingativo...\n\n ')
    time.sleep(1)
    print('         Será que você consegue sobreviver a uma noite ?\n')
    time.sleep(2)

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
    time.sleep(1)
    print('         https://www.youtube.com/watch?v=NAFEiBzMXxc')
    print('            Trilha sonora obrigatória no game !')
    time.sleep(1)
    texto_lento = '       Quando quiser começar, digite a palavra jogar:'
    print_slow('       Quando quiser começar, digite a palavra jogar:')
    comeco = (input('')).casefold()
    while comeco == 'jogar':
        selecao_personagem()
    else:
        print('Até logo então :)')

# Funções de temporizador de letras - OK

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00000001)

def input_slow(str):
    for letter in str:
        sys.stdin.write(letter)
        sys.stdin.flush()
        time.sleep(0.00000001)

# Seleção de personagens - OK

def selecao_personagem():
    print_slow("Selecione seu personagem:\n 1 - Marcie\n 2 - Jack\n 3 - Annie \nDigite 1, 2 ou 3:")
    user_in = int(input(''))
    if user_in == 1:
        print_slow('Você escolheu a Marcie.\n')
        time.sleep(1)
        game1()
    elif user_in == 2:
        print_slow('Você escolheu o Jack.\n')
        time.sleep(1)
        game2()
    elif user_in == 3:
        print_slow('Você escolheu a Annie.\n')
        time.sleep(1)
        game3()
    else:
        print_slow("Digite uma opção válida !")
        selecao_personagem()

# Possibilidades de morte - OK

def jogador_morreu():
    print('======================================================================')
    print_slow("Jason acabou pegando você, que fim horrível, você está morto!.\n")
    print_slow("Game Over!\n\nDigite N para jogar denovo! :")
    resposta = (input("")).upper().lower()
    if resposta == 'n':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")
        quit()

def jogador_morreu_facao():
    print('======================================================================')
    print_slow("Jason estava armado com seu clássico facão, e cortou a sua mão no processo, você acabou sangrando até a morte !\n")
    print_slow("Game Over!\n\nDigite N para jogar denovo! :")
    resposta = (input("")).upper().lower()
    if resposta == 'n':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")
        quit()

def jogador_morreu_pe():
    print('======================================================================')
    print('Você consegue se rastejar, mas Jason consegue correr, é fácil pra ele te pegar. Você virou exemplo para outros monitores inocentes\n Você está morto!')
    print_slow("Game Over!\n\nDigite N para jogar denovo! :")
    resposta = (input("")).upper().lower()
    if resposta == 'n':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")
        quit()

def jogador_morre_machado():
    print('======================================================================')
    print('Jason está com o machado na mão, e com um só golpe parte sua cabeça em duas partes.\n Fim da linha pra você!')
    print_slow("Game Over!\n\nDigite N para jogar denovo! :")
    resposta = (input("")).upper().lower()
    if resposta == 'n':
        selecao_personagem()
    else:
        print("Então tá, até a próxima.")
        quit()

# Jogo da Marcie - OK !

def game1():
    print('======================================================================')
    print_slow("Você está trabalhando como monitor, está de noite...\n")
    print_slow("Nota-se um movimento estranho na floresta ao seu lado.\n")
    print_slow("                O que você faz ?\n")
    print_slow("A - Verifica os arbustos\nB - Ignore e entra em sua cabana \n")
    print_slow("Digite A ou B:")
    resposta = input('').upper()
    if resposta == 'A':
        print("Infelizmente Jason estava te esperando atrás da árvore.")
        jogador_morreu()
    elif resposta == 'B':
        print_slow("Você entra em sua cabana com segurança.\n")
        jogador_cabana_marcie()
    else:
        print("Por favor, digite uma opção válida !")
        game1()

def jogador_cabana_marcie():
    print('======================================================================')
    print_slow("Você entra na cabana, mas sente que tem alguém te observando pela janela...\no que você faz ?\nA - Verifica a Janela\nB - Tenta se esconder e esquecer do problema \nDigite A ou B:")
    resposta = input('').upper()
    if resposta == 'A':
        print_slow("Infelizmente Jason estava te observando e decide te atacar, quebrando a janela e agarrando seu pescoço.\n")
        jogador_morreu()
    elif resposta == 'B':
        print_slow("Você sente que aquela presença acabou sumindo, e você ouve batidas em sua porta.\n")
        jogador_verifica_porta_marcie()
    else:
        print("Digite uma opção válida!")
        jogador_cabana_marcie()

def jogador_verifica_porta_marcie():
    print('======================================================================')
    print_slow("Após ouvir as batidas na porta, o que você fará?\nA - Abro a porta.\nB - Pergunto quem está batendo\nC - Saio pelos fundos correndo.\nDigite A, B ou C:")
    resposta = input('').upper()
    if resposta == 'A':
        print_slow("Nunca assistiu filme de terror ?")
        jogador_morreu()
    elif resposta == 'B':
        print_slow("Você ouve batidas mais fortes, até que uma delas quebra a porta e Jason entra na cabana com tudo!\n")
        jogador_corre_jason_marcie()
    elif resposta == 'C':
        print_slow("No momento em que você corre, Jason quebra a porta, agora ele corre atrás de você!\n")
        jogador_corre_jason_marcie()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_verifica_porta_marcie()

def jogador_corre_jason_marcie():
    print('======================================================================')
    print_slow("Você está correndo de Jason e vê um machado na parede dos fundos, você para pra pegar ele ?\nA - Sim\nB - Não\nDigite A ou B:")
    resposta = input('').upper()
    if resposta == 'A':
        print_slow("Você foi lento demais para pegar o machado, e Jason está na sua cola agora\n")
        jogador_morreu()
    elif resposta == 'B':
        print_slow("Boa escolha, agora você está correndo direto para a saída do acampamento\n")
        jogador_foge()
    else:
        print('Por favor, digite uma opção válida!')
        jogador_corre_jason_marcie()

def jogador_foge():
    print('======================================================================')
    print_slow("Parabéns! Você conseguiu escapar do assassino com sucesso, deseja jogar denovo ?(sim/nao)")
    resposta = input("").upper().lower()
    if resposta == 'sim':
        selecao_personagem()
    else:
        print("Obrigado por jogar !")
        quit()

# Jogo do Jack - OK

def game2():
    print('======================================================================')
    print_slow("Você está aproveitando o fim de expediente com seus colegas no cais,próximo ao lago,\nquando você precisa ir ao banheiro, assim que chega lá, você sente uma presença estranha, como se\nfosse alguém te observando, o que você faz ?\n A - Ignora os barulhos e a presença e volta pra confraternização\n B - Adentra na floresta pra procurar a origem do barulho \nDigite A ou B:")
    resposta = input("").upper()
    if resposta == 'A':
        print_slow("Ótima escolha, você volta pro grupo de amigos e continua a comemorar como se nada tivesse acontecido.\n")
        voltou_amigos_jack()
    elif resposta == 'B':
        print_slow("Voce entra mais fundo na floresta para procurar a origem do som\n")
        entrou_floresta_jack()
    else:
        print_slow("Por favor, digite uma opção válida !")
        game2()

def entrou_floresta_jack():
    print('======================================================================')
    print_slow('Pelo visto você nunca viu filmes de terror, pode pagar o preço com sua vida,\npois Jason estava na floresta em cima de uma árvore, e pulou em você.')
    jogador_morreu()

def voltou_amigos_jack():
    print('======================================================================')
    print_slow('Você chega são e salvo ao cais, mas com o passar das horas você acaba ficando\nbêbado e desorientado, e ao fim de noite decide ir para sua cabana,\ndurante o caminho, nota alguém te seguindo, uma figura mascarada, o que você faz ?\nA - Já olha pro lado e pega a primeira coisa que vê pra se defender\nB - Se vira e grita qualquer coisa pra espantar a figura\nDigite A ou B:')
    resposta = input("").upper()
    if resposta == 'A':
        print_slow('Você achou um taco de baseball que estava encostado em um dos barcos do acampamento !\n')
        jogador_taco_jack()
    if resposta == 'B':
        print_slow(
            'Faz sentido, afinal você está bêbado e não sabe aonde suas ações vão te\nlevar, mas nesse caso quando vira pra frente, Jason está de pé ali.\n')
        jogador_morreu()
    else:
        print("Por favor, digite uma opção válida !")
        voltou_amigos_jack()

def jogador_taco_jack():
    print('======================================================================')
    print_slow("Após pegar o taco de baseball, você está precavido, pois você percebe que Jason saiu da\nmata ao seu lado e veio correndo em sua direção, o que você faz ?\nA - Tenta acertar ele com o taco\nB - Decido correr para frente, em direção a cabana\nDigite A ou B: ")
    resposta = input("").upper()
    if resposta == 'A':
        print_slow('Infelizmente você deveria saber que ele é forte, a batida não tem efeito e ele agora está na sua cola.\n')
        jogador_morreu_facao()
    elif resposta == 'B':
        print_slow('Você acaba sendo mais rápido que ele e entrando em sua cabana.\n')
        jogador_entra_jack()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_taco_jack()

def jogador_entra_jack():
    print('======================================================================')
    print_slow('Você entra em sua cabana, e percebe que Jason quebrou a janela do seu lado,\nvocê avista um pé de cabra encostado na parede, o que você faz ?\nA - Larga o taco e pega o pé de cabra para se defender\nB - Tenta bater no Jason com o taco.\nDigite A ou B: ')
    resposta = input('').upper()
    if resposta == 'A':
        print_slow('Boa escolha, você pega o pé de cabra e aguarda ele entrar na cabana pela janela, e em um golpe você o acerta\nbem na cabeça, quebrando sua máscara e o fazendo cambalear para trás, e isso te dá tempo de correr\npara a saída do acampamento.\n')
        jogador_foge()
    elif resposta == 'B':
        print_slow('O taco estava desgastado e velho, e quebra na mais fraca batida, já sabe o que acontece agora né ?\n')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_entra_jack()

# Jogo da Annie - OK

def game3():
    print('======================================================================')
    print_slow('Você foi a última dos monitores ao entrar no trabalho, e percebe que o ambiente possui um aspecto estranho, nunca antes\nvisto, apesar de já ter visto filmes de terror, decide por ignorar esse fato.\nEsta noite você está descansando após um longo expediente vigiando as crianças do acampamento, quando\ndo nada, o corpo de seu amigo Jack é lançado pela sua janela, sem um dos pés.\nVocê fica aterrorizada e vê que logo em seguida, uma figura mascarada entra pela janela quebrada, e começa\na te perseguir.\nNota-se que exite uma escada dentro do chalé, o que você faz ?\nA - Tenta subir a escada pra escapar do mal iminente\nB - Acaba optando por procurar outra saída dentro do chalé.\nDigite A ou B: ')
    resposta = input('').upper()
    if resposta == 'A':
        print_slow('Agora você sobe as escadas, talvez você encontre algo na parte de cima que te ajude nessa fuga.\n')
        jogador_escada_annie()
    elif resposta == 'B':
        print_slow('Você nota que o chalé só tem uma porta, e Jason está no caminho, não restando outra saída além da morte.\n')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        game3()

def jogador_escada_annie():
    print('======================================================================')
    print_slow('Você nota que na parte de cima do chalé, bem próximo a sacada, existe uma estante cheia de livros, você no desespero faz a estante tombar,\nos livros pesados que caem fazem Jason ficar desnorteado por alguns segundos, te dando uma brecha para escapar.\nAo fundo do corredor do segundo andar, você nota que existe uma porta que dá para o armário de vassouras, e ao seu lado,\numa janela para sair do chalé. O que você faz ?\nA - Decide que é melhor pular a janela para tentar escapar\nB - Corre para se esconder dentro do armário de vassouras.\nDigite A ou B:')
    resposta = input('').upper()
    if resposta == 'A':
        print_slow('Pular da janela do segundo andar de um chalé não parece uma má ideia, porém assim que você pula, pode ouvir um estalo no seu\ncalcanhar e fêmur, você acaba de torcer seu tornozelo e está sentindo muita dor, não conseguindo andar direito.\n')
        jogador_morreu_pe()
    elif resposta == 'B':
        print_slow('Você consegue ir até o fim do corredor e se esconder dentro do armário com sucesso.\n')
        jogador_armario_annie()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_escada_annie()

def jogador_armario_annie():
    print('======================================================================')
    print_slow('Após se esconder dentro do armário, você começa a escutar passos pesados que vem da escada por onde você subiu, e dentro\ndo armário, percebe que tem algumas roupas e tecidos pendurados, mas nota que existe um volume estranho atrás deles, o que você faz ?\nA - Verifica o que existe atrás dos tecidos.\nB - Decide por ignorar tudo a sua volta e esperar o pior passar.\nDigite A ou B: ')
    resposta = input('').upper()
    if resposta == 'A':
        print_slow('Ao remexer nos tecidos, o corpo de sua amiga Marcie cai no seu colo, com a cabeça dilacerada e uma faca cravada nas costas.\n')
        jogador_corpo_annie()
    elif resposta == 'B':
        print_slow('Ignorar nesses casos não é uma boa escolha, Jason acaba quebrando a porta com machadadas e pegando você pelo pescoço, é o fim.\n')
        jogador_morreu_facao()
    else:
        print("Por favor, digite uma opção válida !")
        jogador_armario_annie()

def jogador_corpo_annie():
    print('======================================================================')
    print_slow('Após o corpo cair no seu colo, Jason bate com tudo na porta do closet, e ao perceber que estava fechada, começa a quebrar ela como machado.\nO que você faz?\nA - Decide pegar a faca das costas do corpo para se defender.\nB - Apenas entra em pânico, pois não existe outra saída.\nDigite A ou B: ')
    resposta = input('').upper()
    if resposta == 'A':
        print_slow('Você retira a faca do cadáver, com um pouco de nojo, e assim que Jason consegue entrar, você crava a faca em sua perna e corre para a porta.\nEventualmente você corre pela floresta até chegar a saída do acampamento.\n')
        jogador_foge()
    elif resposta == 'B':
        print_slow('Porque ao menos não tentar lutar pra sobreviver ? Está na cara que ele vai te matar, e é o que acontece.\n')
        jogador_morre_machado()

main()