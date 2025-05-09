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

def apply_rule1(clauses):
    for i in range(len(clauses)):
        if len(clauses[i]) == 1:
            literal = next(iter(clauses[i]))
            result = rule1(clauses, literal)
            if result == 1:
                return "SAT"
            elif result == -1:
                return "UNSAT"
            return "continue"
    return None

def apply_rule2(clauses):
    literals = []
    for clause in clauses:
        for elem in clause:
            literals.append(elem)

    for i in literals:
        if -i not in literals:
            if rule2(clauses, i) == 1:
                return "SAT"
            return "continue"
    return None

def mfo_method(clauses,branches):
    while True:
        res1 = apply_rule1(clauses)
        if res1 == "SAT":
            return "Satisfiable",branches
        if res1 == "UNSAT":
            return "Unsatisfiable",branches
        if res1 == "continue":
            continue

        res2 = apply_rule2(clauses)
        if res2 == "SAT":
            return "Satisfiable",branches
        if res2 == "continue":
            continue

        break

    if clauses == []:
        return "Satisfiable",branches
    for clause in clauses:
        if clause == set():
            return "Unsatisfiable",branches

    d={}
    for clause in clauses:
        for literal in clause:
            if literal in d:
                d[literal] += 1
            else:
                d[literal] = 1

    chosen_literal=max(d, key=lambda lit: d[lit])

    clauses_copy1 = [set(c) for c in clauses]
    clauses_copy2 = [set(c) for c in clauses]

    branches += 1

    rule1(clauses_copy1, chosen_literal)
    result1, branches1 = mfo_method(clauses_copy1, branches)
    if result1 == "Satisfiable":
        return result1, branches1

    rule1(clauses_copy2, compliment(chosen_literal))
    result2, branches2 = mfo_method(clauses_copy2, branches)
    if result2 == "Satisfiable":
        return result2, branches2

    return "Unsatisfiable", max(branches1, branches2)



