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

            