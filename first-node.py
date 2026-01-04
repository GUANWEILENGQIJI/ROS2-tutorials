import rclpy
from rclpy.node import Node

def main():
    rclpy.init()                #rclpy初始化
    node=Node('fucking_node1')  #创建节点
    node.get_logger().info('fuck you fucking_node草拟马的')    #打印运行信息
    rclpy.spin(node)            #运行节点
    rclpy.shutdown(node)

if __name__ == '__main__':
    main()

