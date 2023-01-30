# matrix_rdn_det 
Randomize a matrix with the determinant value as parameter.

This package can be used for e.g. linear algebra teachers that want to create system of equations exercises that are easy to solve by hand and possibly where fractions are avoided (if the parameter _det_value_ is chosen to be $\pm 1$).

Below we describe two ways of installing and using this package; by calling it from a Linux shell or from a Python shell.

## Using Python Shell

###  Download

Use one of the following methods: 
1. Using Pypi via pip:  (also works for Windows)
```bash
$ pip install matrix_rdn_det
```
2. Using git clone:
```bash
$ git clone https://github.com/andis854/matrix_rdn_det.git
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Move the directory _matrix_rdn_det_ (i.e. the inner directory) to a directory that is a search\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```
3. Download the source code: (also works for Windows) 
Download the files in [tar.gz](https://github.com/andis854/matrix_rdn_det/archive/refs/tags/v_0.0.3.tar.gz) or [zip](https://github.com/andis854/matrix_rdn_det/archive/refs/tags/v_0.0.3.zip) form. Extract the directory _matrix_rdn_det_ (i.e. the inner directory) and put in a directory that is a search path of Python, e.g.
```bash
~/.local/lib/python3.10/site-packages/ # Example of a common path.
```

To find the available search paths, type the following commands in a Python terminal.
```Python
>>> import sys
>>> sys.path
```

### Usage

In your Python terminal or script type
```Python
>>> import matrix_rdn_det
```
Now call the function using
```Python
matrix_rdn_det.matrix_gen
```
The syntax is 
```Python
matrix_rdn_det.matrix_gen(dimension=2, det_value=1, lower_bound=-9, upper_bound=10, rdn_prm=0, attempts=200)
```
For a detailed explanation, type
```Python
>>> help(matrix_rdn_det)
```
or
```Python
>>> help(matrix_rdn_det.matrix_gen)
```

## Using Linux Shell

###  Download

1. Using git clone:
```bash
$ git clone https://github.com/andis854/matrix_rdn_det.git
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Move the file _matrix_rdn_det.py_ to a directory that is in the shell variable $PATH, e.g.
```bash
~/.local/bin/ # Example of a common path.
```
2. Download the source code: 
Download the files in [tar.gz](https://github.com/andis854/matrix_rdn_det/archive/refs/tags/v_0.0.3.tar.gz) or [zip](https://github.com/andis854/matrix_rdn_det/archive/refs/tags/v_0.0.3.zip) form. Extract the file _matrix_rdn_det_ (i.e. the inner directory) to a directory that is in the variable $PATH, e.g.
```bash
~/.local/bin/ # Example of a common path.
```

Make the script executable, e.g.
```bash
$ chmod u+x ~/.local/bin/matrix_rdn_det # Use the path of the file
```
To find the available search paths, type the following in a Linux terminal.
```bash
$ echo $PATH
```

### Usage

In your Linux terminal, the command is
```bash
$ matrix_rdn_det.py
```
The syntax is
```bash
$ matrix_rdn_det.py [-h] [ dimension det_value ]
```
For more help, run
```bash
matrix_rdn_det.py -h
```


License
----

MIT License

Copyright (c) 2023 Anders Israelsson, andis854

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
