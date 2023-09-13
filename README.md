# μ4
A esolang based on [μ6](https://github.com/bforte/mu6/)

The program takes a list from STDIN as the argument(s) to the function.

After calling the function, it prints the result of the function.

Unlike μ6, μ4 encodes the characters in octets. All allowed characters:

`0` `1` `2` `3` `;` `(` `)` `!`

# Grammar
## Functions
Here, `N` means a number encoded in base-4.

* `10` Constant function. Takes any number of arguments, and returns `4` (decoded from base-4).
* `;N` Projection. Takes any number of arguments, and returns the `N`th argument.
  * (Numbering starts at `0`)
* `;` Successor. Takes any number of arguments, and returns the successor of its first argument.
## Operators
Here, `h1`, `g`, `f1`, etc. all represent functions.
* `( h1 h2 .. hn g )` Composition. Returns a function:
  * Takes any number of arguments `a1 a2 .. an`.
  * Returns `g(h1([a1, a2, ... an]), h2([a1, a2, ... an]), ... hn([a1, a2, ... an]))`. 
* `! g h` Primitive recursion. Takes
  * Takes any number of arguments `n a1 .. an`.
    * If `n == 0`: Returns `g([a1, a2, .. an])`.
    * Else. Returns `h([n-1, ! g h([n-1, a1, ... an]), a1, .. an])`.
* `! f` Minimization.
  * Takes any number of arguments `a1 a2 .. an`.
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
