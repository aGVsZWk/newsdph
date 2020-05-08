$ sudo apt-get update
$ sudo apt-get install python3-dev python3-numpy
$ sudo apt-get install cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
$ sudo pip3 install opencv-python
$ wget https://github.com/Itseez/opencv/archive/3.1.0.zip
$ unzip 3.1.0.zip && cd opencv-3.1.0/
$ mkdir build && cd build
$ cmake -D CMAKE_BUILD_TYPE=Release \
        -D CMAKE_INSTALL_PREFIX=/usr/local  \
           PYTHON3_EXECUTABLE=/usr/bin/python3 \
           PYTHON_INCLUDE_DIR=/usr/include/python3.4 \
           PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.4m.so \
           PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.4/dist-packages/numpy/core/include ..
$ make -j4
$ wget http://labfile.oss.aliyuncs.com/courses/637/opencv-3.1.0.tar.gz
$ tar xzvf opencv-3.1.0.tar.gz
$ cd opencv-3.1.0/build
$ sudo make install
https://github.com/jwagner/smartcrop.js
wget http://labfile.oss.aliyuncs.com/courses/655/smartcrop.py
