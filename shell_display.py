from PIL import Image as I
import numpy as np
import os
import sys

HIGHT = min(os.get_terminal_size()) - 2
WEIGHT = HIGHT * 2
FILE_NAME = sys.argv[1]

def img_chars(mat: np.ndarray) -> str:
    chars = ''
    n_row, n_col, n = mat.shape
    fill = lambda r, g, b: '\x1b[48;2;%d;%d;%dm '%(r, g, b)
    for i in range(n_row):
        s = ''.join(fill(*mat[i, j]) for j in range(n_col))
        chars += s + '\x1b[0m\n'
    return chars[:-1]

img = I.open(FILE_NAME)
nimg = img.resize((WEIGHT, HIGHT), I.LANCZOS)
mat = np.array(nimg)
s = img_chars(mat)
print(s)
