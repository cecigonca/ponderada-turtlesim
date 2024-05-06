# Desenhando com Turtlesim
Atividade ponderada: criar um projeto ROS que interage com o a tartaruga do trutlesim, através de um script em Python. 

## Vídeo 

## Instruções para Execução
### Pré-requisitos
Ter os seguintes tecnologias instaladas localmentes:
- Python 3 ou superior;
- Turtlesim
- Ros2
  
Caso seja necessário instala-los, opte por seguir os passos indicados nesses links: 

[Instalando ROS](https://rmnicola.github.io/m6-ec-encontros/E01/ros) 

[Criando um Workspace](https://rmnicola.github.io/m6-ec-encontros/workspaces) 

### Execução
1. Clone esse repositório no seu computador. Para isso, você deve abrir o terminal, navegar até onde gostaria que o repositório fosse clonado e colar o seguinte comando:
   <script> git clone ... </script>

2. Ainda em seu terminal, navegue até o diretório correto:
  <script> git clone .../script>


3. Agora digite os seguinte comando para iniciar a tela da tartaruga:

  <script>  ros2 run turtlesim turtlesim_node </script>

4. Nessa etapa, você precisará abrir um segundo terminal, abrir o mesmo diretório e digitar os seguintes comandos:
  colcon build ->  Esse comando irá instalar as dependências necessárias para rodar o meu pacote com o ROS (pastas: build, log e install)
  source install/local_setup.bash
  ros2 run ponderada_cecilia ponderada -> iniciar a tartaruga

## Vídeo do Projeto 
[Assista ao vídeo](videos/meu_video.mp4)




    



 Esse comando irá instalar as dependências necessárias para rodar o meu pacote com o ROS (pastas: build, log e install)


