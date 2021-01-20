# dic = {}
# a = 3
# b = 4
# c = str(a) + str(b)
# d = str(a) 
# dic[c] = 2
# dic[d] = 3
# for x in dic.values():
#     print(x)
# ls = []
# if ls:
#     print(444)
# else:
#     print(222)   

# a = []
# a.append([1,2])
# a.append([3,4])
# b = a.pop(0)
# print(b)
# print(a)
# 
import operator
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(type(sorted_d[0][0]))