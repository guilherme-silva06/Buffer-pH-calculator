#This is the main equation to calculate the pH of buffer solution : [H30+]**2 + (Ka+AcSalt)[H3O+] - Ka*Ca = 0
#AcSalt is Analytical Concentration of the salt
#In order to make the equation easier, we assume that [H3O+] is equal to x
from math import log

a_b = str(input('Indicate wether the solution is acidic or basic [A/B]: '))
if a_b == 'A':
    test = str(input('What value do you have: Ka or Kb? [Ka/Kb]: '))
    if test == 'Ka':
        Kab = float(input('Indicate the Ka of the acid: '))
        Cab = float(input('Indicate the analytical concentration of the acid: '))
        Csal =float(input('Indicate the analytical concentration of the salt: '))
    elif test == 'Kb':
        Kab = float(input('Indicate the Kb of the acid: '))
        Cab = float(input('Indicate the analytical concentration of the acid: '))
        Csal = float(input('Indicate the analytical concentration of the salt: '))
        Kab = (10 ** -14) / (Kab)
if a_b == 'B':
    test = str(input('What value do you have: Ka or Kb? [Ka/Kb]: '))
    if test == 'Kb':
        Kab = float(input('Indicate the Kb of the base: '))
        Cab = float(input('Indicate the analytical concentration of the base: '))
        Csal =float(input('Indicate the analytical concentration of the salt: '))
    elif test == 'Ka':
        Kab = float(input('Indicate the Ka of the base: '))
        Cab = float(input('Indicate the analytical concentration of the base: '))
        Csal = float(input('Indicate the analytical concentration of the salt: '))
        Kab = (10**-14)/(Kab)
###################
a = 1
b = (Csal + Kab)
c = (Cab*Kab)*(-1)
##########
delta = (float(((b)**2) - (4*a*c)))
delta_sqrt = (delta**(1/2))
#####################
x1 = float(-(b) - delta_sqrt)/(2*a)
x2 = float(-(b) + delta_sqrt)/(2*a)

if x1 < 0:
    x = x2
else:
    x = x1

delta = round(delta,4)
delta_sqrt = round(delta_sqrt,4)
print('\033[1;35m'+'The value of x is:',round(x,8), ''+ '\033[0;0m')
print('\033[1;35m' + 'The value of Delta is',delta, 'and its square root is', delta_sqrt,''+ '\033[0;0m')
pH = (-log(x,10))
pOH = (14 - pH)

if a_b == 'A':
    pH = round(pH, 4)
    print('\033[1;34m'+'The pH of the buffer is:',pH, '' + '\033[0;0m')
if a_b == 'B':
    pOH = round(pOH, 4)
    print('\033[1;34m'+'The pH of the buffer is:',pOH, '' + '\033[0;0m')