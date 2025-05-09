import time
import tracemalloc
import copy
import matplotlib.pyplot as plt

# Import your methods
from resolution import resolution_method
from dp import dp_method
from dpll import dpll_method

# --- BENCHMARK FUNCTION ---
def benchmark(method, clauses):
    tracemalloc.start()
    start = time.perf_counter()
    result = method(copy.deepcopy(clauses))  # Deep copy so original clauses stay untouched
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, end - start, peak / 1024  # Return result, time (seconds), peak memory (KB)

# --- YOUR CLAUSES TO TEST ---
def read_clauses_from_dimacs(filename):
    clauses = []
    with open(filename, 'r') as file:
        for line in file:
            stripped = line.strip()
            if (
                stripped.startswith(('c', 'p', '%')) or
                stripped == '' or
                stripped == '0'  # skip lone 0 line
            ):
                continue
            try:
                numbers = list(map(int, stripped.split()))
                if numbers and numbers[-1] == 0:
                    numbers.pop()  # remove ending 0
                clause = set(numbers)
                if clause:
                    clauses.append(clause)
            except ValueError:
                print(f"Warning: Skipping invalid line in {filename}: {line.strip()}")
    return clauses

filename = "Tests/uf20-01.cnf"  # Path to the DIMACS file
clauses = read_clauses_from_dimacs(filename)

# --- METHODS TO TEST ---
methods = [
    ("Resolution", resolution_method),
    ("DP", dp_method),
    ("DPLL", dpll_method)
]

# --- RESULTS STORAGE ---
times = []
memories = []
results = []

# --- RUN THE BENCHMARK ---
for name, method in methods:
    # Run the benchmark
    res, t, mem = benchmark(method, clauses)

    results.append(res)
    times.append(t)
    memories.append(mem)

# --- PRINT FINAL RESULTS ---
print("\nBenchmark Results:\n")
for i in range(len(methods)):
    print(f"{methods[i][0]}: {results[i]}, Time: {times[i]:.6f}s, Memory: {memories[i]:.2f} KB")

# --- PLOT THE RESULTS ---
x_labels = [name for name, _ in methods]
x_pos = range(len(methods))

plt.figure(figsize=(12, 8))

# Plot Time
plt.subplot(2, 1, 1)
plt.bar(x_pos, times, color='skyblue')
plt.xticks(x_pos, x_labels)
plt.ylabel('Time (s)')
plt.title('Benchmark: Time')

# Plot Memory
plt.subplot(2, 1, 2)
plt.bar(x_pos, memories, color='lightgreen')
plt.xticks(x_pos, x_labels)
plt.ylabel('Memory (KB)')
plt.title('Benchmark: Memory Usage')

plt.tight_layout()
plt.show()
