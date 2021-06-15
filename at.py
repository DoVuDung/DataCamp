G= []
P = []
const  = 10
def initOpen(open):
    for i in range(const):
        open.append([])
        for j in range(2):
            open[i].append(0)


def emptyOpen(open):
    return len(open) - open.count(open[0]) == 0


def addQ(open,n,value,index):
    n = n+ 1
    open[n][0] = value
    open[n][1] = index
    i = n
    while i > 1:
        j = int(i/2)
        if open[i][0] < open[i][0]:
            temp = open[i]
            open[i] = open[j]
            open[j] = temp
        i = j
    return n


def removeQ(open):
    value = open[1][0]
    index = open[1][1]
    n = len(open) - open.count(open[0])
    open[1][0] = open[n][0]
    open[1][1] = open[n][1]
    open[n][0] = 0
    open[n][1] = 0
    n = n - 1
    i = 1
    while i <= int(n/2):
        j = i *2
        if j <n:
            if open[j][0] > open[j+1][0]:
                j = j + 1
                if open[j][0] > open[j][0]:
                    open[i], open[j] = open[j], open[i]
        else:
            if open[i][0] > open[j][0]:
                open[i], open[j] = open[j], open[i]
        i = i +1
    return value, index, n


def Split(string):
    k = string.index(' ')
    str = string[0:k]
    a= int(str, base=10)
    m = string.index(' ', k+ 1, -1)
    str = string[k+1:m]
    b = int(str, base=10)
    str = string[m + 1:len(string)]
    c= int(str, base = 10)
    return a, b, c


def init(path,G):
    f = open(path)
    string = f.readline()
    string = string.replace('\t', ' ')
    n,a, z = Split(string)
    for i in range(n +1):
        G.append([])
        for j in range(n+1):
            G[j].append(0)
    while True:
        string = f.readline()
        if not string:
            break
        string = string.replace('\t', ' ')
        i, j, x = Split(string)
        G[i][j] = G[j][i] = int(x)
    f.close()
    return int(n), int(a), int(z)

def view_matrix(G,n):
    for i in range(1,n +1):
        for j in range(1,n+1):
            print("%d" %G[i][j], end=' ')
        print()

def algorithm_for_tree(G,P,n,s,g):
    result = 0
    Close = []  
    O = []
    for i in range(const):
        Close.append(0)
        O.append(0)
    Open = []
    initOpen(open)
    m = 0
    m = addQ(open, m,result, s)
    O[s] = 1
    P[s] = s
    while not emptyOpen(open):
        value, u, m = removeQ(open)
        if u == g:
            result = value
        for v in range(1, n+1):
            if G[u][v] != 0 and O[v] == 0 and Close[v] == 0:
                x = value + G[u][v] 
                m = addQ(open,m,x,v)
                O[v] = 1
                P[v] = u 
        Close[u] = 1
        O[u] = 0
    return result
def Print(P, n, s, g):
    Path = []
    for i in range(0,n+1):
        Path.append(0)
    print("\nDuong di ngan nhat %d" %s,"den %d" %g,"la\nPath:", end=' ')
    Path[0] = g
    i = P[g]
    k = 1
    while i != s:
        Path[k] = i
        k = k +1
        i = P[i]
    Path[k] = s
    for i in range(0,k+1):
        i = k - j
        if i > 0:
            print("%d => "%Path[i], end=' ')
        else:
            print("%d => " %Path[i], end=' ')

    def main():
        n,s,g = init("data.txt",G)
        print("n: %d" %n, end='\n')
        view_matrix(G,n)
        for i in range(0, n+1):
            P.append(0)
        result = algorithm_for_tree(G,P, n, s, g)
