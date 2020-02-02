def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    if y==0:
        raise ValueError('cant divided by zero')
    else:
        return x/y

def main():
    print(add(4,5))
    print(sub(4,2))
    print(div(6,3))

if __name__ == '__main__':
    main()
