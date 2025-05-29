from setuptools import setup

setup(
    name='camera_node',
    version='0.0.0',
    packages=['camera_node'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu_nome',
    maintainer_email='seu_email@exemplo.com',
    description='Pacote ROS 2 camera_node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node_node = camera_node.camera_node_node:main'
        ],
    },
)
