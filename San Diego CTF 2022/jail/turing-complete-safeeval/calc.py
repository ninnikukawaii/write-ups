#! /usr/bin/env python3

import os

os.environ['PWNLIB_NOTERM'] = '1'

import sys
import traceback
import pwnlib.util.safeeval as safeeval

# https://github.com/Gallopsled/pwntools/blob/ef698d4562024802be5cc3e2fa49333c70a96662/pwnlib/util/safeeval.py#L3
_const_codes = [
    'POP_TOP','ROT_TWO','ROT_THREE','ROT_FOUR','DUP_TOP',
    'BUILD_LIST','BUILD_MAP','BUILD_TUPLE','BUILD_SET',
    'BUILD_CONST_KEY_MAP', 'BUILD_STRING',
    'LOAD_CONST','RETURN_VALUE','STORE_SUBSCR', 'STORE_MAP',
    'LIST_TO_TUPLE', 'LIST_EXTEND', 'SET_UPDATE', 'DICT_UPDATE', 'DICT_MERGE',
    ]

_expr_codes = _const_codes + [
    'UNARY_POSITIVE','UNARY_NEGATIVE','UNARY_NOT',
    'UNARY_INVERT','BINARY_POWER','BINARY_MULTIPLY',
    'BINARY_DIVIDE','BINARY_FLOOR_DIVIDE','BINARY_TRUE_DIVIDE',
    'BINARY_MODULO','BINARY_ADD','BINARY_SUBTRACT',
    'BINARY_LSHIFT','BINARY_RSHIFT','BINARY_AND','BINARY_XOR',
    'BINARY_OR',
    ]

# The above only allows Turing-incomplete evaluation,
# so we decided to add our own ingenious additions:
complete_codes = _expr_codes + ['MAKE_FUNCTION', 'CALL_FUNCTION']

TURING_COMPLETE = True

def expr(e):
    if TURING_COMPLETE:
        c = safeeval.test_expr(e, complete_codes)
        return eval(c)
    else:
        return safeeval.expr(e)

try:
    print('Turing complete mode:', 'on' if TURING_COMPLETE else 'off')
    while True:
        e = input('>>> ')
        if e == 'exit':
            break
        try:
            print(expr(e))
        except Exception as err:
            traceback.print_exc(file=sys.stdout)
except EOFError as e:
    print()
