def add(x):
    if x not in S:
      S.append(x)

def remove(x):
    if x in S:
      S.pop(S.index(x))

def check(x):
    if x in S:
      return 1
    elif x not in S:
      return 0
    
def toggle(x):
    if x in S:
      S.pop(S.index(x))
    elif x not in S:
      S.append(x)

# def all():
#     S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

# def empty():
#     S = []

S = [1,2,3,4]

x = 7
toggle(S)

print(S)
        