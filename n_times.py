"""Print 1 t0 N using Head recursion"""

def func(i,n):
    if i > n:
        return
    print(i)
    func(i+1,n)

func(0,10)


"""Print a specific no n times"""

def funa(n,times):
    if times == 0:
        return
    print(n)
    funa(n,times-1)

funa(2,3)

