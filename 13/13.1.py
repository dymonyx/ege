s = 'абг бде вабгж гж дзке евк же зк иж киж'
d = {c[0]: c[1:] for c in s.split()}

def f(s, end):
    if s[-1] == end: return 1
    else: return sum(f(s+c, end) for c in d[s[-1]])
print(f('к','е') + f('в','е'))
