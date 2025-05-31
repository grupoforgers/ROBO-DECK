from setuptools import setup

setup(
    name='sensor_node',
    version='0.0.0',
    packages=['sensor_node'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu_nome',
    maintainer_email='seu_email@exemplo.com',
    description='Pacote ROS 2 sensor_node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_node_node = sensor_node.sensor_node_node:main'
        ],
    },
)
