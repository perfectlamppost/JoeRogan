
A=[0,0]
B=[5.1,5]
C=[4.9,0]
P=[4,1]
def triangle_area(A,B,C):
    
    area=abs(0.5 * ( A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]) ) )
    print(area)
    return(area)

def pointInside(A,B,C,P):
    area=triangle_area(A,B,C)
    areaA=triangle_area(P,B,C)
    areaB=triangle_area(A,P,C)
    areaC=triangle_area(A,B,P)
    if area == (areaA + areaB +areaC):
        return True
    else:
        return False
    
if pointInside(A,B,C,P):
    print(f'Point {P} is in triangle {A} {B} {C}')
else:
    print(f'Point {P} is NOT in triangle {A} {B} {C}')