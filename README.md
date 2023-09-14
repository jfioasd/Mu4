# μ4
A esolang based on [μ6](https://github.com/bforte/mu6/)

## Execution
The program takes a list from STDIN as the argument(s) to the function.

Then, the program is parsed into a function. The result of calling the function is printed.

Unlike μ6, μ4 encodes the characters in octets. All allowed characters:

`0` `1` `2` `3` `;` `(` `)` `!`

# Grammar
## Functions
* `N` Constant function. Takes any number of arguments, and returns `N`, decoded from base-4.
* `;N` Projection. Takes any number of arguments, and returns the `N`th argument. (base-4 decoded)
  * (Numbering starts at `0`)
* `;` Successor. Takes 1 argument. Returns the successor of its argument.
  * (Currently it works for multiple arguments, but I'll raise an error for that when I come back to it.)
## Operators
Here, `h1`, `g`, `f1`, etc. all represent functions.

`a1, a2, .. an` represents an arbitrary number of the same type of argument (i.e. numbers/functions). This list can be empty.
* `( h1 h2 .. hn g )` Composition. Defines a function which:
  * Takes any number of arguments `[a1, a2, .. an]`.
  * Returns `g(h1([a1, a2, ... an]), h2([a1, a2, ... an]), ... hn([a1, a2, ... an]))`. 
* `! g h` Primitive recursion. Defines a function which:
  * Takes any number of arguments `[n, a1, a2, .. an]`.
    * If `n == 0`: Returns `g([a1, a2, .. an])`.
    * Else. Returns `h([n-1, ! g h([n-1, a1, ... an]), a1, .. an])`.
* `! f` Minimization. Defines a function which:
  * Takes any number of arguments `[a1, a2, .. an]`.
  * Return the smallest natural number `x` where `f([x, a1, a2, .. an]) = 0`.

## Examples
### Multiplication
```
!0(;1;2!;0(;1;))
```

Basically:
`p_rec(0, compose(proj(1), proj(2), p_rec(proj(0), compose(proj(1), succ))))`

### Predecessor
```
!0;0
```

### Minimization test
```
!(;1!0;0)
```
