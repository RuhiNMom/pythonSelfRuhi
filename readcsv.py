f1=open("source.csv","r+")
f2=open("destination.txt","a+")
lines=f1.readlines()
print(lines)
for item in lines:
    d2=item.strip()
    data=d2.split("  ")
    print("data \n",data)
    for i in data:
        f2.write(i)
        f2.write("\n")
        print("\n....",i,"....\n")
f1.close()
f2.close()
print("........file close end of prg.....")
    
# tried to raed csv file with three colloums
# rollno  name    amnt
# 1   ronee  2222
# 2   ruhi    333

# first read file 
# readlines for count
# then to avoid \n appy first strip on items 
# the apply spilt method to differntiate values from each other using "   "
# other wise by defalut split function will convert list using single space 
# then aginain using for loop you can acces each element from list seprately
# the write it to the another file as seprate entry 