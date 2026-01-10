import rclpy

from my_first_pkg.person_node import PersonNode

"""
面向对象实例
"""

class WriterNode(PersonNode):
    def __init__(
            self,
            name_val: str,
            age_val : int,
        ) -> None:
        print('WriterNode的__init__()方法被调用了')
        super().__init__(name_val,age_val)
    def books(
            self,
            book_val : str
            ):
        print(f'{self.age}的{self.name}写了"{book_val}"')


def main():
    node = WriterNode('毛主席',34)
    node.eat('辣椒')
    node.books('毛概')