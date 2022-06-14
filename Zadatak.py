a = [-5,-3,0,1,4,5]
poc = 0 #indeks levo
kraj = len(a)-1 #indeks desno
print(kraj)
novi = []
while(poc<=kraj):
    if(abs(a[poc])>abs(a[kraj])):
        novi.append(a[poc]*a[poc])
        poc+=1
    else:
        novi.append(a[kraj]*a[kraj])
        kraj-=1
print(novi)
print(novi[::-1])
for i in range(len(novi)//2):
    (novi[i],novi[-1-i])=(novi[-1-i],novi[i])
print(novi)

