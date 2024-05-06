import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

class TortugaController(Node):
    def __init__(self):
        super().__init__('tortuga_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')

        self.spawn_client.wait_for_service()
        self.set_pen(255, 0, 0, 3, False)
        self.spawn_turtle()  # Inicializa a turtle1

    def spawn_turtle(self):  # Inicializa a turtle2
        spawn_request = Spawn.Request()
        spawn_request.x = 6.0
        spawn_request.y = 5.5
        spawn_request.theta = 0.0
        spawn_request.name = 'turtle2'
        future = self.spawn_client.call_async(spawn_request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('Tortuga 2 spawnada com sucesso!')
        else:
            self.get_logger().info('Spawnar tortuga 2 deu errado!')S

    def set_pen(self, r, g, b, width, off):  # Definindo a pen para vermelho
        while not self.pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Aguardando pelo serviço set_pen para ficar disponível...')
        pen_request = SetPen.Request()
        pen_request.r = r
        pen_request.g = g
        pen_request.b = b
        pen_request.width = width
        pen_request.off = off
        future = self.pen_client.call_async(pen_request)
        rclpy.spin_until_future_complete(self, future)

    def draw_triangle(self):  # Usando twist para fazer o triângulo (usando ângulos para rotação)
        twist = Twist()
        twist.linear.x = 2.0  # Velocidade
        self.move(twist, 2.0)  # Primeiro lado; se move por 2s

        twist.linear.x = 0.0  # Para o movimento linear enquanto faz a rotação
        twist.angular.z = 2.094  # 120 graus em radianos
        self.move(twist, 1.0)  # Girar por 1s

        twist.linear.x = 2.0
        twist.angular.z = 0.0  # Para a rotação
        self.move(twist, 2.0)  # Segundo lado; se move por 2s

        twist.linear.x = 0.0
        twist.angular.z = 2.094
        self.move(twist, 1.0)  # Segunda rotação; funciona da mesma forma da primeira

        twist.linear.x = 2.0
        twist.angular.z = 0.0
        self.move(twist, 2.0)  # Terceiro lado; funciona da mesma forma da segunda

        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher_.publish(twist)  # Finaliza movimento

    def move(self, twist, duration):  # Essa função serve para controlar o movimento, a partir dos comandos específicos do twist na função draw_triangle
        end_time = time.time() + duration
        while time.time() < end_time:  # Define quando o movimento deve parar
            self.publisher_.publish(twist)
            time.sleep(0.1)

    def kill_turtle(self, turtle_name):
        kill_request = Kill.Request()
        kill_request.name = turtle_name
        future = self.kill_client.call_async(kill_request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'{turtle_name} morta com sucesso.')
        else:
            self.get_logger().info('Falha ao matar tartaruga.')

def main(args=None):
    rclpy.init(args=args)
    node = TortugaController()
    node.draw_triangle()
    time.sleep(2)
    node.kill_turtle('turtle2')  # Tenta matar a tartaruga
    rclpy.shutdown()

if __name__ == '__main__':
    main()
