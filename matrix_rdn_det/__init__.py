"""
Randomize a matrix with the determinant value as a parameter. The output is LaTeX compatible.
    
                        This can be used for e.g. linear algebra teachers that want to create system of equations exercises 
                        that are easy to solve by hand and possibly where fractions are avoided 
                        (if det_value is chosen to be \u00B11).
                        
Methods
-------
det_int
  .........
numpy2latex
  Make numpy array LaTeX friendly.
    
    Parameters
    ----------
    matrix : numpy.array
        Array that is written LaTeX friendly. 
    det_value : bool, optional
        If true, print the output in terminal. 
    
    Returns
    -------
    output : str
        A numpy array with shape [dimension,dimension].
    
    Notes
    -----
    The output can be used together with LaTeX environment, e.g.
    \begin{pmatrix}
        [output]
    \end{pmatrix}
    or
    \begin{array}
        [output]
    \end{array}
Randomize a matrix with the determinant value as parameter.
    
    Parameters
    ----------
    dimension : int, optional
        Dimension of the matrix. If set to a non-positive integer the function returns an empty matrix.
    det_value : int, optional
        Value of the determinant of the matrix. Must be an integer.
    lower_bound : int, optional
        Sets the lower bound of the entries in the matrix to lower_bound.
    upper_bound : int, optional
        Sets the upper bound of the entries in the matrix to upper_bound-1.
    rdn_prm : int, optional
        Sets the number of randomized parameters in the function. This can be used to speed 
        up the calculations if the determant value is large (e.g. 7 or larger). If not a
        positive integer, rdn_prm is set to be 0.
    attempts : int, optional
        Sets the number of attempts to randomized parameters in the function. This is used 
        to restart the function if the calculations are taking too long if the determinant
        value is large (e.g. 7 or larger). If not a positive integer, rdn_prm is set to be 200.
    
    Returns
    -------
    out : numpy.ndarray
        A numpy array with shape [dimension,dimension].
    
    Notes
    -----
    This can be used for e.g. linear algebra teachers that want to create system of equations exercises 
    that are easy to solve by hand and possibly where fractions are avoided 
    (if det_value is chosen to be \u00B11).
    
    When the dimension is 2 or 3 the difference between lower_bound and upper_bound has to be at
    least 3 (except if lower_bound <= -1 and upper_bound >=1). This is to ensure that the problem
    is solvable. Otherwise the difference between lower_bound and upper_bound has to be at least 2.
    
    If the dimension is set to 7 or higher, it is recommended to set a few random parameters to
    speed up the calculcations. However, the randomness of the entries will decrease. The number
    of attemps is only used if there are randomized parameters set.
"""
from matrix_rdn_det.matrix_rdn_det import det_int,matrix_gen,numpy2latex
