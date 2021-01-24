rewards = [
    [0,0,0],
    [0,-9999,0],
    [0,0,0],
    [0,-100,1]
]

utilities = [
    [0,0,0],
    [0,-9999,0],
    [0,0,0],
    [0,-100,1]
] # la fel cu rewards ca sa nu mai calculez utilitatile pentru starile care au doar reward-uri,
# oricum in rest ar fi 0 initial deci o sa fie U(3,2) = reward +max[0,0], adica U(3,2) = 1

def R(x,y):
    return rewards[x][y]

def U(x,y):
    return utilities[x][y]

discount = 0.9

#U(3,0)
a = R(3,0) + discount * max([ 
    0.8*U(2,0)+0.1*U(3,0)+0.1*U(3,1), #West
    0.8*U(3,0)+0.1*U(3,0)+0.1*U(2,0), #East
    0.8*U(3,1)+0.1*U(3,0)+0.1*U(2,0), #North
    0.8*U(3,0)+0.1*U(3,0)+0.1*U(2,0)  #South
])
print(a)

#U(2,2)
x = R(2,2) + discount * max([
    0.8*U(1,2)+0.1*U(2,2)+0.1*U(2,1), #West
    0.8*U(3,2)+0.1*U(2,1)+0.1*U(2,2), #East
    0.8*U(2,2)+0.1*U(3,2)+0.1*U(1,2), #North
    0.8*U(2,1)+0.1*U(1,2)+0.1*U(3,2)  #South
])
print(x)

#U(2,1) 
y = R(2,1) + discount * max([
    0.8*U(2,1)+0.1*U(2,0)+0.1*U(2,2), #West
    0.8*U(3,1)+0.1*U(2,0)+0.1*U(2,2), #East
    0.8*U(2,2)+0.1*U(2,1)+0.1*U(3,1), #North
    0.8*U(2,0)+0.1*U(2,1)+0.1*U(3,1)  #South
])
print(y)