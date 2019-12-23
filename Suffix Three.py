l,solution=[],[]
n=int(input())
lines = ""
def solve(i):
    if(i.endswith('po')):
        return("FILIPINO")
    elif(i.endswith('desu') or i.endswith('masu')):
        return("JAPANESE")
    elif(i.endswith('mnida')):
        return("KOREAN")
    else:
        return(" ")

for i in range(n):
    lines=input()
    result=solve(lines)
    solution.append(result)
for i in solution:
    print(i)