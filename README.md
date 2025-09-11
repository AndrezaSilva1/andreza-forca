Projeto: Jogo Forca
Tecnologia: python 3 Descrição : Interação do jogo da forca com interação no terminal. O jogo permite que usuário adicionar palavras completas com interação, controla letras ja tentadas, gerenciamento de forca eficiente, e conforme erros desenhar a forca

Objetivo : Criar um jogo desenvolvido que trabalher com a programação, possibilitando uma interação.

Principais e Mecânicas
O jogador deve digitar três palavras ou terminar com “s”

O jogador acrescentar palavras a lista

Seção aletoria
O sistema apos cada partida,casual seleciona a palavra

O que garante a variedade na partida

Representação da palavra ser adivinhada

A palavra secreta e representada cada letra por _ , conforme o jogador acertar vai substituindo _ por letras.

Gerenciamento das tentativas e letras ja usadas

O jogador tem oito tentativas erradas, representa por parte do desenho do jogo da forca

A cada erro, uma parte do boneco e desenhada na interface.

Sistema Interação e Feedback
A representação do jogo da forca, e desenhado aos tempo

Lembrete para palavras já anexadas

Terminal exibir nitidamente

Mudanças do jogo e restantes de tentativas

Vitória ou derrota
O jogador ganha a vitoria quando os tracinhos acabam e a palavra e adivinhadas

O jogador pedir quando o numero de oito tentativas e atingido, assim desenhando o jogo da forca

Estrutura interna do código:

Inicialização e entradas de dados - A
Lista com palavras pré definidas, mais palavras adicionais

Válida ser a palavra tem mais de quatro letras

Permite o uso do “s” após três tentativas .

Exibir a lista final de palavras

Seleção aleatória - B
randint da biblioteca random para escolher o índice da palavra correta

Preparação de Máscaras e variáveis de controle - C
criar uma lista tentativa_ para cada letra já tentada Inicializa variáveis: Forca para contar erros

acertos para contar letras descobertas

letrasTentadas para armazenar letras ja tentadas

Loop principal do jogo- D
limpa a tela Exibir o desenho da forca conforme as letras erradas

Exibir a palavra mascarada, a quantidade de letras e forca

Checar ser a vitória ou derrota apresenta mensagem apropriada

Solicitar uma letra ao jogador, conferir ser a letra ja foi tentada

Atualiza máscara e contadores conforme o erro ou acerto.

Possíveis melhorias e expansão futura:
Interface Grafica: Tkinter ou Pygame para melhora visualização visual

Bancos de palavras: Carregamento das palavras a partir de arquivos externos para maior escolaridade.

Sistema de dicas: Fornece pista, com categoria.

Modo Multiplayer: Permite que um jogador defina a palavra e outro tente adivinhar Pontuação: Introduzir um sistema de pontos na tentativa de tempo.
