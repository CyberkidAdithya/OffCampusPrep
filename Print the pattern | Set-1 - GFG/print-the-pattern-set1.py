def printPat(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            # print("\n I, J: ", j, i, "\n")
            print(*[j] * i, end = " ")
        print("$", end="")
    return ""

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
# } Driver Code Ends