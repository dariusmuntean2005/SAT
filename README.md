# SAT Solver Project

This project implements and compares three SAT-solving methods: Resolution, Davis–Putnam (DP), and Davis–Putnam–Logemann–Loveland (DPLL), with a focus on branching heuristics within DPLL. It includes experiments on both random 3-SAT problems and structured Blocks World planning instances.

## Features

- Custom Python implementations of Resolution, DP, and DPLL
- Support for multiple DPLL branching heuristics: MFO, MOMS, DLIS, Jeroslow–Wang
- DIMACS file parsing for random 3-SAT instances and SAT encoded Blocks World planning problems
- Benchmarking and result visualization with matplotlib

  
## Installation

1. Make sure you have Python 3.8+ installed:
   https://www.python.org/downloads/

2. Clone the repository:

```
git clone git@github.com:dariusmuntean2005/SAT.git
cd SAT

```

3. Create a virtual enviroment
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

4. Install required libraries
```
pip install matplotlib
```

## User-manual
### Running experiments on Resolution, DP and DPLL slovers
1. Open folder: MPI/solvers/Tests and place a DIMACS CNF file you wish to test
2. Open file: MPI/solvers/benchmark.py
3. Change the filename string to: filename="Tests/your-filename"
![image](https://github.com/user-attachments/assets/12c3e59a-3b38-4d52-bc70-b7d4f00d9561)
4. Run the file

   
### Running single/multiple Blocks World file experiments on DPLL branching methods
1. Open folder: MPI/dpllMethods/BlocksWorld and add DIMACS CNF files with encoded Blocks World Planning problems
2. Open file: MPI/dpllMethods/benchmarkdpll.py
3. Add file path in list "files": "BlocksWorld/your-filename"
![image](https://github.com/user-attachments/assets/5340492d-8bb1-41e8-afeb-9f0e91fd3a02)
4. Run the file


### Running folder with Random 3-SAT problems on DPLL branching methods
1. Open folder: MPI/dpllMethods/3-SAT and add a folder with the DIMACS CNF files
2. Open file: MPI/dpllMethods/dpllmethodsbenchmark.py
3. Add folder path to "folder_path": folder_path="3-SAT/your-foldername"
![image](https://github.com/user-attachments/assets/558aa187-6de4-4a75-b355-80470022b80a)
4. Run the file

### (Optional) Store results
1. Open folder: MPI/Results and add a file and save your results in said file
