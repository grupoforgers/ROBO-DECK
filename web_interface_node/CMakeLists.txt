cmake_minimum_required(VERSION 3.5)
project(web_interface_node)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(DIRECTORY web_interface_node DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY web DESTINATION share/${PROJECT_NAME})
install(PROGRAMS
  web_server.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
