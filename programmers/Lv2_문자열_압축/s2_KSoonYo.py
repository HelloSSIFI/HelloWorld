def solution(s):
    MIN=int(987654321)
    length=len(s)
    if(len(s)==1):
        return 1
    
    for cut in range(1, length//2+1): # 문자열 단위 1 ~ len(s)//2
        cnt=1
        res=""
        comp=s[:cut]
        for idx in range(cut, length, cut):
            if comp==s[idx:idx+cut]:
                cnt+=1
            else:
                if cnt==1:
                    cnt=""
                res+=str(cnt)+comp
                comp=s[idx:idx+cut]
                cnt=1
        if cnt==1:
            cnt=""
        res+=str(cnt)+comp
        
        if MIN > len(res):
            MIN=len(res)
 
    return MIN