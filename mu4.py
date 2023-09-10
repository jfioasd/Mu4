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

    idx = 0
    while idx < len(tok):
        i = tok[idx]
        if isinstance(i, int):
            if idx+1 < len(tok) and tok[idx+1] == ';':
                L.append(proj(i))
                idx += 1
            else:
                L.append(const(i))

        elif i == ';':
            L.append(succ())

        elif i == '(':
            lvl = 1
            T = []

            idx += 1
            while idx < len(tok) and lvl > 0:
                t = tok[idx]
                T.append(t)
                lvl += t == '('
                lvl -= t == ')'
                idx += 1

            L.append(compose(parse(T[:-1])))
            idx -= 1

        elif i == '#':
            t = parse(tok[idx+1:])
            if len(t) == 2:
                L.append(p_rec(t))
            else:
                L.append(mu(t))
            break
        idx += 1

    return L

if __name__ == '__main__':
    f = open(sys.argv[1]).read()
    x = eval(input())
    print(parse(lex(f))[0](x))
