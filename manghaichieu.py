a= []
b= []
c= []
d= []
m = 2
n = 2

def create_matrix(a,m,n,c):
    for i in range(m):
        a.append([])
        for j in range(n):
            x= int(input("%c[%d][%d]= "%(c,i+1,j+1)))
            a[i].append(x)
def view_matrix(a,m,n):
    for i in range(m):
        for j in range(n):
            print("%d" %a[i][j], end= ' ')
        print()
def sum_matrix(a,b,m,n):
    c = []
    for i in range(m):
        c.append([])
        for j in range(n):
            x = a[i][j] + b[i][j]
            c[i].append(x)
    return c
def mul_matrix(a,b,m,n):
    d = []
    for i in range(m):
        d.append([])
        for j in range(n):
            x =0 
            for k in range(m):
                x = x + a[i][k] * b[k][j]
            d[i].append(x)
    return d    
def main():
    print("Tao ma tran a", end = '\n')
    create_matrix(a,m,n,'a')
    print("xem ma tran a", end = '\n')
    view_matrix(a,m,n)
    print("tao ma tran a", end = '\n')
    create_matrix(b,m,n,'b')
    print("tao ma tran b", end = '\n')
    view_matrix(b,m,n)
    c = sum_matrix(a,b,m,n)
    print("tao ma tran c", end = '\n')
    view_matrix(c,m,n)
    d = mul_matrix(a,b,m,n)
    print("xem ma tran d", end = '\n')
    view_matrix(d,m,n)

if __name__ == "__main__":
    main()