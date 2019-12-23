tie=int(input())#tie
scarf=int(input())#scarf
vest=int(input())#vest
jacket=int(input())#jacket
suit1cost=int(input())#suit 1 cost
suit2cost=int(input())#suit 2 cost
maxcost1,maxcost2=0,0
x=min(tie,jacket)
#if(x==jacket):
maxcost1=suit1cost*x
'''else:'''
y=min((jacket-x),vest,scarf)
maxcost1+=suit2cost*y
    
x=min((jacket),vest,scarf)
maxcost2=x*suit2cost
#if(jacket-x!=0):
y=min(jacket-x,tie)
maxcost2+=y*suit1cost
print(max(maxcost1,maxcost2))
