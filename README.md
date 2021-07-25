# ppdT1.2

Trabalho 1.2 de PPD

Membros do grupo:
 - Franco Schmidt
 - Lucas Santana
 - Vinícius Risso

Considerações gerais sobre o trabalho:

  - Utilizamos o xmlrpc em Python, seguindo a documentação e exemplos fornecidos pelo professor.
  - Para nossa implementação e testes, usamos uma classe para a tabela hash pronta
  - Nossos testes foram feitos com a hash possuindo M = 2 000 000, e m = 800k e/ou 80k
  - Foi utilizada a ideia de MultiCall do xmlrpc, não era viável fazer 800k de chamadas uma por uma, então o multi junta as chamadas e faz de uma vez.
  - Nosso client chama uma terceira interface para limpar a hash ao fim do código
  - Nosso client cria as chaves de maneira iterativa, logo, no nosso caso, NUNCA haverá colisões na hash, principalmente pois limpamos ela ao fim de cada execução.
  - Temos DUAS implementações de client, quisemos testar duas abordagens utilizando o MultiCall, mas a principal que deve ser avaliada é o arquivo clientSide.py
  - Nós adicionamos os valores recebidos pelo get() em uma lista chamada list_values, caso necessário visualizar que a hash está realmente sendo preenchida

Considerações específicas sobre o trabalho:

  - A diferença entre o arquivo clientSide.py e o testeThread.py é a abordagem, temos que no primeiro, nós SEMPRE enviamos uma quantidade de 'multis' (junção das chamadas) igual à quantidade de threads criadas. Já no segundo, a quantidade de multis é SEMPRE 8 (valor máximo de threads).
  - Nosso server side possui 3 interfaces, get(), put() e clear(), sendo o clear() para limpar (criar de novo) a Hash, e as outras especificadas no escopo do trabalho.
  - Servidor configurado para localhost usando a porta 8000, caso necessário, só trocar a porta no arquivo do server, e a rota no client side.
  - Para nosso último teste usando o arquivo clientSide,py tivemos um status 'Morto', pois o server não suportou.
  - No caso específico do testeThread.py usamos um valor menor de 'm' pois seria muito demorado se usássemos um valor maior

Valores experimentais obtidos:

  clientSide.py
  M = 2 000 000, m = 800 000
  1 thread -> 55.97792673110962 segundos
  2 thread -> 51.70153880119324 segundos
  4 thread -> 102.636150598526 segundos
  8 thread -> Morto

  testeThread.py
  M = 2 000 000, m = 80 000
  1 thread -> 82.61805844306946 segundos
  2 thread -> 73.28466081619263 segundos
  4 thread -> 69.02350997924805 segundos
  8 thread -> 65.25468921661377 segundos

Perguntas:

  - É necessário implementar algum controle de concorrência no acesso aos métodos e à tabela hash por parte dos diferentes clientes?
  
  Sim, no caso de métodos que só precisam do acesso simultâneo à mesma informação como o get(), não julgamos necessário, pois não hà escrita ou quaisquer manipulação/modificação do dado,
  entretanto, em casos como put(), é interessante e necessário ser usada um controle, pois pode acontecer colisões e conflitos, no entanto, para nosso escopo, ainda sim,
  não é 100% necessário, por ser uma aplicação pequena.
