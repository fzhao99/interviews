def rotate_matrix(matrix):
    layers = len(matrix) // 2

    for layer in range(layers):
        start = layer
        finish = len(matrix) - 1 - layer

        for i in range(finish - start):
            #capture top
            top = matrix[layer][i]

            #left - > top
            matrix[layer][i] = matrix[-i-1][layer]

            #bottom -> left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            #right -> bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
             #top - > right
             matrix[i][-layer-1] = top

        return matrix
