def duplicatezeros():
    arr=list()
    arr=eval(input("enter array:"))
    l=len(arr)
    p = False
    for i in range(0,l):
        if p == True:
            p=False
            continue
        elif arr[i]==0:
            arr.insert(i+1,0)
            p = True
        

    print(arr)
duplicatezeros()
