import time
import copy
import os
import matplotlib.pyplot as plt

# Import your methods
from resolution import resolution_method
from dp import dp_method
from dpll import dpll_method


# --- Read DIMACS CNF file properly ---
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



# --- Benchmark function ---
def benchmark(method, clauses):
    start = time.perf_counter()
    result = method(copy.deepcopy(clauses))
    end = time.perf_counter()
    return result, end - start


# --- Average Benchmark for a method over all files ---
def average_benchmark(method, files):
    total_time = 0
    results = []

    for file in files:
        clauses = read_clauses_from_dimacs(file)
        result, elapsed = benchmark(method, clauses)
        results.append(result)
        total_time += elapsed

    return results, total_time / len(files)


# --- Setup ---
folder_path = 'Tests/40clause'  # Your actual test folder
files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.cnf')]

methods = [
    ("Resolution", resolution_method),
    ("DP", dp_method),
    ("DPLL", dpll_method)
]

# --- Benchmarking ---
avg_times = []
all_results = []

for name, method in methods:
    res, avg_time = average_benchmark(method, files)
    all_results.append(res)
    avg_times.append(avg_time)

# --- Print Results ---
print("\nAverage Benchmark Results:\n")
for i in range(len(methods)):
    print(f"{methods[i][0]}: {all_results[i]}, Average Time: {avg_times[i]:.6f}s")

# --- Plot Results ---
x_labels = [name for name, _ in methods]
x_pos = range(len(methods))

plt.figure(figsize=(10, 6))
plt.bar(x_pos, avg_times, color='darkorange', edgecolor='black')
plt.xticks(x_pos, x_labels)
plt.ylabel('Average Time (seconds)')
plt.title('SAT Solver Comparison')
plt.tight_layout()
plt.show()
