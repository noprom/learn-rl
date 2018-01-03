import numpy as np
import sys

if "../" not in sys.path:
  sys.path.append("../")
from lib.envs.gridworld import GridworldEnv

env = GridworldEnv()
print env