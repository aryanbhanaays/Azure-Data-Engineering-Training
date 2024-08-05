def square_num(number_list):
    print(number_list)
    for i in range(0,len(number_list)):
        number_list[i]*=number_list[i]
    return number_list

if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(square_num(numbers))
