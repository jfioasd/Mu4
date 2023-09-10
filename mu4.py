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
            t = h([i, t] + args)
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
    if tok[0] == '#':
        x = parse(tok[1:])
        if len(x) == 2:
            return p_rec(x)
        else:
            return mu(x)

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
            lvl = 1
            T = []
            x += 1
            while x < len(tok) and lvl > 0:
                T.append(tok[x])
                lvl += tok[x] == '('
                lvl -= tok[x] == ')'
                x += 1
            L.append(compose(parse(T[:-1])))
            x -= 1
        x += 1

    return L
    
while True:
    x = input("> ")
    L = eval(input())
    print(parse(lex(x))(L))
