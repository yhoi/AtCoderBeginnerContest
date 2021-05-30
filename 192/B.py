s = input()
ans = "Yes"

for i in range(len(s)):
    if(i%2==0):
      if(s[i].isupper()):
          ans = "No"
    else:
       if(s[i].islower()):
           ans = "No"
print(ans) 



