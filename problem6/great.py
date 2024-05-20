n=str(input("please input your name"))
t=int(input("please input the time"))
def timetest(t,n):
    if 0<=t<=12:
        print("Good morning",n)
    if 13<=t<=17:
        print("Good afternoon",n)
    if 18<=t<=23:
        print("Good evening",n)
timetest(t,n)