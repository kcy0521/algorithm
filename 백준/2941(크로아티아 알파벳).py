word = list(input())
sol = len(word)

for i in range(1,len(word)):
    if word[i] == '=':
        if word[i-1] == 'c' or  word[i-1]=='s':
            sol -= 1
        elif word[i-1] == 'z' and i >1:
            sol -= 1
            if word[i-2] == 'd':
                sol -= 1
        elif word[i-1]=='z':
            sol -= 1
    elif word[i] == '-':
        if word[i-1] == 'c' or word[i-1] == 'd':
            sol -= 1
    elif word[i] == 'j':
        if word[i-1] =='l' or word[i-1] =='n':
            sol -= 1

print(sol)
