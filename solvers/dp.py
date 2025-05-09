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

def is_tautology(clause):
    for literal in clause:
            if -literal in clause:
                return True
    return False

def dp_method(clauses):
    previous_clauses = set(tuple(sorted(clause)) for clause in clauses)

    while True:
        t = 0  #

        # Step 1: Apply Rule 1 (unit propagation)
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

        # Step 2: Apply Rule 2 (pure literal elimination)
        literals = set()
        for clause in clauses:
            for elem in clause:
                literals.add(elem)

        for i in literals:
            if -i not in literals:
                if rule2(clauses, i) == 1:
                    return "Satisfiable"
                t = 1
                break

        if t == 1:
            continue

        # Step 3: Apply Resolution
        added_new_clause = False
        new_clauses = []
        for i in range(len(clauses) - 1):
            for j in range(i + 1, len(clauses)):
                res = resolution(clauses[i], clauses[j])
                if res == -1:
                    continue
                if is_tautology(res):
                    continue
                if res == []:
                    return "Unsatisfiable"
                if res not in clauses and res not in new_clauses:
                    new_clauses.append(res)
                    added_new_clause = True

        if not added_new_clause:
            current_clauses = set(tuple(sorted(clause)) for clause in clauses)
            if current_clauses == previous_clauses:
                return "Satisfiable"
            previous_clauses = current_clauses

        clauses.extend(new_clauses)


