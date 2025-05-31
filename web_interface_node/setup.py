from setuptools import setup

setup(
    name='web_interface_node',
    version='0.0.0',
    packages=['web_interface_node'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu_nome',
    maintainer_email='seu_email@exemplo.com',
    description='Pacote ROS 2 web_interface_node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'web_server = web_interface_node.web_server:main'
        ],
    },
)
