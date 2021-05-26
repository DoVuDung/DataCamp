g = []
def init(path, g):
    f = open(path)
    n = int(f.readline(),base = 10)
    for i in range(n +1):
        g.append([])
        for j in range(n+1):
            g[i].append(0)
    while True:
        string = f.readline()
        if not string:
            break
        string = string.replace('\t', ' ')
        k = string.index(' ')
        str = string[0:k]
        i = int(str,base=10)
        m = string.index(' ',k+1,-1)
        str = string[k+1:m]
        j = int(str, base = 10)
        str = string[m+1:len(string)]
        x= int(str, base = 10)
        g[i][j] = g[j][i] = x
    f.close() 
    return n

def view_matrix(g,n):
    for i in range(1,n +1):
        for j in range(1,n+1):
            print("%d" %g[i][j], end =' ')
        print()

def main():
    n = init("dulieu.txt", g)
    print("xem ma tran g", end = '\n')
    view_matrix(g,n)

if __name__ == "__main__":
    main()
