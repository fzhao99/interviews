def rotate_matrix(matrix):

    for layer in range(len(matrix[0])):
        matrix_top = matrix[layer][layer][1:-1]
