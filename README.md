# matrix_rdn_det 
Randomize a matrix with the determinant value as parameter

Below we describe two ways of installing and using this script; by calling it from a Linux shell or from a Python script/terminal.

## Python

###  Download

Use one of the following methods:
1. Using Pypi via pip:
```sh
$ pip install matrix_rdn_det
```
2. Download the source code, extract the file matrix_rdn_det.py and put in a directory that is a search path of Python, e.g.
```sh
~/.local/lib/python3.10/site-packages/ # Replace this with appropriate search path.
```
To find the available search paths, type in the following in a Python terminal.
```Python
>>> import sys
>>> sys.path
```

### Usage

In your Python terminal or script type
```Python
>>> from matrix_rdn_det import matrix_gen
```
Now call the function using
```Python
matrix_gen
```
The syntax is 
```Python
matrix_gen(dimension=2, det_value=1, lower_bound=-9, upper_bound=10, rdn_prm=0, attempts=200)
```
For a detailed explanation, type
```Python
>>> help(matrix_gen)
```

## Linux Shell

###  Download

Download the source code, extract the file matrix_rdn_det.py and put in a directory that is in the variable $PATH, e.g.
```sh
~/.local/bin/ # Example of a common path.
```
To find the available search paths, type the following in a Linux terminal.
```sh
$ echo $PATH
```

### Usage

In your Linux terminal type
```bash
$ from matrix_rdn_det import matrix_gen
```
Now call the function using
```Python
matrix_gen
```
The syntax is 
```Python
matrix_gen(dimension=2, det_value=1, lower_bound=-9, upper_bound=10, rdn_prm=0, attempts=200)
```
For a detailed explanation, type
```Python
>>> help(matrix_gen)
```




License
----

MIT License

Copyright (c) 2023 Anders Israelsson

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
