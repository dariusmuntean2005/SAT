def compliment(L):
    return -L

def rule1(clauses, L):
    Lc = compliment(L)
    clauses_copy = clauses[:]
    for clause in clauses_copy:
        if L in clause:
            clauses.remove(clause)
            if clauses == []:
                return 1
        elif Lc in clause:
            clause.remove(Lc)
            if clause == set():
                return -1
    return 0

def rule2(clauses, L):
    clauses_copy = clauses[:]
    for clause in clauses_copy:
        if L in clause:
            clauses.remove(clause)
            if clauses == []:
                return 1
    return 0

def resolution(clause1, clause2):
    for elem in clause1:
        if -elem in clause2:
            new_clause = set(clause1) | set(clause2)
            new_clause.remove(elem)
            new_clause.remove(-elem)
            return new_clause
    return -1

def dp_method(clauses):
    while True:
        t = 0
        for i in range(len(clauses)):
            if len(clauses[i]) == 1:
                literal = next(iter(clauses[i]))
                result = rule1(clauses, literal)
                if result == 1:
                    return "Satisfiable"
                elif result == -1:
                    return "Unsatisfiable"
                t = 1
                break
        if t == 1:
            continue

        literals = []
        for clause in clauses:
            for elem in clause:
                literals.append(elem)

        for i in literals:
            if -i not in literals:
                if rule2(clauses, i) == 1:
                    return "Satisfiable"
                t = 1
                break
        if t == 1:
            continue

        for i in range(len(clauses) - 1):
            for j in range(i + 1, len(clauses)):
                rez = resolution(clauses[i], clauses[j])
                if rez != -1:
                    if rez == set():
                        return "Unsatisfiable"
                    if rez not in clauses:
                        clauses.append(rez)
                        t = 1
                        break
            if t == 1:
                break
        if t == 0:
            return "Satisfiable"
