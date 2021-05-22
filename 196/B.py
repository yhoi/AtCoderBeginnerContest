x = input()
index =x.find('.')
if index != -1:
    x = x[:index]
print(x)