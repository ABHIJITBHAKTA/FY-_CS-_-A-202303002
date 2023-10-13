print("1.bsc cs")
print("2.bsc it")
print("3.bms")

#input choice
ch=int(input("Enter your course no:"))
if ch==1:
    a=int(input("Enter your Percentage:"))
    if a<=55:
        print("You are not Elegable for this course")
    else:
        print("You can procced forward for admission")
elif ch==2:
    b=int(input("Enter your percentage:"))
    if b<=50:
        print("You are not Elegable for this course")
    else:
        print("You can Procced forward for admission")
elif ch==3:
    c=int(input("Enter your percentage:"))
    if c<=40:
        print("You are not elegable for this course")
    else:
        print("You can procced forward for admission")
