# CalendarReader

## Descricao

Um programa simples de leitura do Google Calendar e Drive

## Acesso

**Conta do google**: samuelsa.calendar@gmail.com

**Password**: [ask me]

## Uso

Crie entradas na agenda *Samuel Calendar* no Google Calendar. Mantenha a agenda simples, entradas uma em cima da outra vao confundir o programa.

Toda vez que o programa identifica uma nova entrada, ele vai imprimir o Summary e a Hora na tela. Ele vai usar a mesma cor que voce der no Google Calendar. Se voce nao especificar a cor, ele vai escolher uma aleatoria.

A tarefa vai ficar na tela ate que a tarefa acabe no Google Calendar ou que voce clique na tela (a tela e TouchScreen). Uma vez clicado, a mesma tarefa nao aparece de novo e o programa volta para a tela cinza ate que a proxima tarefa comece.

Voce tem a opcao de tocar um alarme no inicio de cada tarefa. Para isso, entre o nome do arquivo de som (MP3 ou WAV) na Description da tarefa do Google Drive. Escreva apenas o nome do arquivo, nada mais (nem <enter>).

O software ja vem com um arquivo padrao, chama-se beep.mp3. Se voce quiser um arquivo diferente, coloque um arquivo de som com nome escolhido no Google Drive da conta. Uma vez baixado para o RasPi, o que acontece da primeira vez que um arquivo e usado, nao e mais possivel modifica-lo. O programa nao vai baixar um arquivo de som que ja esta no cartao SD, mas voce sempre pode colocar um outro arquivo.

O arquivo de som e tocado 3 vezes, em intervalo de 2 segundos, no inicio da tarefa. Mantenha o som abaixo de 2 segundos para nao tocar um em cima do outro.

#Configuracao da Internet

O programa ja vem configurado com a rede Regina (casa do Rafael) e Salmonela (casa da Cris). Para mudar a rede ou a senha voce vai precisar de um teclado e mouse USB. Conecte os dois atras do dispositivo, lique o RasPi, aperte <ESC> para sair do programa da agenda, clique no simbolo de rede wireless e configure a nova rede.
