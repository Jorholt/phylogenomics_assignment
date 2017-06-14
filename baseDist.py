
def countBases(sequence):
    assert type(sequence) is str
    a = 0
    c = 0
    g = 0
    t = 0
    for i in sequence:
        assert i in 'ACGT'
        if i == 'A':
            a+= 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1
        elif i == 'T':
            t += 1
    baselist = []
    baselist.append(a/len(sequence))
    baselist.append(c/len(sequence))
    baselist.append(g/len(sequence))
    baselist.append(t/len(sequence))

    assert abs(1 - sum(baselist)) < 0.001

    return baselist
