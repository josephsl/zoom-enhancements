# Aprimoramentos na acessibilidade do  Zoom #

* Autores: Mohamad Suliman, Eilana Benish
* Download [versão estável][1]
* Compatibilidade com NVDA: 2018.4 a 2022.1

Esse complemento aprimora a experiência de uso do Zoom para usuários do
NVDA, fornecendo atalhos de teclado para lidar com alertas de diferentes
eventos durante uma reunião, tornando o processo de controle remoto muito
mais acessível e suave, e muito mais.

## atalhos de teclado para controle de alertas em reuniões 

* NVDA + Shift + A: alterna entre diferentes modos de relatório de
  alertas. Os seguintes modos estão disponíveis:

    * Modo de relatório de todos os alertas, em que todos os alertas são
      relatados como de costume
    * Bipe para alertas, em que o NVDA emitirá um bipe curto para cada
      alerta exibido no Zoon
    * Silenciar todos os alertas, onde o NVDA ignorará todos os alertas
    * Modo personalizado, em que o usuário pode personalizar os alertas que
      deseja ter e os que não deseja. Isso pode ser feito usando a caixa de
      diálogo de configurações do complemento ou usando os atalhos de
      teclado dedicados para isso

Os atalhos a seguir podem ser usados para ativar/desativar os anúncios de
cada tipo de alerta (observe que isso entrará em vigor quando o modo
personalizado estiver selecionado):

* NVDA + Ctrl + 1: o participante entrou/saiu da reunião (somente para o
  servidor)
* NVDA + Ctrl + 2: o participante entrou/saiu da sala de espera (somente
  servidor)
* NVDA + Ctrl + 3: Áudio silenciado pelo servidor
* NVDA + Ctrl + 4: Vídeo interrompido pelo servidor
* NVDA + Ctrl + 5: Compartilhamento de tela iniciado/interrompido por um
  participante
* NVDA + Ctrl + 6: Permissão de gravação concedida/revogada
* NVDA + Ctrl + 7: Bate-papo público na reunião recebido
* NVDA + Ctrl + 8: Bate-papo privado na reunião recebido
* NVDA + Ctrl + 9: upload de arquivos durante a reunião concluído
* NVDA + Ctrl + 0: privilégio de host concedido/revogado
* NVDA + Shift + Ctrl + 1: o participante levantou/levantou a mão (somente
  para o servidor)
* NVDA + Shift + Ctrl + 2: Permissão de controle remoto concedida/revogada
* NVDA + Shift + Ctrl + 3: mensagem de bate-papo IM recebida


Note que você precisa deixar a opção de relatar todos os tipos de alerta
selecionada (nas configurações de acessibilidade do Zoom) para que o
complemento funcione como esperado.

## Atalho de teclado para abrir o diálogo de adição 

NVDA + Z Abre a caixa de diálogo do complemento!

Usando essa caixa de diálogo, você pode :

* Veja quais alertas são anunciados e quais não são
* Selecione os tipos de alertas que você deseja que sejam anunciados
* Selecionar o modo de relatório de alertas
* Salvar alterações personalizadas

## Controle remoto 

depois que uma permissão de controle remoto for concedida, NVDA + O moverá o
foco para dentro/fora da tela de controle remoto

Note que o foco deve estar em um dos controles da reunião para que seja
possível controlar remotamente a outra tela

## Uma nota importante

Atualmente, o recurso do modo de alertas personalizados, no qual o usuário
pode escolher quais alertas deseja receber e quais não deseja receber,
funciona com o Zoom somente quando o idioma da interface do usuário está
definido como inglês.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=zoomEnhancements
