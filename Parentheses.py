def minParentheses(p):
     
    
    bal=0
    ans=0
    for i in range(0,len(p)):
        if(p[i]=='('):
            bal+=1
        else:
            bal+=-1
             
        
        if(bal==-1):
            ans+=1
            bal+=1
    return bal+ans

if __name__=='__main__':
    p = "())"
     

    print(minParentheses(p))