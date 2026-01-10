import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue
"""
从网络上下载小内容说并以话题内容形式每五秒发布一行
"""

class NovelPubNode(Node):
    def __init__(
            self,
            node_name : str
                 ):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name}启动成功')
        self.novels_queue = Queue()
        self.novel_publisher = self.create_publisher(String,'novel',10)#创建发布者属性
        self.create_timer(5,self.timer_callback)

    def timer_callback(self):
        if self.novels_queue.qsize() > 0:
            line = self.novels_queue.get()
            msg = String()
            msg.data = line
            self.novel_publisher.publish(msg)
            self.get_logger().info(f'在“novel”话题里发布了：{msg}')

    def download_f(self,url):
        response = requests.get(url)#reponse对象包含了url网页的所有信息
        response.encoding = 'utf-8'
        text = response.text
        print(f'成功从{url}下载{len(text)}字节的"{text[:5]}..."内容')
        for line in text.splitlines():
            self.novels_queue.put(line)

def main():
    rclpy.init()
    node = NovelPubNode('novel_pub')
    node.download_f('http://0.0.0.0:8000/novel3.txt')
    rclpy.spin(node)
    rclpy.shutdown()