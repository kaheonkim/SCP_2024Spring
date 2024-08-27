A = [1,2,[3,19,'D'],4,2.3,'c']

#print(len(A))


#print(A[2])

#print(A[2][1])
#print(A[3:5])



B = [1,2,4,2.3]
#print(max(B))
#print(min(B))
print(sum(B))





A = [1,2,3,4,2]
B = ['C','D',1.5, 3]


# A.append(6)
# A.remove(6)
# A.append(6)
# A.pop(5)

# A.reverse()

# A_ = sorted(A)
# A__ = sorted(A, reverse=True)

print(A+B)
print(3*A)
print(A*3)







def mean(p):
    sumation = sum(p)
    mean_val = sumation/len(p)
    return mean_val



A = ['C','D',1,3,5]

# for i in range(len(A)):
#     print(A[i])
    
    
    
for a in A:
    print(a)



A = [2,4,7,10,11]

sum_ = 0
for a in A:
    sum_ += a**2
print(sum_)


def find_max_ind(A):
    max_val = max(A)
    ind_list = []
    for i in range(len(A)):
        if A[i] == max_val:
            ind_list.append(i)
    return ind_list



def find_even(A):
    val_list = []
    ind_list = []
    
    for i in range(len(A)):
        if A[i]%2==0:
            val_list.append(A[i])
            ind_list.append(i)
    return val_list, ind_list