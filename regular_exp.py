import re
list_of_mail= "this is my list of mail id ruhu @gamil, Ruhi @gamil.com, Rusu"
mail2="roh < roh@gmail.com > , ruhi < ruhi.n@nrn.com > rasik < ruhish@per.gov >"
pot=re.search(r"[r,R][a-z]+u",list_of_mail)
output=re.findall(r"[r,R][a-z]{2}u",list_of_mail)
o3=re.findall(r'\w+@\w+.[a-z]{3}',mail2)

# Name_list=["Gen","girl","age",1,"name","samu","Gen","girl","age",11,"name","swara"]
# print(type(Name_list))
# print(re.search(r'sw',Name_list))
print(pot,output)
print(o3)

# regular expression is the thing we use to search specific contetnt in file or listthat /w means any char from
# a-z [A-Z][0-9]  
# . means wild card means anything + means that any number of char [a-z]{4}means 4 alphabets are expected
# more detatils in re like ^ $ 
# link for details https://www.w3schools.com/python/python_regex.asp



