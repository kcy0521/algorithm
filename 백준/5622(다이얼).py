x = list(input())

sol = 0
for i in range(len(x)):
    a = ord(x[i])
    if 65 <= a < 68: #abc #2
        sol += 3
    elif 68 <= a < 71: #def #3
        sol += 4
    elif 71 <= a < 74: #ghi #4
        sol += 5
    elif 74 <= a < 77: #jkl #5
        sol += 6
    elif 77 <= a < 80: #mno #6
        sol += 7
    elif 80 <= a < 84: #pqrs #7
        sol += 8
    elif 84 <= a < 87: #tuv #8
        sol += 9
    elif 87 <= a <= 90: #wxyz #9
        sol += 10
    
    
print(sol)