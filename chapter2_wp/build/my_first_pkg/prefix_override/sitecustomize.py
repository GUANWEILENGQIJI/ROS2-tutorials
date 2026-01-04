import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jvv/Desktop/tmp_code/python_Files/ros2-tut/chapter2_wp/install/my_first_pkg'
