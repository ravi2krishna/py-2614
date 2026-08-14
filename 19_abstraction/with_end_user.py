# With Abstraction End User

from with_two import Dell

# End User Buying Dell Laptop

print("=" * 50)
print("     Customer Buying DELL Laptop")
print("=" * 50)

dellObject = Dell()
dellObject.should_have_processor()
dellObject.should_have_ram()
dellObject.should_have_hard_disk()
dellObject.should_have_network()

