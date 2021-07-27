# ppdT1.2

Trabalho 1.2 de PPD

Membros do grupo:
 - Franco Schmidt
 - Lucas Santana
 - Vinícius Risso

Considerações gerais sobre o trabalho:

  - Utilizamos o xmlrpc em Python, seguindo a documentação e exemplos fornecidos pelo professor.
  - Para nossa implementação e testes, usamos uma classe para a tabela hash pronta
  - Nossos testes foram feitos com a hash possuindo M = 2 000 000, e m = 800k
  - Foi utilizada em nossos arquivos multiCase1.py e multiCase2.py ideia de MultiCall do xmlrpc, não era viável fazer 800k de chamadas uma por uma, então o multi junta as chamadas e faz de uma vez.
  - É interessante limpar a hash ao fim de cada teste, para achar um teste mais direto (sem considerar colisões e afins)
  - Nosso client cria as chaves de maneira iterativa, logo, no nosso caso, NUNCA haverá colisões na hash, principalmente pois limpamos ela ao fim de cada execução.
  - Temos TRÊS implementações de client, quisemos testar três abordagens, duas utilizando o MultiCall, e uma em chamadas sequenciais, mas a principal que deve ser avaliada é o arquivo clientSide.py
  - Nós adicionamos os valores recebidos pelo get() em uma lista chamada list_values, caso necessário visualizar que a hash está realmente sendo preenchida

Considerações específicas sobre o trabalho:

  - A diferença entre o arquivo multiCase1.py e o multiCase2.py é a abordagem, temos que no primeiro, nós SEMPRE enviamos uma quantidade de 'multis' (junção das chamadas) igual à quantidade de threads criadas. Já no segundo, a quantidade de multis é SEMPRE 8 (valor máximo de threads).
  - Nosso server side possui 2 interfaces, get(), put() como foram especificadas no escopo do trabalho.
  - Servidor configurado para localhost usando a porta 8000, caso necessário, só trocar a porta no arquivo do server, e a rota no client side. 
  - Como podemos ver, a utilização do MultiCall tem um desempenho muito superior, pois não possui uma fila de espera como no outro método

Valores experimentais obtidos:

  clientSide.py
  M = 2 000 000, m = 800 000
  2 thread -> 397.8955545425415 segundos
  4 thread -> 388.0931589603424 segundos
  8 thread -> 375.51914620399475 segundos

  multiCase1.py
  M = 2 000 000, m = 800 000
  2 thread -> 42.91783595085144 segundos
  4 thread -> 39.42269325256348 segundos
  8 thread -> 37.87558698654175 segundos

  multiCase2.py
  M = 2 000 000, m = 800 000
  2 thread -> 42.65044188499451 segundos
  4 thread -> 39.37940168380737 segundos
  8 thread -> 37.92666149139404 segundos
  

Perguntas:

  - É necessário implementar algum controle de concorrência no acesso aos métodos e à tabela hash por parte dos diferentes clientes?
  
  Sim, no caso de métodos que só precisam do acesso simultâneo à mesma informação como o get(), não julgamos necessário, pois não hà escrita ou quaisquer manipulação/modificação do dado,
  entretanto, em casos como put(), é interessante e necessário ser usada um controle, pois pode acontecer colisões e conflitos, no entanto, para nosso escopo, ainda sim,
  não é 100% necessário, por ser uma aplicação pequena. Percebemos também que, o server side ficava muito lento após ter tanta 'request' na fila, o gerenciamento de controle de concorrência deve sim ser implementado nesses casos brutos e grandes, pois caso algum precise de prioridade, o servidor pode atender mais facilmente.
