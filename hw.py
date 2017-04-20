import math
print [x for x in range(2, 101) if x % 2 == 0]
print [y for y in range(2, 101) if y % 3 == 0]
print [z for z in range(2, 101) if ( z in [z for h in range(2, max(3, int(round(math.sqrt(z) + 1)))) if z % h == 0 and z != h] ) ]
