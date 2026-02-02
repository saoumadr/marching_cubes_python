# 3D Surface Reconstruction with Marching Cubes

This repository contains an implementation of the **Marching Cubes (MC)** algorithm for 3D surface reconstruction from volumetric data. The project includes:

- Synthetic datasets (sphere, torus, ellipsoid, cube, cone)
- Evaluation of reconstructed surfaces using **Hausdorff Distance** and **Average Symmetric Surface Distance (ASSD)**
- Interactive 3D visualization with adjustable isolevels
- Application to real-world CT volumes (bladder, liver, lungs, kidneys, skeleton) using the scikit-image implementation.
- Discussion of limitations and modern variants of Marching Cubes

---

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Key features](#key-features)
- [Results](#results)
- [Limitations](#limitations)
- [Modern Variants](#modern-variants)
- [Usage](#usage)

---

## Installation

Clone the repository and install the dependencies:

```bash
git clone <repository_url>
cd <repository_folder>
pip install -r requirements.txt
```

## Dataset

This project supports both synthetic datasets and real CT scans.

### Synthetic datasets

- Sphere
- Torus
- Ellipsoid
- Cube
- Cone

Synthetic shapes are generated as 3D scalar fields on uniform grids. Analytical ground truth surfaces are available and sampled for quantitative evaluation.

### CT volumes

- Bladder
- Liver
- Lungs
- Kidneys
- Skeleton

CT volumes are processed using the custom Marching Cubes implementation to extract organ surfaces.

---


## Key features

- Custom Python implementation for educational purposes.
- NumPy-based voxel representation.
- Interactive Matplotlib visualization with real-time isolevel adjustment.

---

## Evaluation Metrics

Two standard surface distance metrics are used to assess reconstruction accuracy:

- **Hausdorff Distance**  
  Maximum distance from any point on the reconstructed surface to the closest point on the ground truth surface.

- **Average Symmetric Surface Distance (ASSD)**  
  Average of the distances from reconstructed surface points to the ground truth surface and from ground truth points to the reconstructed surface.

These metrics provide a quantitative evaluation of geometric accuracy.

---

## Results

See report

---

## Limitations

The current implementation has several limitations:

- **Vertex duplication**: Vertices are not shared between adjacent triangles, increasing memory usage.
- **Performance**: Python-level loops over the voxel grid limit scalability to large volumes.
- **Topological ambiguities**: Classic Marching Cubes may produce holes or inconsistencies.
- **Manual isolevel selection**: No automatic optimization or gradient-based smoothing.
- **Uniform grids only**: Non-uniform voxel spacing is not fully supported.

---

## Modern Variants

Several improvements and alternatives to classic Marching Cubes exist:

- **Marching Cubes 33 (MC33)**  
  Resolves topological ambiguities by increasing the number of distinct cube configurations.
- **Marching Tetrahedra**  
  Decomposes cubes into tetrahedra to avoid ambiguous cases.
- **GPU-accelerated implementations**  
  Enable real-time surface reconstruction.
- **Surface smoothing and adaptive refinement**  
  Improve mesh quality and reduce noise.

---

## Usage

Run the main script to reconstruct and visualize a surface:

```bash
python main.py
```
