

def permute(a, l, r): 
    if l==r: 
        for i in range(n):
            print(a[i], end=' ')
        print(' ')
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] 



n = int(input('Enter count of words: '))
a = []

for i in range(n):
    a.insert(i, input('Enter word '+str(i+1)+': '))

permute(a, 0, n-1) 


input('Press any key to exit . . .')
















# import math
# import random

# n = int(input('Tedad kalamat ra moshakhas konid: '))
# words = []
# out = []


# for i in range(n):
#     words.insert(i, input('kalame '+str(i+1)+' ra vared konid: '))

# for i in range(math.factorial(n)):
#     out.insert(i, '')

# for i in range(math.factorial(n)):
#     out[i] = out[i]+words[i]





# for i in range(math.factorial(n)):
#     out.insert(i, '')

# for i in range(n):
#     x=0
#     for j in range(math.factorial(n-1)):
#         for k in range(n):
#             out[x]=out[x]+words[k]+' , '
#             x=x+1
#     words.insert(n, words[0])
#     words.remove(words[0])

# print('tedad halat ha: '+str(x))     

# for i in range(math.factorial(n)):
#     print(out[i])





# for i in range(n):
#     a=''
#     for i in range(n):
#         a = a + words[i]+' , '
#     print(a)
#     words.insert(n, words[0])
#     words.remove(words[0])

# words.reverse()
# for i in range(n):
#     a=''
#     for i in range(n):
#         a = a + words[i]+' , '
#     print(a)
#     words.insert(n, words[0])
#     words.remove(words[0])



# j=0
# for i in range(int(n)):
#     print(words[0+i]+' , '+words[1+i]+' , '+words[2+i])
#     print(words[0+i]+' , '+words[1+i+1]+' , '+words[2+i-1])
#     j=-2
