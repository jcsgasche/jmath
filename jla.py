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