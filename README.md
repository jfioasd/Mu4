# Mu4
A language based on [μ6](https://github.com/bforte/mu6/)

Unlike μ6, μ4 encodes the characters in octets. All allowed characters:

`0` `1` `2` `3` `;` `(` `)` `#`

# Grammar
## Functions
* `10` Constant function. Takes any number of arguments, and returns `4` (decoded from base-4).
* `1;` Projection. Takes any number of arguments, and returns the first argument.
* `;` Successor. Takes any number of arguments, and returns the successor of its first argument.
## Operators
Here, `h1`, `g`, `f1`, etc. all represent functions.
* `( .. h2 h1 g )` Composition. Takes any number of arguments. Applies these arguments to all of the `h` functions. Apply this result to `g`.
* `# f1 f2` Primitive recursion.
* `# f1` Minimization.
