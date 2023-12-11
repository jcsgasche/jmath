import math 

def mina(a, b, c):
	if b**2 < (4*a*c):
		return('Nicht definiert, weil negative Diskriminante')

	l1 = (-b + (b**2 - (4*a*c))**(0.5)) / (2*a)
	l2 = (-b - (b**2 - (4*a*c))**(0.5)) / (2*a)
	return(l1, l2)

def mina2(a, b, c):
    if b**2 < (4*a*c):
        return('Nicht definiert, weil negative Diskriminante')
    
    wurzelteil = 'sqrt({})'.format(b**2 - 4*a*c)
    nenner = '2*{}'.format(a)
    l1 = '(-{} + {}) / {}'.format(b, wurzelteil, nenner)
    l2 = '(-{} - {}) / {}'.format(b, wurzelteil, nenner)
    
    return(l1, l2)

def pq(x, y, z): 
    discri = y * y - 4 * x * z 
    sqrtval = math.sqrt(abs(discri)) 

    # checking condition for discriminant
    if discri > 0: 
        print("Real and different roots") 
        x1 = ((-y + sqrtval)/(2 * x)) 
        x2 = ((-y - sqrtval)/(2 * x))
        xs = [x1, x2]
        return(xs)

    elif discri == 0:
        print("Real and same roots") 
        x = (-y / (2 * x))
        return(x)

    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        x1 = (- y / (2 * x), " + i", sqrtval) 
        x2 = (- y / (2 * x), " - i", sqrtval)
        xs = [x1, x2]
        return(xs)