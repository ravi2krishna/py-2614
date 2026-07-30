# Customer Wants To use mathprofile module 

# 2nd Syntax - from module import specific_functionality (imports only what you need) # Recommended
from mathprofile import maintainer
print(f"Maintainer is {maintainer}")
# print(f"Institute is {institute}") # NameError: name 'institute' is not defined

print("=" * 50)

import mathprofile
print(f"Maintainer is {mathprofile.maintainer}")
print(f"Institute is {mathprofile.institute}")

print("Product Is: ",mathprofile.mul(20,30))
print(mathprofile.profile())
