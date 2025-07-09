a= input()
lis1= a.split('.')
counter= 0
lis= [int(d) for d in lis1]
for i in range(len(lis)):
    if lis[i] in range(0, 256):
        counter += 1
if counter == 4:
    print('ДА')
else:
    print('НЕТ') 
