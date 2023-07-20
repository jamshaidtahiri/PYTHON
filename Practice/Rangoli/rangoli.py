alph = {
  1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
  9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
  16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
  23: 'w', 24: 'x', 25: 'y', 26: 'z'
}




def print_rangoli(size):
    # your code goes here

    for i in range(n):
        m = (n+(n-2))-2*i
        print(m*"-",end="")
        for j in range(i+1):
            print(alph[n-j],end="",sep="")
            if i!=0:
                print("-",end="",sep="") 
            
        for j in  reversed(range(i)):
            print(alph[n-j],end="",sep="") 
            if j  != 0:
                print("-",end="",sep="") 
            
            
        m = (n+(n-2))-2*i
        print(m*"-")
            
            
    for i in reversed(range(n-1)):
        m = (n+(n-2))-2*i
        print(m*"-",end="")
        for j in range(i+1):
            print(alph[n-j],end="",sep="")
            if i!=0:
                print("-",end="",sep="") 
            
        for j in  reversed(range(i)):
            print(alph[n-j],end="",sep="") 
            if j  != 0:
                print("-",end="",sep="") 
            
            
        m = (n+(n-2))-2*i
        print(m*"-")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)