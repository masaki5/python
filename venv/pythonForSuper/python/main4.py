team = ["A", "B", "C", "D", "E"]
for t1 in team :
    for t2 in team :
        if t1 == t2 :
            continue
        print(t1, "vs", t2)