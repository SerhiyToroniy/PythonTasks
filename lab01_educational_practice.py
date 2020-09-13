def transfer_to_binary(x):
    bin = ""
    while x != 0:
        b = x % 2
        bin += str(b)
        x //= 2
    bin = bin[::-1]
    return bin

def count_nums(N, K):
    i = 1
    zero_count = global_count = 0
    while i != N:
        bin_num = transfer_to_binary(i)
        for j in bin_num:
            if j == "0":
                zero_count += 1
        if zero_count == K:
            global_count += 1
        i += 1
        zero_count = 0
    print(global_count)

def condition_acsses(s):
    line = s
    k = n = ""
    float_check = space_check = False
    float_count = 0
    for z in line:
        if z == " ":
            space_check = True
        elif space_check == False and z != " ":
            n += z
        else:
            k += z
        if z == "." or z == ",":
            float_count += 1
            float_check = True
    if float_check:
        print("N and K should be integer and lower than 109!")
        return
    a = int(n)
    b = int(k)
    if float_check or (a > 109 or b > 109):
        print("N and K should be integer and lower than 109!")
        return
    count_nums(a, b)

condition_acsses(input("Input N and K using \'SPACE\': "))