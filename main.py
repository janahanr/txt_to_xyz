import open3d
import math
import numpy as np
import txtconvet
import create3d

if __name__ == "__main__":
    txtconvet.txt_to_xyz("data.xyz", "dataset.txt")
    create3d.modeling("data.xyz")