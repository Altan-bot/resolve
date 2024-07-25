def get_matrix(n,m,value):
    matrix=[]
    for row in range(n):
        temp_list=[]
        for column in range(m):
            temp_list.append(value)
        matrix.append(temp_list)
    return matrix
result1=get_matrix(n=2,m=2,value=10)
result2=get_matrix(n=3,m=5,value=42)
result3=get_matrix(n=4,m=2,value=13)
print(result1)
print(result2)
print(result3)