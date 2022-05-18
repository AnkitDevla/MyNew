# import pytube as pt
# con= pt.YouTube("https://www.youtube.com/watch?v=jWYsvvENTHw")
# fmt= con.streams
# print(fmt)

# from pytube import YouTube  
# video = YouTube('https://www.youtube.com/watch?v=jWYsvvENTHw')  
# # video.streams.all()  
# stream = video.streams.all()  
# for i in stream:  
    # print(i)  





# def show(a,b=[10,20]):
#     return a
#     return b

# print(show(130))

# num= int(input("Enter the number: "))

# def fun(num):    
#     if (num%3==0 and num%7!=0):
#         print("tik")
        
#     elif(num%7==0 and num%3!=0):
#         print("tok")
        
#     elif(num%3==0 and num%7==0):
#         print("tiktok")
        
#     else:
#         print(num)
# fun(num)









# a= int(input("Enter the number: "))
# b= int(input("Enter the number: "))
# def ma(a,b):
#     ret = a if a>b else b
#     return ret
# k = ma(a,b)
# print(f"Maximum number is: {k}")



# a= int(input("Enter the number: "))
# b= int(input("Enter the number: "))
# c= int(input("Enter the number: "))
# def ma(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>c:
#         return b
#     else:
#         return c

# k = ma(a,b,c)
# print(f"Maximum number is: {k}")


def tiktok (num):
    if num % 3 == 0 and num % 7 ==0:
        return "tiktok"
    if num % 3 == 0:
        return "tik"
    if num % 7 == 0:
        return "tok"
    return num 

print(tiktok(21))