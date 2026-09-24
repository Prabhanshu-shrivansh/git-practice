#two pointer approch
#Two sum of the sorted list
#My code 
# numbers = [1, 2, 4, 6, 8, 9, 11]
# target = 10
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]+numbers[j]==target:
#          print(numbers[i],numbers[j])

# correct code
# numbers = [1, 2, 4, 6, 8, 9, 11]
# target = 10
# left=0
# right=len(numbers)-1
# while left<right:
#     total=numbers[left]+numbers[right]
#     if total==target:
#         print(numbers[left],numbers[right])
#         break
#     elif total<target:
#         left+=1
#     else:
#         right-=1

#remove duplicate from sorted list
# numbers = [1, 1, 2, 2, 3, 4, 4, 5, 5]
# slow=0
# for fast in range(1,len(numbers)):
#     if numbers[slow]!=numbers[fast]:
#         slow+=1
#         numbers[slow]=numbers[fast]
# print(numbers[:slow+1])


#move negative value to one side
# numbers = [2, -4, 5, -1, 3, -7, 8, -2]
# left=0
# right=len(numbers)-1
# while left<=right:
#     if numbers[left]<0:
#         left+=1
#     elif numbers[right]>=0:
#         right-=1
#     else:
#         numbers[left],numbers[right]=numbers[right],numbers[left]
#         left+=1
#         right-=1
        
# print(numbers)

# palindrom using two pointer
# text = "mam"
# left = 0
# right = len(text) - 1
# is_palindrome = True
# while left < right:
#     if text[left] != text[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome") 

#find the middlw value 
# num=[1,2,3,4,5,6,7,8,9]
# slow=0
# fast=0
# while fast+1<len(num):
#     slow+=1
#     fast+=2
# print(num[slow])


#print all possible pairs
# numbers = [1, 2, 3, 4, 6, 8, 9]
# target = 10
# left=0
# right=len(numbers)-1
# while left<right:
#     total=numbers[left]+numbers[right]
#     if total==target:
#         print(numbers[left],numbers[right])
#         left+=1
#         right-=1
        
#     elif total<target:
#         left+=1
#     else:
#         right-=1


# # find the closest value of the target
# numbers = [1, 3, 5, 7, 9, 12]
# target = 11


lst=[1,2,3,1,1,1,3,5,6,1]
pos=0
for i in range(len(lst)):
    if lst[pos]!=0:
        lst[pos],lst[i]=lst[i],lst[pos]
        pos+=1
print(lst)