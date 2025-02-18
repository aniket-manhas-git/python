def pal(s):
    for i in range(0,int(len(s)+1/2)):
        if(s[i]!=s[len(s)-i]):
            return "Not Palindrome"
    return "Palindrome"
if __name__=="__main__":
    s=input("Enter a string : ")
    print(pal(s))