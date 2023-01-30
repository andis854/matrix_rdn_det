#!/usr/bin/python3
' '
# Created by: Anders Israelsson, 2023
# Email: andis854@outlook.com
# https://github.com/andis854/matrix_rdn_det

import numpy

# det_int calculates the determinant of matrices with interger entries
# and reduces the number of calculations whenever an entry is 0.
def det_int(matrix):
    '''Calculate the determinant of a square matrix with integer entries. 
    
    The function expands rows and columns recursively and reduces calculation by 
    finding the rows/columns with the largest number of zeroes.
    
    Parameters
    ----------
    matrix : numpy.array
        Numpy array representing a square matrix, which determinant is to be evaluated.
    
    Returns
    -------
    determinant : int
        The determinant of the input matrix.
         '''
    dimension = numpy.size(matrix, axis=0)
    if dimension != numpy.size(matrix, axis=1):
        raise TypeError('Not a square matrix!')
    elif dimension == 1:
        return matrix[0,0]
    else:

        max_zero = dimension

        row_column_index = 0

        for row in range(0, dimension):
            if numpy.count_nonzero(matrix[row, :]) < max_zero:
                max_zero = numpy.count_nonzero(matrix[row, :])
                row_column_index = row
        for column in range(0, dimension):
            if numpy.count_nonzero(matrix[:, column]) < max_zero:
                max_zero = numpy.count_nonzero(matrix[:, column])
                row_column_index = row + dimension

        determinant = 0
        if row_column_index < dimension:
            for column in range(0, dimension):
                if matrix[row_column_index, column] != 0:
                    determinant += (-1)**(row_column_index + column) * matrix[
                        row_column_index, column] * det_int(
                            numpy.delete(numpy.delete(matrix, row_column_index, axis=0), column, axis=1))

        else:
            row_column_index -= dimension
            for row in range(0, dimension):
                if matrix[row, row_column_index] != 0:
                    determinant += (-1)**(
                        row_column_index + row) * matrix[row, row_column_index] * det_int(
                            numpy.delete(numpy.delete(matrix, row_column_index, axis=1), row, axis=0))

        return int(determinant)



# divmod_mod calculates the 2-array div_rest such that numerator = 
# denominator*div_rest[0]+div_rest[1] and abs(div_rest[1]) is the
# smallest possible value.
def divmod_mod(numerator, denominator): 
    '\b'
    if ((not type(numerator) is int) or (not type(denominator) is int)) and ((not type(numerator) is numpy.int64) or (not type(denominator) is numpy.int64)):
        raise TypeError('Input must be of type int or numpy.int64')
    div_rest = numpy.array(numpy.divmod(numerator, denominator))
    if div_rest[1] > denominator / 2 and denominator > 0:
        div_rest[1] -= numpy.abs(denominator)
        div_rest[0] += 1
    if div_rest[1] < denominator / 2 and denominator < 0:
        div_rest[1] += numpy.abs(denominator)
        div_rest[0] += 1
    return div_rest

# Calculate the greatest common divisor of a numpy array of integers.
def gcd(array):
    '\b'
    if not type(array) is numpy.ndarray:
        raise TypeError('Input must be of type numpy.ndarray')
    if numpy.size(array) > 2:
        return gcd(numpy.append(array[:-2],gcd(array[-2:])))
    elif array[1] == 0:
        return abs(array[0])
    else:
        return gcd(numpy.array([array[1], array[0] % array[1]]))


def numpy2latex(matrix,_print=False):
    """Make numpy array LaTeX friendly.
    
    Parameters
    ----------
    matrix : numpy.array
        Array that will be written LaTeX friendly. 
    det_value : bool, optional
        If true, print the output in terminal. Otherwise return as a string.
    
    Returns
    -------
    output : str
        If _print is set to 'False' the function returns a string that is LaTeX friendly when printed. 
    
    Notes
    -----
    The output can be used together with some LaTeX environments, e.g.
    \\begin{pmatrix}
        [output]
    \\end{pmatrix}
    or
    \\begin{array}
        [output]
    \\end{array}
    
    Examples
    --------
    >>> numpy2latex(numpy.array([[4,-3],[5,2],[-8,5]]))
    4 & -3 \\\\\\\\\\n5 & 2 \\\\\\\\\\n-8 & 5'
    
    >>> numpy2latex(numpy.array([[4,-3],[5,2],[-8,5]]),_print=True)
    4 & -3 \\
    5 & 2 \\
    -8 & 5
    
    >>> print(numpy2latex(numpy.array([[4,-3],[5,2],[-8,5]])))
    4 & -3 \\
    5 & 2 \\
    -8 & 5"""
    
    
    if not type(matrix) is numpy.ndarray:
        raise TypeError('Input must be of type numpy.ndarray')
    elif not type(_print) is bool:
        raise TypeError('_print must be of type bool')
    dimensions = numpy.array([numpy.size(matrix,axis=0),numpy.size(matrix,axis=1)])
    output = ''
    for row in range(0,dimensions[0]):
        for column in range(0,dimensions[1]):
            output += str(matrix[row,column])
            if column < dimensions[1] - 1:
                output += ' & '
            elif row < dimensions[0] - 1:
                output += ' \\\\\n'
    if _print: # If true, print output to terminal.
        print(output)
        return
    else: # If false, return output.
        return output


# matrix_gen outputs a random matrix with requested value of the determinant.
def matrix_gen(dimension = 2, det_value = 1, lower_bound = -9, upper_bound = 10, rdn_prm = 0, attempts=200):

# In this function a matrix of specified dimension is requested. First, the rows [2:dimension] are randomized. 
# Then the possible values first row is calculated by solving the diophantine equation

    # a_1*c_1+a_2*c_2+...+a_dimension*c_dimension = det_value.

# where c_1,...,c_dimension are the cofactors of the first row of the matrix. 
# The diophantine equation is solved by substuting the variables with new variables until the 
# diophantine equation has only two unknown variabes. The program always try to
# reduce the term with largest cofactor (in absolute value).

  # Example: assume that the diophantine equation is calculated as

    # 5a_1 + 7a_2 + 8a_3 = 1

  # Then make the following substitutions: (start with reducing 8 in the third term)

    # a_2 = -a_3 + b_1 => 5a_1 +7b_1+a_3 = 1,
    # a_1 = -b_1 + b_2 => 5b_2 +2b_1 + a_3 = 1,
    # b_1 = -2b_2 + b_3 => b_2 + 2b_3 + a_3 = 1,
    # b_2 = -2b_3 + b_4 => b_4 + a_3 = 1,
    # => b_4 + a_3 = 1.
  
  # That is, we have a modified and lot simpler diophantine equation. 
  # Note that this shows that the original diophantine equation is solvable.
  # Moving everything to the left hand side we obtain the augmented matrix
  # [[0,1,1,1,0,0,0,0],
  #  [1,0,0,1,-1,0,0,0],
  #  [0,0,0,1,2,-1,0,0],
  #  [0,0,0,0,1,2,-1,0]
  #  [0,0,1,0,0,0,1,-1]
  # where the columns represent the variables
  # [a_1,a_2,a_3,b_1,b_2,b_3,b_4,constant]
  # (observe that in this function, every row is implicitly assumed to be equal to 0).

  # Solving for a_1,a_2,a_3 depending on the parameters b_3 and b_4 we obtain
  # all possible solutions to the diophantine equation.

  
# Then the function finalizes by calculating possible solutions for
# a_1,...a_dimension within the given bounds. To speed up the calculation the 
# function tries to write as many unknowns as possible depending on only one
# parameter. This is done in Part 4 by column-wise elimination. Also the user can choose to randomize some variable (by assigning
# rdn_prm a positive integer), to reduce the number of calculation but to the cost
# of less randomness of the output matrix.

    """Randomize a matrix with the determinant value as parameter.
    
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
    This can be used for e.g. teachers in linear algebra who want to create system of equations exercises 
    that are easy to solve by hand and possibly where fractions are avoided 
    (if det_value is chosen to be \u00B11).
    
    When the dimension is 2 or 3 the difference between lower_bound and upper_bound has to be at
    least 3 (except if lower_bound <= -1 and upper_bound >=1). This is to ensure that the problem
    is solvable. Otherwise the difference between lower_bound and upper_bound has to be at least 2.
    
    If the dimension is set to 7 or higher, it is recommended to set a few random parameters to
    speed up the calculcations. However, the randomness of the entries will decrease. The number
    of attemps is only used if there are randomized parameters set.

    Examples
    --------
    >>> matrix_gen()
    array([[ 9, -1],
       [ 1,  0]])
       
    Specify dimension:
    
    >>> matrix_gen(5)
    array([[ 9,  5,  0, -3, -3],
           [-1,  3,  1,  3,  3],
           [-1,  8, -2,  4,  4],
           [-6, -9, -4, -6, -5],
           [-6,  1,  8, -4,  2]])

    >>> matrix_gen(dimension=3)
    array([[ 1, -3,  5],
           [-1,  2, -1],
           [-3,  3,  8]])
           
    Specify determinant value:
    
    >>> matrix_gen(det_value=3)
    array([[2, 1],
           [7, 5]])

    >>> matrix_gen(dimension=4,det_value=3)
    array([[ 4, -4,  9,  3],
           [ 3, -7,  7, -6],
           [ 6,  2, -2,  3],
           [-1, -6,  5, -7]])


    >>> matrix_gen(3,-2)
    array([[ 8, -8,  9],
           [-2, -4,  8],
           [-9, -1,  7]])
    Set bounds of entries between -4 and 5:
    
    >>> matrix_gen(dimension=4,lower_bound=-4,upper_bound=6)
    array([[ 0, -2, -4, -1],
           [ 5,  0,  2,  3],
           [-3,  5,  5, -4],
           [ 5,  1,  2,  1]])
    
    Set the number of random paramters to speed up calculations if the number of dimesions is large:
    
    >>> matrix_gen(dimension=8,rdn_prm=3)
    array([[-3,  8, -6, -4, -5,  9,  0,  2],
           [-8, -1, -9, -5,  5, -8,  9,  9],
           [-3, -7,  3, -6, -4,  9, -6, -4],
           [ 3, -3,  3,  6, -3,  2,  0,  4],
           [ 2, -6,  0, -4,  2, -1,  7, -2],
           [-7,  2, -3,  9,  8, -2,  7, -1],
           [-8, -4,  4,  0,  3,  1,  1, -9],
           [ 8, -7, -3, -5,  5, -2, -3,  2]])
    
    Set number of attemps:
    
    >>> matrix_gen(dimension=6,rdn_prm=3,attempts=100)
    array([[-3,  6, -5,  2,  6, -3],
           [ 3, -9, -9,  8,  4,  4],
           [-8, -7,  6,  9, -1, -7],
           [ 4,  2,  0,  3,  2,  7],
           [ 0,  3, -4,  3,  9, -4],
           [ 1,  6,  6,  7,  7,  2]])"""


    if not type(dimension) is int:
        raise TypeError('Only integers are allowed for dimension')
    if dimension <= 0: # Take care of the special cases
        return numpy.array([[]])
    elif dimension == 1 and lower_bound <= det_value and det_value < upper_bound:
        return numpy.array([[det_value]])
    elif dimension == 1: 
        raise ValueError('det_value is outside the bounds!')
    if not type(det_value) is int:
        raise TypeError('det_value is of invalid datatype!')
    if not type(rdn_prm) is int or rdn_prm < 0:
        rdn_prm = 0
    if not type(attempts) is int or attempts <= 0:
        attempts = 200
    if not type(lower_bound) is int:
        raise ValueError('Only integers are allowed for lower_bound')
    if not type(upper_bound) is int:
        raise ValueError('Only integers are allowed for upper_bound')


    if lower_bound >= upper_bound - 1:
        raise ValueError('the difference between lower_bound and upper_bound must be at least 2!')
    elif dimension <= 3 and lower_bound >= upper_bound-2 and (lower_bound >= 2 or upper_bound <=-1):
        raise ValueError('the values of lower_bound and upper_bound are too narrowly chosen!')

    # If rows are swapped in the end, the sign of the determinant changes.
    rdn_row = numpy.random.randint(0,dimension) 
    if rdn_row != 0:
        det_value = -det_value


    # If parameters is randomized below, choose how many attempts before restarting the function.
    sol_attempts = attempts
    while attempts <= sol_attempts:
        sol_attempts = 0
        sol_exists = False
        # sol_exists sets to true if the diophantine equation is solvable
        while sol_exists == False:
            

            # Part 1 - Generate row 2-n and calculate cofactors of row 1
            
            

            cofactors = numpy.zeros(dimension,int) # cofactors of row 1
            matrix_generation_attempts = 0
            while matrix_generation_attempts <= 10 and numpy.count_nonzero(cofactors) == 0: 
                # Make sure not all cofactors are 0.
                matrix_red = numpy.random.randint(lower_bound, upper_bound, [dimension - 1, dimension]) 
                # Randomizes rows [2: dimension]
    
                for column in range(0, dimension):
            
                    # Calculate the cofactors of the first row
                   
                    submatrix = numpy.delete(matrix_red, column, axis=1)
                    cofactors[column] = numpy.round((-1)**column * det_int(submatrix))

                if det_value == 0:
                    break
                matrix_generation_attempts += 1
                
            if numpy.count_nonzero(cofactors) == 0 and det_value != 0:
                # Check so that there is a solution to the diophantine equation.
                raise ValueError('You were extremely unlucky! Try again!')
            
            

            # Part 2 - Generate a system of equations describing the diophantine equation 
            # generated by cofactor expansion of the unknown row 1

            # We treat the zero cofactors separately and reduce the dimension considered to the
            # number of non-zero cofactors.
            zero_cofactor = (cofactors == 0)
            _dim = numpy.count_nonzero(numpy.invert(zero_cofactor))

    
            
            nonzero_variables = numpy.count_nonzero(cofactors)
        
            cofactors = cofactors[numpy.invert(zero_cofactor)] # Set new cofactors to non-zero cofactors
            abs_cofactors = numpy.abs(cofactors) # To compare the size of the cofactors

            if _dim > 1:
        
                order = numpy.flip(numpy.argsort(abs_cofactors), axis=0)
    
        
                tot_rows = 10
                sys_of_eq = numpy.zeros([tot_rows, tot_rows+_dim+1], int)
        
                row_counter = 0
    
        
                coeff_enumeration = numpy.arange(_dim) # Keep track of the unknowns and the
                # defined parameters
        
                coeff_geq_2 = numpy.size(cofactors[numpy.abs(cofactors) > 1]) # Calculates which
                # cofactors that are >= 2.
                while coeff_geq_2 > 1 or nonzero_variables > 2: # Reduce diophantine equation 
                    # there is at most one cofactor and the number of cofactors (with the 
                    # modified diophantine equation) is at most 2.
                    
    
                    if row_counter >= tot_rows - 3:
                        tot_rows += 10
                        sys_of_eq_new = numpy.zeros([tot_rows, tot_rows+_dim+1], int)
                        sys_of_eq_new[0:tot_rows - 10, 0:tot_rows+_dim-9] = sys_of_eq
                        sys_of_eq = sys_of_eq_new 
                      
                    div_rest = divmod_mod(cofactors[order[0]],cofactors[order[1]])
        
                    sys_of_eq[row_counter, coeff_enumeration[order[1]]] = 1    
                    sys_of_eq[row_counter, row_counter + _dim] = -1
                    sys_of_eq[row_counter, coeff_enumeration[order[0]]] = div_rest[0]
        
                    cofactors[order[0]] = div_rest[1]
                    abs_cofactors = numpy.abs(cofactors)
                    coeff_enumeration[order[1]] = _dim + row_counter

        
                    order = numpy.flip(numpy.argsort(abs_cofactors), axis=0)
                    nonzero_variables = numpy.count_nonzero(cofactors)
        
                    coeff_geq_2 = numpy.size(cofactors[numpy.abs(cofactors) > 1])
                    row_counter += 1

                
                final_equation = numpy.concatenate((cofactors, numpy.array([-det_value])))
                final_equation = numpy.array(final_equation/gcd(final_equation),int)

                if numpy.count_nonzero(final_equation) >= 3 or final_equation[-1] % final_equation[order[0]] == 0: # check if solution exists. This can happen if there are 
                    # either >= 2 cofactors left (since only one cofactors can have absolute 
                    # value > 1, gcd of the coefficients has to be 1) or if there is 1 
                    # coefficients which divides the right hand side.
                    sol_exists = True
            elif _dim == 1 and det_value % cofactors[0] == 0: # Treats the case when only one 
                # cofactor is non-zero.
                solution = numpy.zeros(dimension, int)
                solution[numpy.invert(zero_cofactor)] = int(det_value / cofactors[0])    
                solution[zero_cofactor] = numpy.random.randint(lower_bound, upper_bound, dimension - _dim)
        
                matrix = numpy.concatenate(([solution], matrix_red))
                matrix[[0,rdn_row],:] = matrix[[rdn_row,0],:]
                return matrix
            elif _dim == 0: # E.g. if one randomized row is zero.
        
                solution = numpy.random.randint(lower_bound, upper_bound, dimension - _dim)
        
                matrix = numpy.concatenate(([solution], matrix_red))
                return matrix
        

        while row_counter < _dim - 1: # Makes sure every unknown variable is written as function 
            # of a parameter, in case the system of equation contains too few rows.
            sys_of_eq[row_counter, row_counter] = 1
            sys_of_eq[row_counter, row_counter + _dim] = -1
            row_counter += 1

        # Adding final equation the system of equations
        row_counter += 1
        
        sys_of_eq[row_counter - 1, row_counter + _dim - 1] = final_equation[-1]
        sys_of_eq[row_counter - 1, coeff_enumeration] = final_equation[:-1]
        


        # Part 3 - Solve for the unknown variables as functions of appropriate parameters. 
        # This is done by Gauss elimination. If the number of unknown variables is n, 
        # then the number of parameters should be n-1. Observe that row_counter may increase.
        column = 0
        while column < row_counter: # Go through all columns for all unknown variables.
            row = column
    
        
            while row < row_counter:
                # Set a 1 in the position [row,row] if possible and use this to eliminate
                # the other entries in the row.
                if sys_of_eq[row, column] == 1: 
                    sys_of_eq[[column, row], :] = sys_of_eq[[row, column], :]
                    break
                elif sys_of_eq[row, column] == -1:
                    sys_of_eq[row, :] = -sys_of_eq[row, :]
                    sys_of_eq[[column, row], :] = sys_of_eq[[row, column], :]
                    break
                elif row == row_counter - 1: # In case there is no 1 or -1 in use in the column, 
                    # add a row and a parameter in the system of equations.
                    if row_counter >= tot_rows - 4:
                        tot_rows += 10
                        sys_of_eq_new = numpy.zeros([tot_rows, tot_rows+_dim+1], int)
                        sys_of_eq_new[0:tot_rows - 10, 0:tot_rows+_dim - 9] = sys_of_eq
                        sys_of_eq = sys_of_eq_new
        
                    sys_of_eq[:, [row_counter + _dim - 1, row_counter + _dim ]] = sys_of_eq[:,[row_counter + _dim , row_counter + _dim - 1]]

                    sys_of_eq[[column, row_counter],:] = sys_of_eq[[row_counter, column],:]
                    sys_of_eq[column, column] = 1
                    sys_of_eq[column, _dim + row_counter - 1] = -1
        
                    row_counter += 1
                    break
                row += 1
        
            for row in numpy.delete(numpy.arange(0, row_counter), column): # Use the 1 in 
                # [row,row] to eliminate the other entries in the column.
                sys_of_eq[row, :] = sys_of_eq[row, :] - sys_of_eq[row, column] * sys_of_eq[column, :]

            column += 1
       

        tot_rows = row_counter 
        sys_of_eq = sys_of_eq[0:_dim,row_counter:row_counter + _dim] # Remove unneccesary rows and
        # column with 0 now that the system of equations will not be expanded any further.

        # Part 4 - Try to make the unknown variables dependent on one parameter
        # only (if possible).
        # This is done by column elimination in the parameter columns.
        # Observe that no multiplication of a an interger with a column is allowed,
        # since the system of equations might loose interger solutions.
      
        row_order = numpy.argsort(numpy.count_nonzero(sys_of_eq[:, _dim: _dim-1], axis=1))

        for counter in numpy.arange(0, _dim-1): 
            row = row_order[counter] # Goes through rows in the correct order.
            non_zero_entries = (sys_of_eq[row,counter: _dim-1 ] != 0)
        
            non_zero_entries_count = numpy.count_nonzero(non_zero_entries)
        
            while non_zero_entries_count > 1:
                column_order = numpy.argsort(numpy.abs(sys_of_eq[row,counter: _dim-1 ]))+counter
                column_order = column_order[non_zero_entries[column_order-counter]]

        
                div_rest = divmod_mod(sys_of_eq[row,column_order[non_zero_entries_count - 1]],sys_of_eq[row,column_order[non_zero_entries_count - 2]])
        
                sys_of_eq[:,column_order[non_zero_entries_count - 1]] = sys_of_eq[:,column_order[non_zero_entries_count - 1]] - div_rest[0] * sys_of_eq[:,column_order[non_zero_entries_count - 2]]
                 
                non_zero_entries = (sys_of_eq[row,counter: _dim-1 ] != 0)
                non_zero_entries_count = numpy.count_nonzero(non_zero_entries)
        
            sys_of_eq[:,[counter,int(numpy.nonzero(non_zero_entries)[0])+counter]] = sys_of_eq[:,[int(numpy.nonzero(non_zero_entries)[0])+counter,counter]]

            
            if 0 < counter and counter < _dim-1:
                for column in numpy.arange(0,counter):

                    div_rest = divmod_mod(sys_of_eq[row, column],sys_of_eq[row, counter])
                    sys_of_eq[:,column] = sys_of_eq[:,column] - div_rest[0] * sys_of_eq[:,counter]

        
        # Part 5 - Determine bounds for the parameters
        
        parameters_bounds = numpy.zeros([_dim-1,2],int)
        control_rows=numpy.array([_dim-1]) # Keeps track of the unknown variables
        # that are dependent 
        # of more than one parameter
        for parameter_counter in range(0,_dim-1):
            previous_parameter_sum = numpy.zeros(2,int)
            if numpy.count_nonzero(sys_of_eq[row_order[parameter_counter],:parameter_counter]) != 0:
                control_rows = numpy.append(control_rows,row_order[parameter_counter])
                for previous_parameter in range(0,parameter_counter): # Calculates neccesary 
                    # bounds for the parameters
                    
                    if sys_of_eq[row_order[parameter_counter],previous_parameter] < 0:
                        previous_parameter_sum[0] += sys_of_eq[row_order[parameter_counter],previous_parameter]*parameters_bounds[previous_parameter,0]
                        previous_parameter_sum[1] += sys_of_eq[row_order[parameter_counter],previous_parameter]*parameters_bounds[previous_parameter,1]
                    elif sys_of_eq[row_order[parameter_counter],previous_parameter] > 0:
                        previous_parameter_sum[0] += sys_of_eq[row_order[parameter_counter],previous_parameter]*parameters_bounds[previous_parameter,1]
                        previous_parameter_sum[1] += sys_of_eq[row_order[parameter_counter],previous_parameter]*parameters_bounds[previous_parameter,0]
                
            if sys_of_eq[row_order[parameter_counter],parameter_counter] > 0:
                parameters_bounds[parameter_counter,0] = numpy.ceil((-upper_bound+1 - sys_of_eq[row_order[parameter_counter],-1]-previous_parameter_sum[0])/sys_of_eq[row_order[parameter_counter],parameter_counter])
                parameters_bounds[parameter_counter,1] = numpy.floor((-lower_bound - sys_of_eq[row_order[parameter_counter],-1]-previous_parameter_sum[1])/sys_of_eq[row_order[parameter_counter],parameter_counter]) 
            elif sys_of_eq[row_order[parameter_counter],parameter_counter] < 0:
                parameters_bounds[parameter_counter,0] = numpy.ceil((-lower_bound - sys_of_eq[row_order[parameter_counter],-1]-previous_parameter_sum[1])/sys_of_eq[row_order[parameter_counter],parameter_counter])
                parameters_bounds[parameter_counter,1] = numpy.floor((-upper_bound+1 - sys_of_eq[row_order[parameter_counter],-1]-previous_parameter_sum[0])/sys_of_eq[row_order[parameter_counter],parameter_counter]) 
        control_rows = numpy.sort(control_rows)
        
        
        solutions_size = 100
        solutions = numpy.zeros([solutions_size, _dim], int)
        sol_counter = 0
        
        while sol_counter == 0:

            # Try random parameters
            b = numpy.append(parameters_bounds[:,0], [1])
            rdn_prm = min(rdn_prm,_dim - numpy.size(control_rows))
            if rdn_prm == 0:
                randomised_parameters = numpy.array([])
                non_randomised_parameters = numpy.arange(0,_dim-1)
            else:
                randomised_parameters = numpy.random.choice(numpy.delete(numpy.arange(0,_dim-1),control_rows[0:-1]),rdn_prm,replace=False) # Chooses variables from the set of 
                # unknowns depending on several parameters.
                for randomised_parameter_counter in randomised_parameters:
                    b[randomised_parameter_counter] = numpy.random.randint(parameters_bounds[randomised_parameter_counter,0],parameters_bounds[randomised_parameter_counter,1]+1)
                    non_randomised_parameters = numpy.delete(numpy.arange(0,_dim-1),randomised_parameter_counter)

            
    
            sol_attempts += 1

            if sol_attempts >= attempts: # Restart function and generate new random rows if too
                # many attemps are done.
                # print('Maximum number of attempts reached, restarting function...')
                break
            
            while b[non_randomised_parameters[0]] <= parameters_bounds[non_randomised_parameters[0],1]:
                sol_test = True
                for row in control_rows:
                    
                    a = -sys_of_eq[row, :] @ b

                    if upper_bound-1 < a or a < lower_bound: # Test if the calculated solution 
                        # is within bounds.
                        sol_test = False
        
                if sol_test:
                    solutions[sol_counter, :] = -sys_of_eq @ b
                    sol_counter += 1

                    
                    if sol_counter == solutions_size:
                        solutions_size += 100
                        solutions = numpy.append(solutions,numpy.zeros([100, _dim], int),axis=0)
        
                counter = numpy.size(non_randomised_parameters) - 1
                while b[non_randomised_parameters[counter]] >= parameters_bounds[non_randomised_parameters[counter],1] and counter != 0:
                    b[non_randomised_parameters[counter]] = parameters_bounds[non_randomised_parameters[counter],0]
                    counter -= 1
        
                b[non_randomised_parameters[counter]] += 1
            
      
        # Part 6 - Choose one solution and concatenate it with the rest of the randomized
        # matrix rows.
        
        solutions = solutions[0:sol_counter, :]
        
        if sol_counter != 0:
            sol_gen = numpy.random.randint(0, sol_counter)
            sol_exists = True
            solution = numpy.zeros([1,dimension],int)
            solution[0,zero_cofactor] = numpy.random.randint(lower_bound, upper_bound, dimension - _dim)
            solution[0,numpy.invert(zero_cofactor)] = solutions[sol_gen:sol_gen + 1, :] 

            matrix = numpy.concatenate((solution, matrix_red))
        
    
    matrix[[0,rdn_row],:] = matrix[[rdn_row,0],:]
    
    return matrix

if __name__ == '__main__':
    import argparse
    import sys
    
    _epilog='''examples:
  matrix_rdn_det.py 
                        Outputs a matrix of dimension 2 with determinant 1 and entries between -9 and 9.
                        Example output:
                          9 & -1 \\\\
                          1 & 0
  matrix_rdn_det.py 5
                        Outputs a matrix of dimension 3 with determinant 1 and entries between -9 and 9.
                        Example output:
                          -2 & 3 & 5 & 7 & 7 \\\\
                          -2 & 2 & 6 & -4 & -7 \\\\
                          4 & -4 & -5 & 5 & 4 \\\\
                          -9 & -9 & 1 & 5 & 0 \\\\
                          -9 & -7 & 4 & 3 & -3
  matrix_rdn_det.py 5 -4
                        Outputs a matrix of dimension 5 with determinant -4 and entries between -9 and 9.
                        Example output:
                          6 & 3 & 6 & 4 & -8 \\\\
                          8 & -5 & 5 & -6 & 5 \\\\
                          9 & -8 & -7 & -5 & 5 \\\\
                          0 & -1 & -2 & 3 & -8 \\\\
                          -2 & -6 & -1 & -1 & -7
  matrix_rdn_det.py 5 6 -3 14
                        Outputs a matrix of dimension 5 with determinant 6 and entries between -3 and 13.
                        Example output:
                          11 & 1 & 4 & 3 & -1 \\\\
                          3 & -2 & -1 & 2 & 13 \\\\
                          0 & 4 & 4 & 8 & 10 \\\\
                          -2 & 6 & 3 & 11 & 8 \\\\
                          -3 & 3 & 11 & 1 & 11
  matrix_rdn_det.py 7 6 -3 14 2 300
                        Outputs a matrix of dimension 7 with determinant 6 and entries between -3 and 13. The number
                        of randomization of 2 parameters can make the calculations faster. The parameters are 
                        randomized 300 times before the called function restarts. It is recommended to set randomized 
                        parameters when the dimension is 7 or larger.
                        Example output:
                          8 & 0 & 7 & 11 & 9 & 5 & 7 \\\\
                          1 & 12 & 12 & 11 & 3 & 10 & 4 \\\\
                          -2 & 10 & -1 & 12 & 2 & 10 & 5 \\\\
                          2 & 1 & -3 & 0 & 5 & 1 & -1 \\\\
                          -3 & 11 & -1 & -1 & -3 & 8 & 5 \\\\
                          9 & 4 & 6 & -2 & 9 & 6 & -3 \\\\
                          -1 & 7 & 13 & 5 & 6 & -3 & 12'''
    parser = argparse.ArgumentParser(description='''                        Randomize a matrix with the determinant value as a parameter. The output is LaTeX compatible.
    
                        This can be used for e.g. teachers in linear algebra who want to create system of equations 
                        exercises that are easy to solve by hand and possibly where fractions are avoided 
                        (if det_value is chosen to be \u00B11).
                        
                        When the dimension is 2 or 3 the difference between lower_bound and upper_bound has to be at
                        least 3 (except if lower_bound <= -1 and upper_bound >=1). This is to ensure that the problem
                        is solvable. Otherwise the difference between lower_bound and upper_bound has to be at least 2.

                        If the dimension is set to 7 or higher, it is recommended to set a few random parameters to
                        speed up the calculcations. However, the randomness of the entries will decrease. The number
                        of attemps is only used if there are randomized parameters set.
    
                        The standard output can be used together with some LaTeX environments, e.g.
                        \\begin{pmatrix}
                            [output]
                        \\end{pmatrix}
                        or
                        \\begin{array}
                            [output]
                        \\end{array}
                        
                        https://github.com/andis854/matrix_rdn_det
                        Report bugs to andis854@outlook.com''', formatter_class=argparse.RawTextHelpFormatter, epilog=_epilog)

    parser.add_argument('parameters', nargs='*', help='''Set the parameters [dimension, det_value, lower_bound, upper_bound, rdn_prm, attempts]. 
          dimension
            Dimension of the matrix. If set to a non-positive integer the function returns an 
            empty matrix. Default is 2.
          det_value
            Value of the determinant of the matrix. Must be an integer. Default is 1.
          lower_bound
            Sets the lower bound of the entries in the matrix to lower_bound. Default is -9.
          upper_bound
            Sets the upper bound of the entries in the matrix to upper_bound-1. Default is 10.
          rdn_prm
            Sets the number of randomized parameters in the function. This can be used to speed
            up the calculations if the determant value is large (e.g. 7 or larger). If rdm_prm is set
            out of range, this is automatically adjusted. Default value is 0.
          attempts
            Sets the number of attempts to randomized parameters in the function. This is used to
            restart the function if the calculations are taking too long if the determinant value is
            large (e.g. 7 or larger). Default value is 200.
    ''')

    args=parser.parse_args()

    arguments = numpy.array([2,1,-9,10,0,200])
    

    arguments[0:len(args.parameters)] = args.parameters 


    a = matrix_gen(int(arguments[0]),int(arguments[1]),int(arguments[2]),int(arguments[3]),int(arguments[4]),int(arguments[5]))
    sys.stdout.write(numpy2latex(a,_print=False)+'\n')

