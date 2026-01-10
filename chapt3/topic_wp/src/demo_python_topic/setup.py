from setuptools import find_packages, setup
import sys

package_name = 'demo_python_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    options={
        'build_scripts': {
            'executable': sys.executable,  # 使用当前 Python 环境
        },
    },
    maintainer='jvv',
    maintainer_email='1445977823@qqq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'novel_pub_node = demo_python_topic.novel_pub_node:main',
            'novel_sub_node = demo_python_topic.novel_sub_node:main',

        ],
    },
)
