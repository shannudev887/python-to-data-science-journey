# list = ['shannu','thing','sheep']
# for i in list:
#     for j in i:
#         if j == 'a':
#             print(i,'Contains a')
#         else:
#             continue

# strings

# s1 = "Shannu "
# s2 = ["good","1"]
# print(s1.upper())
# print(s1.lower())
# print(s1.strip())
# print(isinstance(s1.split(),list))
# print(type(s1.join(s2)))
# print(s1.replace('n','u'))

# l1 = ["a","b","c","d","c"]
# l2 = ["1","2"]
# l1.append(3)
# l1.extend(range(4,2,-2))
# l1.remove("a")
# print(l1.count(2))
# print(l1.index("c"))

# if l1.index("c"):
#     l1.pop(l1.index("c"))
# print(l1)
# print(l1[1:4:2])

# t1 = (1,2,3)
# print(t1[-3:-1:2])
# print(t1[2])
# print(t1.count(2))

# s1 = {1,2,3,4,5}
# s1.add(6)
# s1.update((6,9))
# s1.remove(2)
# s1.discard(10)
# s1.pop()
# s1.clear()
# print(isinstance(s1,set))
# print(s1)

# d1 = {}
# d1 = {1:2,2:3}
# d2 = dict([[1,"shannu"], [2,"top"]])
# d3 = dict(name="shannu",height = 6.0)
# for key,value in d1.items():
#     print(key,value) 
# print(type(d1))
x = 0
for i in  range(4):
    x =+ i
    
print(x)