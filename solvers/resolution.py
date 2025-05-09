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

def resolution_method(clauses):
    k=len(clauses)
    while True:
        added_new_clause = False
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                res = resolution(clauses[i], clauses[j])
                if res == -1:
                    continue
                if is_tautology(res):
                    continue  # Skip tautologies
                if res == []:
                    return "Unsatisfiable"
                already_exists = False
                if res in clauses:
                    already_exists = True
                if not already_exists:
                    k+=1
                    clauses.append(res)
                    added_new_clause = True

        if not added_new_clause:
            break
    print(k)
    return "Satisfiable"


