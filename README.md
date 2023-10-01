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
