# 🎯️ SOLVE LINEAR SYSTEM

## 📃 Linear system solver (Ax = b)

A python-based library for solving system of equation linear using matrix decomposition techniques. This projects focuses on numerical stability and efficiency by implemting core algorithms from scratch. 

## 🚀️ Overview

This solver provides tools to decomposed matrix and find solutions for $x$ in the equation $Ax = b$. Instead of using generic inversion methods, it uses specific decomposition based on the properties matrix A.
$$\left\{\begin{array}{ccc}a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n} & = & b_{1} \\ a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n} & = & b_{2} \\ & \vdots & \\ {ccc}a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{nn} & = & b_{n} \end{array}\right.$$

## 🛠️ Features

The projects implements three decomposition methods:

- **LU decomposition**: Splites a square matrix into a lower triangular matrix ($\mathit{L}$) and upper triangular matrix ($\mathit{U}$). Ideal for general square matrix.
- **QR decomposition**: Decomposes matrix into an orthogonal matrix ($\mathit{O}$) and a upper triangular matrix ($\mathit{R}$). Highly stable and orks non-square matrix.
- **Cholesky decomposition**: An efficient $\mathit{L}\mathit{L}^{T}$ decomposed for **Symetric-Positive-Definite (SPD)** matrices. It is twices as fast as LU.

## 📁️ Project structure
```text
SolveLinearSystem-/
├── decomposition
│   ├── cholesky.py
│   ├── lu.py
│   └── qr.py
├── docs
│   ├── resolution_system_lineair.pdf
│   └── resolution_system_linear.tex
├── main.py
├── README.md
├── requirement.txt
└── solver.py

```

## 💻️ Usage

### Prerequisites
- Python 3.x
- Numpy (for matrix storage and operation)
