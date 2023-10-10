matrix = [
    [1,2,3,4,5,6,-1],
    [2,3,1,7,9,6,1],
    [-1,-1,2,4,5,7,3],
    [-2,3,5,6,1,2,6]
]



def submatrix_avg(matrix, row_start, row_end, col_start, col_end):
    total = count = 0
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if matrix[i][j] >= 0:
                total += matrix[i][j]
                count += 1
    print("total: ", total)
    return total // count if count > 0 else 0

def sum_min(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = 10000

    for i in range(m-1):
        for j in range(n-1):
            print("i,j:", i,j)

            tl = submatrix_avg(matrix,0,i,0,j)
            tr = submatrix_avg(matrix, 0, i, j + 1, n - 1)
            dl = submatrix_avg(matrix,i+1,m-1,0,j)
            dr = submatrix_avg(matrix,i+1,m-1,j+1,n-1)
            #
            print(tl,tr,dl,dr)

            min_sub = min(tl,tr,dl,dr)
            max_sub = max(tl,tr,dl,dr)
            res = min(res,abs(min_sub-max_sub))
            print("diff: ", abs(min_sub-max_sub))
    return res

            # print("diff: ", abs(min_sub-max_sub))
# sum_min(matrix)
print("res:", sum_min(matrix))

def presum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    res = 10000

    presum_matrix = [[0]*n for _ in range(m)]
    count_non_zero = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            # if matrix[i][j]<0:
            #     matrix[i][j]=0
            above = presum_matrix[i - 1][j] if i - 1 >= 0 else 0
            left  =  presum_matrix[i][j-1] if j - 1 >= 0 else 0
            above_left = presum_matrix[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            presum_matrix[i][j] = matrix[i][j] + above + left - above_left if  matrix[i][j]>=0 else above + left - above_left

            above_c = count_non_zero[i - 1][j] if i - 1 >= 0 else 0
            left_c = count_non_zero[i][j - 1] if j - 1 >= 0 else 0

            above_left_c = count_non_zero[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            count_non_zero[i][j] = 1 + above_c + left_c - above_left_c if matrix[i][j]>=0 else above_c + left_c - above_left_c


    # print("count: ",count_non_zero)
    return presum_matrix,count_non_zero


# print(matrix)
presum,precount = presum(matrix)

def dp(presum,precount):
    res = 1000
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m-1):
        for j in range(n-1):
            print("dp: i,j: ",i,j)
            sbm1  = presum[i][j]
            sbm2  = presum[i][n-1] - presum[i][j]
            sbm3 = presum[m-1][j] - presum[i][j]
            sbm4 = presum[m-1][n-1]- presum[i][n-1]-presum[m-1][j]+presum[i][j]

            print(sbm1, sbm2, sbm3, sbm4)

            min_sub = min(sbm1, sbm2, sbm3, sbm4)
            max_sub = max(sbm1, sbm2, sbm3, sbm4)
            res = min(res, abs(min_sub - max_sub))
            # print("diff: ", abs(min_sub - max_sub))

            res = min(res, abs(min_sub - max_sub))
            print("diff: ", abs(min_sub - max_sub))
    return res




print("dp",dp(presum,precount))