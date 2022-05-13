from operator import itemgetter
import itertools as it
from traceback import print_last

def subsets(A,k):
    return(list(it.combinations(A,k)))
    
    
def is_a_in_x(A, X):
  for i in range(len(X) - len(A) + 1):
    if A == X[i:i+len(A)]: return True
  return False


res1=[]
res2=[]

sum1=[]
sum2=[]


list_A = list(map(int, input().split(" ")))
list_B = list(map(int, input().split(" ")))


for i in range(1, len(list_A)+1):
    m = subsets(list_A, i)
    for items in m:
        res1.append(list(items))
for i in range(1, len(list_B)+1):
    m = subsets(list_B, i)
    for items in m:
        res2.append(list(items))    

res1 = sorted(res1, key=itemgetter(0))
result1=[]
for item in res1:
    if is_a_in_x(item, list_A):
        result1.append(item)


for r in result1:
    sum1.append(sum(r))
for r in res2:
    sum2.append(sum(r))
    

for i in sum1:
    if i in sum2:
        print(result1[sum1.index(i)])
        print(res2[sum2.index(i)])
        break
    
    
print(0)    
