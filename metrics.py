import numpy as np
from scipy.spatial.distance import directed_hausdorff
from scipy.spatial import cKDTree
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



def compute_hausdorff_distance(points_a, points_b):
    """
    Compute the symmetric Hausdorff distance between two point clouds.
    Each input is an (N, 3) NumPy array.
    """
    d_ab = directed_hausdorff(points_a, points_b)[0]
    d_ba = directed_hausdorff(points_b, points_a)[0]
    return max(d_ab, d_ba)


def compute_assd(surface1, surface2):
    """
    Compute Average Symmetric Surface Distance (ASSD)
    between two point clouds (Nx3 arrays).
    """
    tree1 = cKDTree(surface1)
    tree2 = cKDTree(surface2)

    dists1, _ = tree1.query(surface2)
    dists2, _ = tree2.query(surface1)

    assd = (np.mean(dists1) + np.mean(dists2)) / 2.0
    return assd
