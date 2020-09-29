def create_matrix(arr, n):#the function which do all tasks
    matrix = []
    for i in range(n):
        temp=[] #the main matrix
        for j in range(n):
            temp.append(pow(arr[j],i)) #create temporary array
        matrix.append(temp) #add temporary array to the matrix
    for z in range(n): #outputting
        print(matrix[z])

def validation_and_running():#the function for validating data
    check = False
    while not check:
        try: #try to catch an error
            arr = []
            N = float(input("Input N: "))
            assert N > 0
            assert N % int(N) == 0
            N = int(N)
            print("Input array: ")
            for i in range(N):
                arr.append(float(input()))
            create_matrix(arr,N) #call the main function
            check  = True
        except AssertionError:
            check = False
            print("N must be a natural number!")
        except IndexError:
            check = False
            print("Make sure, array's length and N are equal!")
        except (TypeError, ValueError):
            check = False
            print("You must input only numbers using \"ENTER\"(=_=)!")

def menu():#the function for infinity starting a program
    check = "1" #key
    while check == "1":
        validation_and_running() #call a function to validate data
        check = input("Input \"1\" to try again or something else to exit: ")

menu()
