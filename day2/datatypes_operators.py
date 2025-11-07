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

l1 = ["a","b","c","d","c"]
l2 = ["1","2"]
l1.append(3)
l1.extend(range(4,2,-2))
l1.remove("a")
print(l1.index("c"))
print(l1)
print(l1[1:4:2])