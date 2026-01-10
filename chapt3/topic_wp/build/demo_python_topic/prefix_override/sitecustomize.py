import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jvv/Desktop/tmp_code/python_Files/ros2-tut/chapt3/topic_wp/install/demo_python_topic'
