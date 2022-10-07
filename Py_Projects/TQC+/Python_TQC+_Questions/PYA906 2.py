f_name = input()
str_old = input()
str_new = input()
#TODO
with open(f_name,'r') as file:
    content = file.read()
print("=== Before the replacement")
#TODO
print(content)
print("=== After the replacement")
#TODO
print(content.replace(str_old,str_new))
