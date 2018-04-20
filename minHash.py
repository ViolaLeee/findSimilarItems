from numpy import *

# h1
def hash1(x):
    h1 = (2*x + 1) % 6
    return h1

# h2
def hash2(x):
    h2 = (3*x + 2) % 6
    return h2

# h3
def hash3(x):
    h3 = (5*x + 2) % 6
    return h3

# minhashing
def minHash(M,S,h1,h2,h3,sig):

    [rows,cols] = M.shape
    # signature matrix

    # signature initiate to infinite
    sig = full((3,4),float('inf'))
#    for row in range(3):
 #       sig.append([])
  #      for col in range(4):
   #         sig[row].append(float('inf'))

    # compute signature
    for i in range(rows):# for each column set
        for j in range(cols):
            if (S[i][j] == 1):
                if(h1[j] <= sig[0][i]):
                    sig[0][i] = h1[j]
                if(h2[j] <= sig[1][i]):
                    sig[1][i] = h2[j]
                if(h3[j] <= sig[2][i]):
                    sig[2][i] = h3[j]

    return sig
if __name__=="__main__":
    row = [0, 1, 2, 3, 4, 5]

    S = [[0, 0, 1, 0, 0, 1],
         [1, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0],
         [1, 0, 1, 0, 1, 0]]
    M = mat(S)
    Mtrans = transpose(M)
    h1 = []
    h2 = []
    h3 = []
    for i in row:
        h1.append(hash1(i))
        h2.append(hash2(i))
        h3.append(hash3(i))
    sig = []
    result = minHash(M,S,h1,h2,h3,sig)

    print(result)