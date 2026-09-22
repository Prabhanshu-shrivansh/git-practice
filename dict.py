#frequency of the numbers
# numbers = [1, 2, 2, 3, 1, 4, 2, 3, 3]
# dict={}
# for i in numbers:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)

#frequency of chacater
# text="Prabhanshu"
# dict={}
# for i in text:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)

# find the key with maximum value
# dict={'P': 1, 'r': 1, 'a': 2, 'b': 1, 'h': 6, 'n': 1, 's': 4, 'u': 1}
# high=0
# high_name=""
# for i in dict:
#     if dict[i]>high:
#         high=dict[i]
#         high_name=i
# print(high)
# print(high_name)

#find duplicate value in dict
# dict={'P': 1, 'r': 2, 'a': 2, 'b': 1, 'h': 5, 'n': 6, 's': 1, 'u': 3}
# seen=[]
# duplicate=[]
# for value in dict.values():
#     if value not in seen:
#         seen.append(value)
#     elif value not in duplicate:
#         duplicate.append(value)
# print(seen)
# print(duplicate)

# import copy

# a = [[1, 2], [3, 4]]

# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(b)
# print(c)

#remove duplicate
# data={"a":10,"b":20,"c":30,"d":30,"e":20}
# new={}
# for i in data:
#     if data[i] not in new.values():
#         new[i]=data[i]
# print(new)

#merge two dict 
# dict1 = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }

# dict2 = {
#     "d": 40,
#     "e": 50,
#     "f": 60
# }
# dict3={}
# for i in dict1:
#     dict3[i]=dict1[i]
# for i in dict2:
#         dict3[i]=dict2[i]
        
# print(dict3)

#common keys of two dict
# dict1 = {
#     "a": 10,
#     "b": 20,
#     "c": 30,
#     "d": 40
# }

# dict2 = {
#     "c": 50,
#     "d": 60,
#     "e": 70
# }
# result=[]
# for i in dict1:
#     if i in dict2:
#         result.append(i)

# print(result)


#total of value
# marks = {
#     "Rahul": 85,
#     "Amit": 92,
#     "Priya": 78,
#     "Neha": 95
# }
# total=0
# for i in marks.values():
#     total+=i
# print(total)

#find the maximum value in dict
# marks = {
#     "Rahul": 85,
#     "Amit": 92,
#     "Priya": 78,
#     "Neha": 95
# }
# high=0
# for i in marks:
#    if  marks[i]>high:
#        high=marks[i]
# print(high)

#merge list into key values pair
# keys=["name","age","city","job"]
# values=["jay",21,"indore","python developer"]
# result={}
# for i in range(len(keys)):
#     result[keys[i]]= values[i]
# print(result)