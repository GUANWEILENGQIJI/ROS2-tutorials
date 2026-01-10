import espeakng
import rclpy
import threading
import time
from rclpy.node import Node
from queue import Queue
from example_interfaces.msg import String

class NovelSubNode(Node):
    def __init__(
            self,
            node_name
            ):
        super().__init__(node_name)
        self.novel_queue = Queue()
        self.get_logger().info(f'{node_name}启动成功')
        self.novel_subcriber = self.create_subscription(String,'novel',self.novel_callback,10)
        self.speech_thread = threading.Thread(target=self.speak_thread)
        self.speech_thread.start()

    def speak_thread(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'zh'
        while rclpy.ok():
            if self.novel_queue.qsize()>0:
                text = self.novel_queue.get()
                self.get_logger().info(f'当前线程{threading.get_ident()}开始朗读：{text}')
                speaker.say(text)
                speaker.wait()
            else:
                #让当前线程休眠
                time.sleep(1)

    def novel_callback(self,msg):
        self.novel_queue.put(msg.data)

def main():
    rclpy.init()
    node = NovelSubNode('novel_sub')
    rclpy.spin(node)
    rclpy.shutdown()
