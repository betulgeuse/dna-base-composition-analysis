import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Example DNA sequence (you can replace it with your own)
dna_sequence = "ATGCTTAGCGATCGATCGCTTAGCGATCGATGCTAGC"

# Step 1: Count the frequency of each base
bases = ["A", "T", "G", "C"]
counts = {base: dna_sequence.count(base) for base in bases}

# Step 2: Calculate percentages using NumPy
values = np.array(list(counts.values()))
percentages = (values / values.sum()) * 100

# Step 3: Create a Pandas DataFrame
df = pd.DataFrame({
    "Base": bases,
    "Count": list(counts.values()),
    "Percentage": percentages
})

print("DNA Base Composition:\n")
print(df)

# Step 4: Visualize with Matplotlib
plt.bar(df["Base"], df["Percentage"], color=["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"])
plt.title("DNA Base Composition")
plt.xlabel("Base")
plt.ylabel("Percentage (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()