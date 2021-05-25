A,B,W = map(int,input().split())
mx = int(0)
mn = int(0)
W = W*1000
if W%B == 0:
    mn = (W/B)
else:
    aCount = int(0)
    wTest = int(W)
    while(True):
        wTest = wTest -A
        print(wTest)    
        aCount =aCount+1
        print(aCount)
        if(wTest<0):
            break
        if(wTest%B==0):
            mn = aCount +(wTest/B)
if W%A == 0:
    mx = (W/B)
else:
    bCount = int(0)
    wTest = int(W)
    while(True):
        wTest = wTest -B    
        bCount =bCount+1
        if(wTest<0):
            break
        if(wTest%A==0):
            mn = bCount +(wTest/A)        

if(mx==0 and mn==0 ):
    print("UNSATISFIABLE")
else:
    print(mn+" "+mx)
