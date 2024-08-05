def square(numbers):
    return [i*i for i in numbers]    

if __name__=='__main__':
    numbers=list(map(int,input().split()))
    print(square(numbers))