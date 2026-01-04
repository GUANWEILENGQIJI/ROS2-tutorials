###### 指令：

1.在当前终端修改[node_name].get_logger().info('请输入文本')输出信息指令(仅在当前终端生效):

```bash
export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{function_name}:{line_number}]:{message}'
```

2.ros2构建节点功能包:

```
ros2 pkg create --build-type ament_python --license Eg.Apache-2.0 Eg.my_first_pkg
```

3.ros2构建，--packages-select可选择构建功能包

```
colcon build --packages-select my_first_pkg
```

4.筛选并打印含有PYTHON字段的环境变量

```
printenv | grep PYTHON
```

5.执行脚本，Eg. ./install/setup.bash

```
source ./install/setup.bash
```

6.创建双重文件夹

```
mkdir -p chapter2_wp/src
```

7.拷贝文件，mv 待拷贝文件夹/ 目的文件夹

```
mv my_first_pkg/ chapter2_wp/src/
```

8.删除文件夹

```
rm -rf build/ install/ log/
```


###### 构建流程：

1.生成功能包

```
Eg.ros2 pkg create --build-type ament_python --license Eg.Apache-2.0 Eg.my_first_pkg
```

2.在(pkg)/(pkg)/ 目录下创建 py文件，往里写入节点代码 ，要想节点生效还需修改setup.py里面的entry_points，往console_scripts中括号里添加：

'(你起一个节点的名字) =_____(节点文件的路径，把“/”改成“.”):_____(函数名字)'。

```
Eg.'fucking_node1 = my_first_pkg.fucking_node1:main'
```

2.在package.xml里添加依赖，可以添加其他功能包作为依赖，影响后续构建顺序

```
Eg.<depend>rclpy</depend>
```

3.colcon构建

```
colcon build
```

构建完成后生成install文件夹，每次更新节点均需重新构建以更新install文件夹

4.执行setup.bash以更新当前终端环境变量

```
source ./install/setup.bash
```


###### 工作空间习惯

1.创建双重文件夹，src里存放源代码

```
mkdir -p workspace/src/
```

2.
