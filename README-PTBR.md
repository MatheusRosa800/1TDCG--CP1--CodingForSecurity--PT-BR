# FIAP - 1° Checkpoint - Conding for Security

## Introdução
Checkpoint realizado com o intuito de colocar em prática todos os conhecimentos em Python adquiridos na matéria de Conding for Security, ministrada pelo [Professor Fábio Cabrini](https://www.linkedin.com/in/fabio-cabrini/).

## Participantes
- Eduardo dos Santos
- Henrique Lorenzetti
- Jorge Gabriel
- Matheus Rosa
- Pedro Augusto

## Desafio
O desafio consiste em criar um programa que solicite ao usuário informar a quantidade de números que deseja ver da Sequência de Fibonacci, assim os exibindo na tela.

### O que é Sequência de Fibonacci?
A sequência recebeu esse nome em homenagem ao matemático italiano Leonardo Fibonacci, que a descreveu pela primeira vez em seu livro Liber Abaci, publicado em 1202. A sequência de Fibonacci é encontrada em muitos fenômenos naturais, como na disposição das folhas nas plantas, nas conchas dos moluscos, no formato das galáxias e em muitas outras coisas. Além disso, a sequência possui propriedades interessantes e é estudada em muitas áreas da matemática e da ciência da computação.

### Como ela funciona?
É uma sequência numérica em que cada número é a soma dos dois números que o antecedem. Começando com 0 e 1, os primeiros números da sequência são 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, e assim por diante.

![Sequência de finonacci](https://assets-global.website-files.com/60ff690cd7b0537edb99a29a/61323d9cc3bdd91d263cd3c5_Sequencia-de-Fibonacci-em-uma-aspiral.jpg)

## Passo a passo para executar o programa

### 1° Passo - Abrir o terminal

### 2° Passo - Obter o projeto do github
Para obter os arquivos digite o comando: 
```
git clone https://github.com/MatheusRosa800/CP1---Coding-for-Security
cd CP1---Coding-for-Security
```
### 3° Passo - Execute o comando abaixo para abrir o programa Python
```
python3 index.py
```
### 4° Passo - Escreva a quantidade de números que deseja ver
![Imagem do programa](https://i.ibb.co/H42b5Pf/img.png)

## Youtube
[Link para o youtube](https://www.youtube.com/watch?v=WSloQqbnwzs&ab_channel=SweetGirl)

## Implementações para tratativa de erros
- [ ] Problema
- [x] Solução

---
- [ ] O usuário informa dados que não são número inteiros.

- [x] Validação com o ```try except``` para validar a entrada do dado.

- [ ] O usuário pede para exibir menos que 2 números.

- [x] Validação com o ```if``` para tratar a quantidade inserida pelo usuário com o seguinte teste lógico ```quantidade < 2```.

- [ ] O usuário força qualquer tipo de entrada não permitida.

- [x] O programa trata o erro e exibe uma mensagem para o usuário e volta o prompt para digitação novamente.

### Evidência
![Imagem de molde](https://i.ibb.co/56fdLrC/img.png)