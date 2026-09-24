# #find the largest element
# numbers = [10, 5, 25, 8, 30, 15]
# large=numbers[0]
# for num in numbers:
#     if num>large:
#          large=num
# print(large)


# #find the smallest
# numbers = [10, 5, 25, 8, 30, 15]
# small=numbers[0]
# for num in numbers:
#     if num<small:
#          small=num
# print(small)

#second highest
# numbers = [10, 5, 25, 8, 30, 15]
# high = numbers[0]
# second = numbers[0]
# for i in numbers:
#     if i > high:
#         second = high
#         high = i
#     elif i > second and i != high:
#         second = i
# print(second)
  
#reverse the list      
# numbers = [1, 2, 3, 4, 5]
# lst=[]
# for i in range(len(numbers)-1,-1,-1):
#     lst.append(numbers[i])
# print(lst)

# #separate even odd
# numbers = [10, 15, 20, 33, 42, 55, 60, 71]
# even=[]
# odd=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

#remove duplicate
# numbers = [1, 2, 2, 3, 1, 4, 3, 5, 2]
# dup=[]
# for i in numbers:
#     if i not in dup:
#         dup.append(i)
# print(dup)


#remove duplicate
# numbers = [1, 2, 2, 3, 1, 4, 3, 5, 2]
# dup=[]
# element=[]
# for i in numbers:
#     if i not in dup:
#         dup.append(i)
#     elif i not in element:
#         element.append(i)

# print(element)

# frequency string and call keys with join
# numbers = "prabhanshu"
# freq={}
# for i in numbers:
#     if i not in freq: 
#         freq[i]=1
#     else:
#         freq[i]=+1

# freq="".join(freq)
# print(freq)

# find common element
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# lst3=[]
# for i in list1:
#     if i not in lst3:
#         lst3.append(i)
# for i in list2:
#     if i not in lst3:
#         lst3.append(i)
# print(lst3)

#common element
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# lst3=[]
# for i in list1:
#     if i in list2:
#         lst3.append(i)
# print(lst3)

# all one at left side
# list1 = [1,1,1, 2,1,1,1, 3, 4,1,1, 5]
# lst2=[]
# for i in list1:
#     if i !=1:
#         lst2.append(i)
# for i in list1:
#     if i==1:
#         lst2.append(i)
# print(lst2)

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# lst3=[]
# for i in list1:
#     if i not in list2:
#         lst3.append(i)
# print(lst3)

# move zero at the end
# numbers = [0, 1, 0, 3, 12, 0, 5]
# lst=[]
# for i in numbers:
#     if i!=0:
#         lst.append(i)
# for i in numbers:
#     if i==0:
#         lst.append(i)
# print(lst)


#find the missing value
# lst=[1,2,3,5,6]
# n=6
# ex=0
# ac=0
# for i in range(1,n+1):
#     ex+=i
# for i in lst:
#     ac+=i
# miss=ex-ac
# print(miss)

#merge two list and remove duplicate
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# lst3=[]
# for i in list1:
#     if i not in lst3:
#         lst3.append(i)
# for i in list2:
#     if i not in lst3:
#         lst3.append(i)
# print(lst3)


