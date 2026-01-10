###### 指令：

1.在当前终端修改get_logger().info('请输入文本')输出信息指令:

```bash
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{function_name}:{line_number}]:{message}'
```

2.ros2构建节点功能包:

```apache
ros2 pkg create --build-type ament_python --license Apache-2.0 your_pkg_name
```

3.ros2构建，--packages-select可选择构建功能包

```apache
colcon build --packages-select my_first_pkg
```

4.筛选并打印含有PYTHON字段的环境变量

```apache
printenv | grep PYTHON
```

5.执行脚本，Eg. ./install/setup.bash

```apache
source ./install/setup.bash
```

6.创建双重文件夹

```apache
mkdir -p chapter2_wp/src
```

7.拷贝文件，mv 待拷贝文件夹/ 目的文件夹

```apache
mv my_first_pkg/ chapter2_wp/src/
```

8.删除文件夹

```apache
rm -rf build/ install/ log/
```

9.ros2查看节点信息

```apache
ros2 node info /node_name
```

10.ros2查看话题信息

```
ros2 topic echo /topic/topic_name...#查看话题的内容
ros2 topic info /topic/topic_name...#查看话题的类型，发布者与订阅者
ros2 interface show /topic_interface... #查看话题接口的具体结构和字段定义
```

11.ros2发布话题指令

```apache
ros2 topic pub /topic_name /topic_interface topic_content
```

topic_content格式为yaml格式，每个标点符号后加空格

```apache
robot: {id: r2d2, specs: {height_cm: 96, weight_kg: 32.5}}
#等价于
robot:
  id: r2d2
  specs:
    height_cm: 96
    weight_kg: 32.5
```

###### 构建流程：

1.生成功能包

```apache
ros2 pkg create --build-type ament_python --license Apache-2.0 your_pkg_name
```

2.在(pkg)/(pkg)/ 目录下创建 py文件，往里写入节点代码 ，要想节点生效还需修改setup.py里面的entry_points，往console_scripts中括号里添加：

```
'fucking_node = your_pkg_name.node_name:function_name'
```

2.在package.xml里添加依赖，可以添加其他功能包作为依赖，影响后续构建顺序

```
<depend>rclpy</depend>
```

3.colcon构建(在工作空间里构建)

```
colcon build
```

构建完成后生成install文件夹，每次更新节点均需重新构建以更新install文件夹

4.执行setup.bash以更新当前终端环境变量

```
source ./install/setup.bash
```


###### 工作空间

1.创建双重文件夹，src里存放源代码

```
mkdir -p workspace/src/
```

2.节点文件模板

```apache
import rclpy
from rclpy.node import Node

class Node'sName(Node):
    def __init__(
	self,
	node_name : str
	):
        super().__init__(node_name)
        self.get_logger().info(f'{node_name}启动成功')

def main():
    rclpy.init()
    node = NovelPubNode('Node'sName')
    rclpy.spin(node)
    rclpy.shutdown()
```


###### 多线程

1.用threading.Thread()方法创建一个thread对象，再用threading.start()方法开始线程

```apache
thread = threading.Thread(target = function)
```

2.查看当前线程编号函数

```apache
threading.get_ident()
```



###### 发布一个话题

创建节点，用.create_publisher方法创建一个Publisher对象，用publisher()方法发布

```apache
from rclpy.node import Node
node = Node('node_name')
publisher = node.create_publisher(msg_type,str,qos_profile)
publisher.publish(#msg_type类型对象的data属性)
```
