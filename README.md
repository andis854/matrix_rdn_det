# matrix_rdn_det - Randomize a matrix with the determinant value as parameter
Below we describe two ways of installing and using this script; calling it from a Linux shell or from a Python script/terminal.

## Python

###  Download

1. To download matrix_rdn_det, either DOWNLOAD AND PUT IN DIRECTORY or use Pypi via pip.
```sh
$ pip install matrix_rdn_det
```

### Usage

In your Python terminal or script type
```Python
from matrix_rdn_det import matrix_gen
```
Now call the function using
```Python
matrix_gen
```
The syntax is 
```Python
matrix_gen(dimension=2, det_value=1, lower_bound=-9, upper_bound=10, rdn_prm=0, attempts=200)
```


## Linux Shell

### Download

### Usage




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
