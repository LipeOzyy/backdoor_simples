# backdoor_simples
Neste código o objetivo principal é implementar uma tecnica de reverse shell, ultilizando a linguagem Python. O código consiste em dois componentes, o cliente e servidor.

--------------------------------------------------------------------
# *Backdoor*: 
 A backdoor é o código que sera executado na maquina alvo, tem como obetivo inciar uma conexão com o a maquina do atacante e receber comandos shell, que serão executados diretamente no shell do sistema alvo. A resposta(output) sera então devolvida ao atacante por meio da LIB subprocess.

--------------------------------------------------------------------
# *Controlador*: 
 Neste código, o objetivo é aguardar a conexão da maquina vitima, e enviar os inputs de comando para o shell da mesma. Desta forma conectando as duas por meio da lib socket.
