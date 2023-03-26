project(savePose)
 
cmake_minimum_required(VERSION 3.0)
 
find_package(VISP REQUIRED)
 
include_directories(${VISP_INCLUDE_DIRS})
 
add_executable(savePose savePose.cpp)
target_link_libraries(savePose ${VISP_LIBRARIES})