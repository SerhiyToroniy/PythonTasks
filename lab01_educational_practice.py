def transfer_to_binary(x): #the function transfer decimal nums to binary
    bin = ""
    while x != 0:
        b = x % 2
        bin += str(b)
        x //= 2
    bin = bin[::-1] # [::-1] ~ reverse()
    return bin

def count_nums(N, K):    #the function counts suitable nums
    i = 1 #a condition from the task
    zero_count = global_count = 0 #global_count counts suitable nums
    while i != int(N):
        bin_num = transfer_to_binary(i) #call the function
        for j in bin_num: # counts zero in binary num
            if j == "0":
                zero_count += 1
        if zero_count == int(K): #compare zero_count and input data
            global_count += 1
        i += 1
        zero_count = 0 #update zero counter
    print(global_count)

def condition_acsses(s):    #the function check correct input data
    k = n = "" #k - left number; n - right number
    space_check = False
    for z in s:
        if z == " ":
            space_check = True
        elif space_check == False and z != " ":
            n += z #add symbols to LEFT num (using concatenation)
        else:
            k += z #add symbols to RIGHT num (using concatenation)
    if float(n) % 1 != 0 or float(k) % 1 != 0:
        raise Exception("N and K should be integer!")
    elif int(n) > 109 or int(k) > 109 or int(n) < 1 or int(k) < 1:
        raise Exception("N and K should be natural numbers and lower than 109!")
    count_nums(n, k)#call other function
condition_acsses(input("Input N and K using \'SPACE\': "))
