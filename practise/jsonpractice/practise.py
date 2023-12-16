# print( "Twinkle, twinkle, little star,\n \tHow I wonder what you are! \n\t\tUp above the world so high,\n\t\tLike a diamond in the sky. Twinkle, twinkle, little star, \n\tHow I wonder what you are")

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# l={}
# x=list(d.values())
# print(x)
# for key,val in d.items():
#     l.setdefault(val,key)
# print(l)
    
# def f(n):
#     a=n
#     b=str(n)+str(n)
#     c=str(n)+str(n)+str(n)
#     return a+int(b)+int(c)
# print(f(5))

# def vols(r):
#     return (4/3)*(22/7)*pow(r,3)

# print(vols(6))

# l=[1,2,3,4,5,6]

# for x in l:
#     print(x)

# l={}
# n=5
# for x in range(5+1):
#     l[x]=x*x
# print(l)

# l=[1,2,"id",4]
# k=[4,5,3,False]
# d={}
# for x in range(len(l)):
#     d[l[x]]=k[x]
# print(d)

z=[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
y=[]
for x in z:
    f=(list(x.values()))
    y.append(list(f[0].keys()))
q=[]
for x1 in y:
    q.append(x1[0])
    
print(q)



