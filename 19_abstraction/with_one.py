# With Abstraction 

# There will be Abstract Classes & Abstract Methods 

# There Will be Contract Like Behavior 

# Laptop Contract - Government said these are must features for building Laptops 


# Abstract Class 
from abc import ABC, abstractmethod 

class Laptop(ABC):
    
    # Abstract Methods
    @abstractmethod
    def should_have_processor(self):
        pass 
    
    @abstractmethod    
    def should_have_ram(self):
        pass 
    
    @abstractmethod        
    def should_have_hard_disk(self):
        pass 
     
    @abstractmethod           
    def should_have_network(self):
        pass 


