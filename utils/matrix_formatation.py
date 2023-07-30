def format_matrix(matrix):
    '''Transform and format the frame's matrix in and long string.'''
    return '\n'.join([' '.join(row) for row in matrix])