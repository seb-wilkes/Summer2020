import numpy as np
from src.computer import FishMeister

# Simple script to test that pathing is ok by default

my_class = FishMeister()
with open('somefile.txt', 'w') as f:
    f.write(str(np.random.randint(0,128)))
    f.write(str(my_class.frog))
