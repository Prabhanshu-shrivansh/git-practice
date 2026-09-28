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



#find missing value
# lst=[1,2,3,5,6,7,8]
# ex=0
# ac=0
# for i in range(len(lst)+2):  # 2isliye 1 value missing hai or range 1 value kam tk chala hai
#     ex+=i
# for i in lst:
#     ac+=i
# miss=ex-ac
# print(miss)
    
#sum of all even no and odd
# numbers = [2, 5, 6, 9, 10, 13]
# even=0
# odd=0
# for i in numbers:
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(even)
# print(odd)

#count even and odd no.
# numbers = [2, 5, 6, 9, 10, 13]
# even=0
# odd=0
# for i in numbers:
#     if i %2==0:
#         even+=1
#     else:
#         odd+=1
        
# print(even)
# print(odd)

#second smallest nmber in the list
# numbers = [10, 5, 25, 8, 30, 15]
# small=float('inf')
# second=float('inf')
# for i in numbers:
#     if i<small:
#         second=small
#         small=i
#     elif i <second and i !=small:
#         second=i
# print(second)

#diffrence between max and min
# numbers = [10, 5, 25, 8, 30, 15]
# max=numbers[0]
# min=numbers[0]
# for i in numbers:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# diff=max-min
# print(diff)


#count -+ and zero
# numbers = [10, -5, 0, 8, -3, 0, 15, -7]
# pos=0
# neg=0
# zero=0
# for i in numbers:
#     if i >0:
#         pos+=1
#     elif i<0:
#         neg+=1
#     else:
#         zero+=1
# print(pos)
# print(neg)
# print(zero)

#lambda function
# print((lambda X: X*X)(5))

#lambda with filter
# number=[1,2,3,4,5,6,7]
# result=list(map(lambda x:x*2,number))
# print(result)
#lambda with filter
# number=[1,2,3,4,5,6,7]
# result=list(filter(lambda x: x%2==0,number))
# print(result)

#first duplicate
# numbers = [1, 2, 3, 4, 2, 5, 3]
# seen=[]
# dup=[]
# for i in numbers:
#     if i not in seen:
#         seen.append(i)
#     else:
#         dup.append(i)
#         break
# print(dup)

#find all dupicate
# numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]
# seen=[]
# dup=[]
# for i in numbers:
#     if i not in seen:
#         seen.append(i)
#     else:
#         dup.append(i)
        
# print(dup)


#sum of all value of dict
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30,
#     "d": 40
# }
# total=0
# for i in data.values():
#     total+=i
# print(total)

#find max value
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30,
#     "d": 40
# }
# total=0
# for i in data.values():
#     if i>total:
#         total=i
# print(total)

data = {
    "a": 10,
    "b": 50,
    "c": 30,
    "d": 20
}
max=0
max_key=""
for key , value in data.items():
    if value>max:
        max=value
        max_key=key
print(max_key) 