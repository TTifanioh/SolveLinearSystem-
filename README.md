# 🎯️ Resolution of linear system
A linear equation system is a set of equation in the form 
$$\left\{\begin{array}{ccc} a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} & = & b_{1} \\ 
                            a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} & = & b_{2} \\
                            \vdots                                           & \vdots & \vdots \\
                            a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{nn}x_{n} & = & b_{n}\end{array}\right.$$

or $x_{1}, \cdots, x_{n}$ are unknown generally element of $\mathbb{K}$.

## ⛓️ Forme matricielle
A linear system can as to write under form matrix $Ax = b$ or $A \in M_{m,n}(\mathbb{K}, \; x \in \mathbb{K}^{n})$ and $b \in \mathbb{K}^{m}$.
$$A = \left(\begin{array}{cccc} a_{11} & a_{12} & \cdots & a_{1n} \\
                                a_{21} & a_{22} & \cdots & a_{2n} \\
                                \vdots & \vdots & \ddots & \vdots \\
                                a_{m1} & a_{m2} & \cdots & a{mn}
            \end{array}\right), \;
    x = \left(\begin{array}{c} x_{1} \\ x_{2} \\ \vdots \\ x_{n}\end{array}\right), \mbox{ and }
    b = \left(\begin{array}{c}b_{1} \\ b_{2} \\ \vdots \\ b_{m}\end{array}\right)$$

## 📁️ Project structured

```text
SolveLinearSystem/
├── decomposition
│   ├── cholesky.py
│   ├── lu.py
│   └── qr.py
├── main.py
├── README.md
├── requirement.txt
└── solver.py

```

## 🛠️ Tools
Make sure you have installed python
