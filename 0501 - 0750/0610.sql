select x, y, z,
iif(x + y > z and x + z > y and z + y > x, 'Yes', 'No') as triangle
from Triangle
