def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1

        for i in range(first,last):
            matrix_top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i-1][layer]

            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            matrix[i][-layer-1] = top

        return matrix
