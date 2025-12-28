# 📦 Package Sorting Automation

This repository contains a simple Python function used to sort packages in a robotic automation factory based on their **dimensions** and **mass**.

## 🧠 Problem Overview

Each package must be dispatched to the correct stack according to the following rules:

### Definitions

- **Bulky**
  - Volume ≥ **1,000,000 cm³**, **OR**
  - Any dimension ≥ **150 cm**

- **Heavy**
  - Mass ≥ **20 kg**

### Dispatch Rules

| Condition | Stack |
|--------|-------|
| Not bulky and not heavy | `STANDARD` |
| Bulky **or** heavy | `SPECIAL` |
| Bulky **and** heavy | `REJECTED` |

---

## 🛠️ Implementation

The core logic is implemented in a single function:

```python
def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

## ▶️ How to Run

### Requirements
- Python 3.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/package-sorting.git
   cd package-sorting
2. Run the Python script:
   ```bash
   python sort.py 
