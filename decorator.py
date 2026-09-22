#make and use of decorator
#login-check decorator
def login_req(func):
    def wrapper():
        logged_in=True
        if logged_in:
            func()
        else:
            print("Please loggin first")
            
    return wrapper

@login_req
def dashboard():
    print("Welcome to the Home Page")
    
dashboard()

# # calculate time 
# import time
# def calculate_time(func):
#     def wrapper():
        