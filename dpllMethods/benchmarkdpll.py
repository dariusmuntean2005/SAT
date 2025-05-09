import time
import copy
import matplotlib.pyplot as plt

# Import your methods
from dpll import dpll_method
from MFO import mfo_method
from JW import jw_method
from DLIS import dlis_method
from MOMS import moms_method


# --- BENCHMARK FUNCTION ---
def benchmark(method, clauses):
    start = time.perf_counter()
    result, branch_count = method(copy.deepcopy(clauses), 0)  # Pass 0 as initial branch count
    end = time.perf_counter()
    return result, end - start, branch_count


# --- FUNCTION TO READ CLAUSES FROM FILE ---
def read_clauses_from_file(filename):
    clauses = []
    with open(filename, 'r') as file:
        for line in file:
            clause = set(map(int, line.split()))
            if 0 in clause:
                clause.remove(0)
            clauses.append(clause)
    return clauses


# --- AVERAGE BENCHMARK FUNCTION ---
def average_benchmark(method, files):
    total_time = 0
    total_branches = 0
    total_results = []

    for filename in files:
        clauses = read_clauses_from_file(filename)
        result, t, branches = benchmark(method, clauses)
        total_results.append(result)
        total_time += t
        total_branches += branches

    avg_time = total_time / len(files)
    avg_branches = total_branches / len(files)

    return total_results, avg_time, avg_branches


# --- LIST OF FILES TO TEST ---
files = [
    # 'clause1.txt',
    # 'clause2.txt',
    'clause3.txt'
]

# --- METHODS TO TEST ---
methods = [
    ("DPLL", dpll_method),
    ("MFO", mfo_method),
    ("JW", jw_method),
    ("DLIS", dlis_method),
    ("MOMS", moms_method)
]

# --- RESULTS STORAGE ---
avg_times = []
avg_branches = []
all_results = []

# --- RUN THE AVERAGE BENCHMARK ---
for name, method in methods:
    res, avg_time, avg_branch = average_benchmark(method, files)

    all_results.append(res)
    avg_times.append(avg_time)
    avg_branches.append(avg_branch)

# --- PRINT FINAL RESULTS ---
print("\nAverage Benchmark Results:\n")
for i in range(len(methods)):
    print(
        f"{methods[i][0]}: {all_results[i]}, Average Time: {avg_times[i]:.6f}s, Average Branches: {avg_branches[i]:.2f}"
    )

# --- PLOT THE RESULTS ---
x_labels = [name for name, _ in methods]
x_pos = range(len(methods))

plt.figure(figsize=(12, 8))

# Plot Average Time
plt.subplot(2, 1, 1)
plt.bar(x_pos, avg_times, color='skyblue')
plt.xticks(x_pos, x_labels)
plt.ylabel('Time (s)')
plt.title('Average Benchmark: Time')

# Plot Average Branches
plt.subplot(2, 1, 2)
plt.bar(x_pos, avg_branches, color='salmon')
plt.xticks(x_pos, x_labels)
plt.ylabel('Branch Count')
plt.title('Average Benchmark: Branching')

plt.tight_layout()
plt.show()
