# denv
Dockerized Develop Environment

# Build
- `docker build -t denv .`
- `sudo cp denv.py /usr/local/bin/denv`


# Python Examples
## Run Prompt
- Run python3 from host
```sh
$ python3
Python 3.10.9 (main, Jan 11 2023, 15:21:40) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
>>> 
```
As can be seen, my host python3 version is: `3.10.9` and `numpy` is not installed in host.


- Now execute it from the denv docker. You can see the version in the docker is `3.9.2` and the current directory is in `/app`.  
```sh
$ denv python3 
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> current_working_directory = os.getcwd()
>>> print(current_working_directory)
/app
>>> 
```

- Use `numpy` in denv image.
```sh
$ denv python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> 
```

## Run Script
- Run hello
```sh
$ denv python3 examples/python_example/hello_denv.py
Hello Denv
```

- Run numpy example
```sh
$ denv python3 examples/python_example/numpy_example.py 
Addition Result: [ 7  9 11 13 15]
Subtraction Result: [-5 -5 -5 -5 -5]
Multiplication Result: [ 6 14 24 36 50]
Division Result: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
Square Root Result: [1.         1.41421356 1.73205081 2.         2.23606798]

```


# CPP Example
```sh
$ denv make
g++ -Wall -g -o HelloWorld HelloWorld.cpp

$ ls
HelloWorld  HelloWorld.cpp  Makefile

$ denv ./HelloWorld
Hello, World!

$ denv make clean
rm -f HelloWorld

$ ls
HelloWorld.cpp  Makefile

```

# Arduino Example
