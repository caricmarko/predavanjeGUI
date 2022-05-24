a = [3,100,101,2,11,17,19]
for i in range(2):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            (a[i],a[j])=(a[j],a[i])

print(a)
print(a[1])