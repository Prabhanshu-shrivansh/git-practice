# #thread usingjin and without join
# import threading
# from threading import Thread ,Lock
# import time

# def test_method():
#     print("method start executing")
#     time.sleep(3)
#     print("method excuted successfully")
    
# if __name__=="__main__":
#     thread=threading.Thread(target=test_method)
#     print("thread is start")
#     thread.start() # start the thread
#     thread.join() # it can complete the thread like with the help of this one thread can run after that onther thread can run
#     print("thread is end")

# #create a thread and pass miltiple positional argument
# def print_value(a,b,c):
#     print(f"a:{a},b:{b},c:{c}")
    
# thread=threading.Thread(target=print_value, args=(1,2,3))
# thread.start()
# thread.join()


#create a thread and pass miltiple key value positional argument
# def print_value(a,b,c):
#     print(f"a:{a},b:{b},c:{c}")
    
# thread=threading.Thread(target=print_value, kwargs={'a':10,'b':20,'c':30})  
#--------------------------
#damon thread can run until it work can complete ""daemon=True""

# thread.start()
# thread.join()

# Locks in threads
# def person_one(lock):
#     with lock:
#         print("First person booked the room")
#         time.sleep(1)
#         print("First person vacates the room")


# def person_second(lock):
#     with lock:
#         print("Second person booked the room")
#         time.sleep(0.2)
#         print("Second person vacates the room")


# if __name__ == "__main__":
#     lock = threading.Lock()

#     thread1 = Thread(target=person_one, args=(lock,))
#     thread2 = Thread(target=person_second, args=(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()


# time out use for when thread take more time it it will waiat fro some time and run the next thread
