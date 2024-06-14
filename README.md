# Boas-vindas ao repositório do projeto `Algorithms`

  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />

  Neste projeto você irá resolver problemas e otimizar algoritmos desenvolvendo a sua capacidade de implementar soluções para os mais diversos problemas do dia a dia!
  
  🚵 Habilidades exercitadas:
  
Lógica;

Capacidade de interpretação de problemas;

Capacidade de interpretação de um código legado;

Capacidade de otimizar a resolução de problemas e;

Resolver problemas/Otimizar algoritmos sob pressão.

</details>

# Orientações

<details>
  <summary><strong>⚠️ Antes de começar a desenvolver</strong></summary><br />

  1. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`
  
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate".
  :warning: Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Requisitos Obrigatórios

## 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa Product Manager `(PM)` quer saber qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível.

O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.

Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada `força bruta` em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável `target_time` e serão analisados os retornos da função.

:eyes: _De olho na Dica:_ O melhor horário será aquele no qual o contador retornado pela função for o maior

## 2 - Criptografia de inversões (Testes)

> Implemente em: tests/encrypt/test_encrypt.py

Durante a dinâmica em grupos de um processo seletivo, a empresa contratante definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa deve criar uma função de criptografia, e a segunda pessoa deve implementar os testes da função implementada pela primeira pessoa.

Você fará o papel da _**segunda pessoa**_ nessa dinâmica, ou seja: deve implementar os testes de uma função de criptografia.

Esse teste deve se chamar `test_encrypt_message`, e ele deve garantir que a função de criptografia `encrypt_message` deve respeitar uma lógica específica.

<details>
  <summary>
    <b>🧠 Entenda a lógica da função de criptografia</b>
  </summary>

* Recebe uma string `message` e um inteiro `key` como parâmetros
* Se `key` e `message` não possuírem os tipos corretos, uma exceção deve ser lançada
* Se `key` não for um índice positivo válido de `message`, retorna a string `message` invertida
* Se `key` for ímpar:
  * divide `message` no índice `key`, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas
* Se `key` for par:
  * divide `message` no índice `key`, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas

Veja alguns exemplos:

<p align="center">
    <img src="encrypt-examples.png" alt="Exemplos ilustrativos da lógica da função encrypt_message" width="640" />
</p>

</details>

## 3 - Palíndromos (Recursividade)

Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um _booleano_, `True` ou `False`.

Mas o que é um palíndromo?

> Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`.

:warning: Neste projeto iremos focar somente em **palavras palíndromas** e não em frases ou números.

## 4 - Anagramas (Algoritmo de ordenação)

Faça um algoritmo que consiga comparar duas _strings_, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla `()` com a primeira string ordenada, a segunda string ordenada e um _booleano_, `True` ou `False` representando se são anagramas.

O algoritmo deve considerar letras _maiúsculas_ e _minúsculas_ como iguais durante a comparação das entradas, ou seja, ser _case insensitive_.

Mas o que é um anagrama?

> "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

---

# Requisitos Bônus

## 5 - Encontrando números repetidos (Algoritmo de busca)

Dada um _array_ de números inteiros contendo `n + 1` inteiros, chamado de `nums`, em que cada inteiro está no intervalo `[1, n]`.

Retorne apenas um número duplicado em `nums`.

## 6 - Palíndromos (Iteratividade)

Resolva o mesmo problema apresentado no `requisito 2 - Palíndromos`, porém dessa vez utilizando a solução iterativa.

* Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
  * O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;

* O algoritmo deve utilizar a solução iterativa;

* O código deve ser feito dentro do arquivo `challenge_palindromes_iterative.py`.

---
