def init(path):
    f = open(path)
    while True:
        x= f.read()
        print(x)
        if not x:
            break
    f.close()
def main():
    init("data.txt")
if __name__ == "__main__":
    main()
