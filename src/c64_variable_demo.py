import basicVarAnalysis


def c64_vars_mem_dump():
    mem = basicVarAnalysis.MemoryDump('C64')
    mem.find_vars("test_data/c64_variable_test.bin")
    mem.print_basic_ranges()
    mem.print_variables()    
    return mem

'''
10 F1=999999999999
20 F2=5.5
30 F3=-5.5
40 F4=0.00012345678912345
50 I1%=5
60 I1% = I1% + 1
70 I2%=-5
80 S1$="TEST":REM STR IN BASIC AREA, WILL HAVE "C" PREFIX
90 S2$="TES"+"T": REM STR IN HEAP, WILL HAVE "H" PREFIX
100 DIMF1(3):DIMF2(2,3):DIMF3(1,2,3):DIMI1%(1,2,3):DIMS$(1,2,3)
110 FORX=0TO1:  FORY=0TO2:FORZ=0TO3
120 F1(Z)=Z
130 F2(Y,Z)=Y*10+Z
140 F3(X,Y,Z)=X*100+Y*10+Z
150 I1%(X,Y,Z)=X*100+Y*10+Z
160 S$(X,Y,Z)=CHR$(48+X)+CHR$(48+Y)+CHR$(48+Z)
170 NEXT:NEXT:NEXT
'''

'''
parsing vars from memory dump...
- 40960 bytes (assuming $0000 to $9FFF)
- BASIC line number: 170
- BASIC line number on last exit: 0

BASIC ranges:
-------------
TXTTAB $0801/2049: start of BASIC (default $0801/2049), 439-byte extent
VARTAB $09B7/2487: start of variables, 77-byte extent
ARYTAB $0A04/2564: start of arrays, 369-byte extent
STREND $0B75/2933: end of arrays (exclusive)
FRETOP $9F3C/40764: end (bottom) of string heap, 196-byte extent
MEMSIZ $A000/40960: start (top) of string heap

floats:
-------
F1: 1E+12
modified: 10

F2: 5.5
modified: 20

F3: -5.5
modified: 30

F4: 1.234568E-04
modified: 40

X: 2
read: 140, 150, 160
modified: 110

Y: 3
read: 130, 140, 150, 160
modified: 110

Z: 4
read: 120, 130, 140, 150, 160
modified: 110


integers:
---------
I1%: 6
read: 60
modified: 50, 60

I2%: -5
modified: 70


strings:
--------
S1$: c"TEST"
modified: 80

S2$: h"TEST"
modified: 90


float arrays:
-------------
F1(row 0-3) = 0, 1, 2, 3
modified: 100, 120

F2(row 0-2, col 0-3) =
0, 10, 20
1, 11, 21
2, 12, 22
3, 13, 23
modified: 100, 130

F3(0, row 0-2, col 0-3) =
0, 10, 20
1, 11, 21
2, 12, 22
3, 13, 23
F3(1, row 0-2, col 0-3) =
100, 110, 120
101, 111, 121
102, 112, 122
103, 113, 123
modified: 100, 140


integer arrays:
---------------
I1%(0, row 0-2, col 0-3) =
0, 10, 20
1, 11, 21
2, 12, 22
3, 13, 23
I1%(1, row 0-2, col 0-3) =
100, 110, 120
101, 111, 121
102, 112, 122
103, 113, 123
modified: 100, 150


string arrays:
--------------
S$(2, 3, 4) =
S$(0, 0, 0) = h"000"
S$(1, 0, 0) = h"100"
S$(0, 1, 0) = h"010"
S$(1, 1, 0) = h"110"
S$(0, 2, 0) = h"020"
S$(1, 2, 0) = h"120"
S$(0, 0, 1) = h"001"
S$(1, 0, 1) = h"101"
S$(0, 1, 1) = h"011"
S$(1, 1, 1) = h"111"
S$(0, 2, 1) = h"021"
S$(1, 2, 1) = h"121"
S$(0, 0, 2) = h"002"
S$(1, 0, 2) = h"102"
S$(0, 1, 2) = h"012"
S$(1, 1, 2) = h"112"
S$(0, 2, 2) = h"022"
S$(1, 2, 2) = h"122"
S$(0, 0, 3) = h"003"
S$(1, 0, 3) = h"103"
S$(0, 1, 3) = h"013"
S$(1, 1, 3) = h"113"
S$(0, 2, 3) = h"023"
S$(1, 2, 3) = h"123"
modified: 100, 160
'''

if __name__ == "__main__":
    mem = c64_vars_mem_dump()
