# #find the largest and smallest numbers element without using max min
# lst=[10,20,30,30,40,50,60,7]
# large=lst[0]
# small=lst[0]
# for num in lst:
#     if num>large:
#         large=num
#     if num<small:
#         small=num
    
# print("highest: ",large)
# print("smallest:",small)

# find the second highest element in the list
# lst1=[1,10,20,30,40,50,5,60,7]
# large=float('-inf')
# sec_large=float('-inf')

# for num in lst1:
#     if num>large:
#         sec_large=large
#         large=num
#     elif num>sec_large and num!=large:
#         sec_large=num     
# print(sec_large)

#remove duplicate elements in list
# lst=[1,10,20,4,40,20,30,40,50,5,60,7]
# lst1=[]
# for num in lst:
#     if num not in lst1:
#         lst1.append(num)
        
# print(lst1)


#all zeros at the end  
# lst1=[0,10,0,30,0,0,5,60,0]
# pos=0
# for i in range(len(lst1)):
#     if lst1[i]!=0:
#         lst1[pos],lst1[i]=lst1[i],lst1[pos]
#         pos+=1
# print(lst1)   

#count frequency of the element in the list
# lst=[1,4,1,1,1,10,30,40,50,10,20,30,40,50,5,60,7] 
# freq={}
# for i in lst:
#     if i not in freq:
#         freq[i]=1  #for first time we see numbers 
#     else:
#         freq[i]+=1  #have we already see the number then e increce the count 
# print(freq)
    
#reverse the list 
# lst=[1,10,20,30,40,50,5,60,7] 
# lst1=[]
# for i in range(len(lst)-1,-1,-1):
#     lst1.append(lst[i])
# print(lst1)


#sum of all elements
# lst = [1, 10, 20, 30, 40, 50, 5, 60, 7] 
# total=0
# for i in lst:
#     total+=i
# print(total)

#common element in list
# lst=[1,2,3,4,5]
# lst1=[3,4,5,6,7]
# lst2=[]
# for i in range(len(lst)):
#     for j in range(len(lst1)):
#         if lst[i]==lst1[j]:
#             lst2.append(lst[i])
# print(lst2)

# lst=[1,2,3,4,5]
# lst1=[3,4,5,6,7]
# lst2=[]

# for i in range(len(lst)):
#     found=False
    

#     for j in range(len(lst1)):
#         if lst[i]==lst1[j]:
#             found=True
#             break

        
#         if found==False:
#             lst2.append(lst[i])
            
# print(lst2)


#remove duplicate and merge two list     
# lst=[1,2,3,4,5]
# lst1=[3,4,5,6,7]
# result=[]

# for i in lst:
#     if i not in result:
#         result.append(i)
        
# for i in lst1:
#     if i not in result:
#         result.append(i)
# print(result)

#find the even and odd in the list
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

# numbers = [0, 1, 0, 3, 12, 0, 5]
# pos=0
# for i in range(len(numbers)):
#     if numbers[i]!=0:
#         numbers[pos],numbers[i]=numbers[i],numbers[pos]
#         pos+=1
# print(numbers)

#fuind duplicate in list
# nums = [1, 2, 2, 3, 1, 4, 3]
# result=[]
# for i in range(len(nums)):
#     found=False
#     for j in range(len(result)):
#         if nums[i]==result[j]:
#             found=True
#             break
    
#     if not found:
#         result=result+ [nums[i]]

# print(result)         



# from random import randint
# nums=[]
# new=[]
# high=0
# for i in range(100):
#     num=randint(1,100)
#     nums=nums+[num]

# for j in nums:
#     if j >high:
#         new.append(j)

# print(new)
# print(nums)

# #reverse the number
# num=12345
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10

# print(rev)

#Palindrom 
# num = 121
# temp=num
# rev=0
# while temp>0:
#     digit=temp%10
#     rev =rev*10+digit
#     temp//=10
    
# if rev==num:
#     print("palindrom")
# else:
#     print("NOT")

# nums = [1, 2, 3, 5, 6, 7, 8]
# exp=0
# act=0
# for i in range(1,len(nums)+2):
#     exp+=i
# for j in nums:
#     act+=j
    
# missing=exp-act
# print(missing)

# nums = [45, 12, 89, 3, 67, 21]
# high=float('-inf')
# second=float('-inf')

# for i in nums:
#     if i>high:
#         second=high
#         high=i
#     elif i> second and i!=high:
#         second=i
    
# print(high)
# print(second)

# nums = [45, 12, 89, 3, 67, 21]
# high=nums[0]
# small=nums[0]
# for i in nums:
#     if i>high:
#         high=i
#     if i<small:
#         small=i
# print(high)
# print(small)

# nums = [1, 2, 2, 3, 1, 4, 2, 3]
# freq={}
# for i in nums:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# nums = [2, 7, 11, 15, 3, 6]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print(nums[i], nums[j])

# nums = [0, 1, 0, 3, 12, 0, 5]
# pos=0
# for i in range(len(nums)):
#     if nums[i]!=0:
#         nums[pos],nums[i]=nums[i],nums[pos]
#         pos+=1
# print(nums)

# student={}
# for i in range(1,101):
#     name=input(f"enter the student name{i}")
#     age=int(input(f"enter the age{i}"))
    
#     student[name]=age
    
# print(student)


#all negative at starting
# nums = [3, -1, 5, -2, 8, -4, 7]
# pos=0
# for i in range(len(nums)):
#     if nums[i]<0:
#         nums[i],nums[pos]=nums[pos],nums[i]
#         pos+=1
# print(nums)
        
# nums = [3, 8, 5, 2, 7, 4, 9, 6]
# pos=0
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         nums[pos],nums[i]=nums[i],nums[pos]
#         pos+=1
# print(nums)

# s = "aabbcddee"

# for i in range(len(s)):
#     found = False

#     for j in range(len(s)):
#         if i != j and s[i] == s[j]:
#             found = True
#             break

#     if not found:
#         print(s[i])
#         break

# nums = [12, 5, 8, 3, 5, 2, 9]
# small=float('inf')
# second=float('inf')
# for i in nums:
#     if i <small:
#         second=small
#         small=i
#     elif i<second and i!=small:
#         second=i
        
# print(second)
