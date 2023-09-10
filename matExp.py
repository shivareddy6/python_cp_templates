def matMult(mat1, mat2, mod):
    n1, m1 = len(mat1), len(mat1[0])
    n2, m2 = len(mat2), len(mat2[0])

    ans = [[0 for i in range(m2)] for j in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                ans[i][j] += mat1[i][k]*mat2[k][j]
                ans[i][j] %= mod

    return ans

def matExp(mat, k, mod):
    '''returns mat power of k with mod'''
    n,m = len(mat), len(mat[0])
    if k == 0:
        ans = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i == j:
                    ans[i][j] = 1
                else:
                    ans[i][j] = 0
        return ans
    
    if k%2 == 0:
        ans = matExp(matMult(mat, mat, mod), k//2, mod)
    else:
        ans = matMult(mat, matExp(mat, k-1, mod), mod)
    
    return ans