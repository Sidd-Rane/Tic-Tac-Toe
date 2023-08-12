def sum(a,b,c):
    return a+b+c
def checkwin(xstate,ostate):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if(sum(xstate[win[0]] , xstate[win[1]] , xstate[win[2]]) ==3):
            print('------X won the match------')
            return 1
        if(sum(ostate[win[0]] , ostate[win[1]] , ostate[win[2]]) ==3):
            print('------O won the match------')
            return 0
        return -1
    
def printboard(xstate,ostate):
    zero='X' if xstate[0] else ('O' if ostate[0] else 0)
    one='X' if xstate[1] else ('O' if ostate[1] else 0)
    two='X' if xstate[2] else ('O' if ostate[2] else 0)
    three='X' if xstate[3] else ('O' if ostate[3] else 0)
    four='X' if xstate[4] else ('O' if ostate[4] else 0)
    five='X' if xstate[5] else ('O' if ostate[5] else 0)
    six='X' if xstate[6] else ('O' if ostate[6] else 0)
    seven='X' if xstate[7] else ('O' if ostate[7] else 0)
    eight='X' if xstate[8] else ('O' if ostate[8] else 0)
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    ostate=[0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for x and 0 for 0
    print("Welcome to Tic Tac Toe")
    
    while(1):
        printboard(xstate,ostate)
        if(turn==1):
            print("X's Chance")
            value=int(input("Enter the value : "))
            xstate[value]=1
            turn=0
        else:
            print("O's Chance")
            value=int(input("Enter the value : "))
            ostate[value]=1
            turn=1
        print("\n")
        c=checkwin(xstate,ostate)
        if(c!=-1):
            break
