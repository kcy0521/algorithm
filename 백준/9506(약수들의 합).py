while True:
    n = int(input())
    if n == -1:
        break
    
    sol = []
    for i in range(1,n):
        if n % i == 0:
            sol.append(i)

    if sum(sol) == n:
        print(n,'= ',end='')
        for i in range(len(sol)):
            if i == len(sol)-1:
                print(sol[i])
            else:
                print(f"{sol[i]} + ",end='')
            
    else:
        print(f"{n} is NOT perfect.")