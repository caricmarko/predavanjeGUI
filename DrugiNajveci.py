a = [3,100,101,2,11,17,19]
print(a)
for i in range(2):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            (a[i],a[j])=(a[j],a[i])

print(a)
print(a[0])

a =[[3,5,7,8,9,3,7],[1,2,3,4,5,2,8]]
print(len(a))
print(len(a[0]))
print(a[1])
#zamena mesta vrsta 
for i in range(len(a[0])):
    (a[0][i],a[1][i])=(a[1][i],a[0][i])

print(a)
print(sum(a[0]))
#i isto moze
for i in range(len(a)):
    (a[0],a[1])=(a[1],a[0])
print(a)
print(sum(a[1]))
print(sum(a[0]) + sum(a[1]))


