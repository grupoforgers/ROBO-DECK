from setuptools import setup

setup(
    name='esp32_bridge',
    version='0.0.0',
    packages=['esp32_bridge'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='seu_nome',
    maintainer_email='seu_email@exemplo.com',
    description='Pacote ROS 2 esp32_bridge',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'esp32_bridge_node = esp32_bridge.esp32_bridge_node:main'
        ],
    },
)
