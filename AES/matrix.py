def bytes2matrix(text):
    """ Converts a N*N-byte array into a NxN matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a NxN matrix into a N*N-byte array.  """
    text=''
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            text += chr(matrix[i][j])
    return text

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))

# flag: crypto{inmatrix}