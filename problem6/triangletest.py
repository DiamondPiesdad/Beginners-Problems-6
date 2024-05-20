print("please input 3 sides of the triangle")
sd1=int(input())
sd2=int(input())
sd3=int(input())
def triangeltest(sd1,sd2,sd3) :
    m=max(sd1,sd2,sd3)
    li=[sd1,sd2,sd3]
    li.remove(m)
    s=sum(li)
    return s>m
print(triangeltest(sd1,sd2,sd3))