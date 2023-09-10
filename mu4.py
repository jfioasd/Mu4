import sys

def proj(x):
    return lambda a: a[x-1]

def const(x):
    return lambda a: x

def succ():
    return lambda a: a[0] + 1

def compose(fns):
    return lambda a: \
        fns[-1]([h(a) for h in fns[:-1]])

def p_rec(fns):
    g, h = fns
    def x(args):
        t = g(args[1:])
        for i in range(args[0]):
            t = h([i, t] + args[1:])

        return t
    return x

def mu(f):
    f = f[0]
    def x(args):
        t = 0
        while f([t] + args) != 0:
            t += 1
        return t
    return x

def lex(prog):
    ptr = 0
    L = []
    while ptr < len(prog):
        if prog[ptr] in '0123':
            x = int(prog[ptr])
            ptr += 1

            while ptr < len(prog) and \
                    prog[ptr] in '0123':
                x = x * 4 + int(prog[ptr])
                ptr += 1
            
            L.append(x)
            ptr -= 1

        else:
            L.append(prog[ptr])

        ptr += 1
    return L

def parse(tok):
    L = []

    x = 0
    while x < len(tok):
        i = tok[x]
        if isinstance(i, int):
            if x+1 < len(tok) and tok[x+1] == ';':
                L.append(proj(i))
                x += 1
            else:
                L.append(const(i))

        elif i == ';':
            L.append(succ())

        elif i == '(':
            L.append('(')
        
        elif i == ')':
            lvl = 1
            T = []
            while lvl > 0:
                tmp = L.pop()
                T = [tmp] + T
                lvl += tmp == ')'
                lvl -= tmp == '('
            L.append(compose(T[1:]))

        elif i == '#':
            if len(L) >= 2 and '(' not in L[-2:]:
                L.append(p_rec([L.pop(-2), L.pop()]))
            else:
                L.append(mu([L.pop()]))
        x += 1

    return L

if __name__ == '__main__':
    f = open(sys.argv[1]).read()
    x = eval(input())
    print(parse(lex(f))[0](x))
