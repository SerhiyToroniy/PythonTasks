def binary_search(K, list):
    global_operation = operation = 1#counters
    save=[]
    for i in list:#copying array
        save.append(i)
    list.sort()#sort array
    left = 0
    right = len(list)-1
    while True:
        mid = (left + right) // 2
        if left<=right:
            if list[mid] == K:  # we find it
                for i in range(len(save)):
                    global_operation += 1
                    if save[i] == list[mid]:  # print indexs
                        print("Index: ", i)
                break
            if list[mid] > K:  # K is on the left side
                operation += 1
                right = mid - 1
            if list[mid] < K:  # K is on the right side
                operation += 1
                left = mid + 1
        else:#we didn't find K
            global_operation = operation
            print("This number doesn't exist!")
            break
    print("Operation count: ", operation)
    print("All operation count: ", global_operation)

x = [-5, 364, -114, 91, 43, -436, -134, 5, 77, 336] #example
binary_search(float(input("Input K:")), x) #call a function
