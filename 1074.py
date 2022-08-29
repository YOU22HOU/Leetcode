import collections

matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 2

#变换矩阵, 求每行子矩阵的和,得到新矩阵
for i in range(len(matrix)):
    for j in range(len(matrix[i])-1):
        matrix[i][j+1] += matrix[i][j]

#print(matrix)

result = 0
for i in range(len(matrix)):
    #初始化prefix_sum
    prefix_sum = [0]*len(matrix[i])
    for j in range(i, len(matrix)):
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        for k in range(len(matrix[j])):
            prefix_sum[k] += matrix[j][k]
            #print(prefix_sum[k])
            if prefix_sum[k]-target in lookup:
                result += lookup[prefix_sum[k]-target]
            lookup[prefix_sum[k]] += 1
            print(lookup)
print(result)