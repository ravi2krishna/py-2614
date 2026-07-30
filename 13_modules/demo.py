# Inbuilt Modules 

# 1st Syntax - import module (imports complete module i.e loading all functionalities in module)
# print(math.sqrt(25)) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print(math.sqrt(25))
print(math.pi)

print("=" * 20)

# 2nd Syntax - from module import specific_functionality (imports only what you need) # Recommended
from math import pi,e 
print(pi)
print(e)

# Python Inbuilt Modules - https://docs.python.org/3/py-modindex.html