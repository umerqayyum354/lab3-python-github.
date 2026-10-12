while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Check Even / Odd\n6. Calculate Percentage\n7. Exit")

    N1 = float(input("\nEnter first number : "))
    operation = int(input("\nChoose Operation : "))

    if operation == 7:
        print("\nExiting Program")
        break

    if operation == 5:
        if int(N1) % 2 == 0:
            print("\nYour No. is an Even Number")
        else:
            print("\nYour No. is an Odd Number")
        continue

    N2 = float(input("\nEnter Second Number : "))

    if operation == 1:
        result = N1 + N2
    elif operation == 2:
        result = N1 - N2
    elif operation == 3:
        result = N1 * N2
    elif operation == 4:
        if N2 == 0:
            print("Invalid Denominator")
            continue
        result = N1 / N2
    elif operation == 6:
        if N2 == 0:
            print("Invalid Denominator")
            continue
        result = (N1 / N2) * 100
    else:
        print("\nError In Input")
        continue

    print("\nFirst Number :", N1)
    print("Operation :", operation)
    print("Second Number :", N2)
    print("Result :", result)
    print("\nTask Completed")
