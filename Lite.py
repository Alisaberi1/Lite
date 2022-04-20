"""
Input 5 characters 'c1', 'c2', 'c3', 'c4', c5'
and output whether that snack is healthy or not!
------------------------------------------------

01. R <- 0 , Y <- 0 , G <- 0
02. if c1 = 'G' then
03.     G <- G + 1
04. else if c1 = 'Y' then
05.     Y <- Y + 1
06. else then
07.     R <- R + 1
08. // repeat for all c2 , ... , c5
09. // afterwards G is equal to the number of 'G's
10. // and R is equal to the number of 'R's
11. // and Y is equal to the number of 'Y's
12. if R >= 3 OR (Y >= 2 AND R >= 2) OR G = 0 then
13.     output "nakhor lite"
14. else then
15.     output "rahat baash"
"""
c1,c2,c3,c4,c5=map(str,input())
R,G,Y=0,0,0
if c1=="G":
    G=G+1
elif c1=='Y':
    Y=Y+1
else:
    R=R+1
if c2=="G":
    G=G+1
elif c2=='Y':
    Y=Y+1
else:
    R=R+1
if c3=="G":
    G=G+1
elif c3=='Y':
    Y=Y+1
else:
    R=R+1
if c4=="G":
    G=G+1
elif c4=='Y':
    Y=Y+1
else:
    R=R+1
if c5=="G":
    G=G+1
elif c5=='Y':
    Y=Y+1
else:
    R=R+1
G,R,Y="G","R","Y"
if len(R)>=3 or (len(Y)>=2 and len(R)>=2) or len(G)==0:
    print("nakhor lite")
else:
    print("rahat baash")