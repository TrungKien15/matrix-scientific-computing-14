## Setup (Global)

### 1. Install Python

Make sure you have Python (>=3.8) installed on your system.

Check version:

```
python --version
```

---

### 2. Install Manim globally

Install Manim using pip:

```
pip install manim
```

---

### 3. Verify installation

Run:

```
manim --version
```

If the version is displayed, the installation was successful.

---

## Usage

To render the animation quickly:

```
manim -pql main.py SVD
```

* `-pql`: low quality (faster rendering)
* `-pqh`: high quality (slower rendering)

---

## Note

Rendering in high quality may take a significant amount of time.
