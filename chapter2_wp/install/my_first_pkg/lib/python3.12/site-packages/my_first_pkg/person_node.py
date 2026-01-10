import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(
            self,
            node_name : str,
            name_val : str,
            age_val : int
        ) -> None:
        super().__init__(node_name)
        print('PersonNode的__init__()函数被调用了')
        self.name = name_val
        self.age = age_val

    def eat(self,fd_name : str):
        """
        eat 的 Docstring
        
        :param self: 某个人
        :param fd_name: 喜欢吃的食物的名字
        :type fd_name: str
        """
        # print(f'{self.age}岁的{self.name}爱吃{fd_name}')
        self.get_logger().info(f'{self.age}岁的{self.name}爱吃{fd_name}')




def main():
    rclpy.init()
    node=PersonNode('NodeOfZS','法外狂徒张三',21)
    node.eat('炸鸡')
    rclpy.spin(node)
    print('---------------')
    node.destroy_node()
    rclpy.shutdown()

# main()