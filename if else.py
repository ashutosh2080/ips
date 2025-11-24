tic = int(input("enter the number of ticket: "))
seat =int(input("enter the number of seates: "))

if tic % 2 != 0:
    print("Invalid ticket count")
elif tic > seat:
    print("insufficient seats")
else:
    seat -= tic
    print("!!!seat reserved!!!")
    print("seats available : ", seat)
