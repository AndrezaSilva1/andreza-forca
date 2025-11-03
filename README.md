Jogo da Forca
Data 01/11/2025
Descrição do projeto:
Este projeto é implementação desenvolvida com jogo python, utilizando a biclioteca pygame para criar uma interface grafica com usuario.

O jogo começa com menu principal, onde o jogador pode:
-Inicar o jogo
-Sair do jogo

No jogo, o jogador tem que adivinhar uma palavra escolhida aleatoriamente de um arquivo externo(Palavras.txt) digitando as letras no teclado e depois dando enter.
A cada erro, uma parte do boneco da forca e desenhado. O jogo finaliza quando:
- O jogador acertas todas as letras (vitoria)ou
- Quando o jodagor erra (derrota)

Estrutura do Projeto
JogoDaForca/
│
├── JogoForca.py    #codigo principal do jogo e interface gráfica       
├── Palavras.txt    #Palavras jogo        
└── README.md       #Documentação do projeto

Tecnologias usadas
- python 3.10+
- Pygame(bliblioteca para interface gráfica)

Conceitos de Programação Orientada a Objetos(POO)
-Encapsulamento: Classes Button, Menu, Jogo de Game organizam funcionalidades especificas.
-Abastração: Cada classe representa um conceito logico do jogo
-Herança: A estrutura garantir facil expansão(ex:novos menu  ou modos de jogos)                                                            
-Polimorfismo: Métodos que mudam o comportamento conforme o contexto(ex: callbacks dos botões).

Pré-Riquisitos                                                                                                                             
Antes de começa o jogo de e necessario ter:
-Python instalado(versão 3.10 ou mais avancada)
-Biblioteca Pygame
Para baixar o pygame e só enserir esse comando no terminal:
pip install pygame

Como executar o jogo
-Baixe ou clone o repositório:
git clone https://github.com/AndrezaSilva1/andreza-forca/blob/main/jogo25102025.py
-Acesse a pasta do projeto:
cd JogoForca.py
- Execute o jogo:
python JogoForca.py
- O menu será exibido com as opções:
Iniciar o jogo: Começa o jogo
Sair: Fecha o programa

Arquivo de Palavras:
O arquivo palavras.txt contém a lista de palavras que o jogo usa.
Você pode adcionar, remover ou editar palavras.
Exemplo:
lapis  
mesa  
computador  
livro  
sol  
lua  
melancia  
abacate  
melao  
abacaxi  
goiaba  
uva  
cachorro  
gato  
tigre  
leao

Créditos:
Desenvolvido : Andreza Pereira  
Versão: 6ª Versão Final  
Data: 01/11/2025  
Linguagem: Python  
Biblioteca: Pygame

Licença
Este projeto é de uso educacional e livre para estudos e melhorias.
Sinta-se a vontade para aprimorar ou modificar meu jogo.
