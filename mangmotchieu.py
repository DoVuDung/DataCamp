n = 0
a= []
def create_arr(a,n):
    for i in range(n):
        a.append(int(input('nhap so %d:' %(i+1))))
def  view_arr(a,n):
    for j in range(n):
        print(a[j], end=' ')
    print("\n")
def view_down_to(a,n):
    for i in range(0,n): 
        print(a[n-i-1], end= " ")
    print("\n")
def sum_of_items(a,n):
    s = 0
    for i in range(n):
         s += int(a[i])
    return s   
def insert_item(a,n,k,x):
    for i in range(k,n):
        j = n -1 -i +k
        a.append(a[j-1])
    a.insert(k,x)
    return n + 1
def reverse_array(a,n):
    i = 0
    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
def sort_arr(a,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if a[j] < a[i]:
                a[i],a[j] = a[j], a[i]
def main():
    n = int(input("nhap n: "))
    create_arr(a,n)
    view_arr(a,n)
    n = insert_item(a,n,2,9)
    view_arr(a,n)
    reverse_array(a,n)
    view_arr(a,n)
    sort_arr(a,n)
    view_arr(a,n)

if __name__ =="__main__":
    main()