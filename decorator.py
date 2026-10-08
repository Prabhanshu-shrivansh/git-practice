# #make and use of decorator
# #login-check decorator
# def login_req(func):
#     def wrapper():
#         logged_in=True
#         if logged_in:
#             func()
#         else:
#             print("Please loggin first")
            
#     return wrapper

# @login_req
# def dashboard():
#     print("Welcome to the Home Page")
    
# dashboard()

# # # calculate time 
# # import time
# # def calculate_time(func):
# #     def wrapper():
        
        
def decorator1 (func):
    print("-------------")
    def wrapper1():
        print("first")
        func()
        print("second")
    return wrapper1

def decorator2(func):
    print("////////////")
    def wrapper2():
        print("Hii")
        func()
        print("Bye")
    return wrapper2

@decorator1
@decorator2
def greet():
    print("Prbhanshu")

greet() 