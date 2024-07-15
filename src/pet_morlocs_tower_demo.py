
import basicVarAnalysis

# Process variables in a PET memory dump of Morloc's Tower (Automated Simulations, 1979)
# https://en.wikipedia.org/wiki/Morloc%27s_Tower

def c64_morlocs_tower_mem_dump():
    mem = basicVarAnalysis.MemoryDump('PETROM4.0')
    mem.find_vars("test_data/pet_morlocs_tower.bin")

    # TODO:  No manual code analysis done yet on Morloc's Tower variables
    #        just some formatting on some arrays loaded from the 2nd file
    mem.add_formatting("D1%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("D2%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("M%()",  width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("MT%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("N%()",  width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("NO%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("T%()",  width = 3, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("TX%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("TY%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("XS%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")
    mem.add_formatting("YS%()", width = 2, row = 1, col = 0, comment = "TODO: loaded from 2nd file")

    mem.print_basic_ranges()
    mem.print_variables()
    return mem

'''
parsing vars from memory dump...
- 32768 bytes (assuming $0000 to $7FFF)
- BASIC line number: 96
- BASIC line number on last exit: 0

BASIC ranges:
-------------
TXTTAB $0401/1025: start of BASIC (default $0401/1025), 13695-byte extent
VARTAB $397F/14719: start of variables, 665-byte extent
ARYTAB $3C18/15384: start of arrays, 2997-byte extent
STREND $47CD/18381: end of arrays (exclusive)
FRETOP $73AB/29611: end (bottom) of string heap, 3157-byte extent
MEMSIZ $8000/32768: start (top) of string heap + 1

floats:
-------
AA: 5
read: 7040
modified: 1020

AI: 0
read: 480
modified: 475

AM: 1
read: 830, 7040
modified: 1020

AS: 1.5
read: 5430, 5824
modified: 5000

HI: 0
read: 7005
modified: 5400

HN: 4
read: 1330, 6140
modified: 1020, 6140

I: 2
read: 20, 21, 24, 43, 48, 51, 66, 68, 75, 76, 80, 86, 93, 94, 95, 96, 310, 320, 462, 500, 664, 702, 910, 930, 965, 1030, 1605, 1610, 1613, 1615, 1620, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1650, 1660, 4210, 4310, 4320, 4330, 5049, 5050, 5051, 5052, 5391, 5410, 5803, 5820, 5852, 5854, 6212, 6400, 6405, 6410, 6450, 6460, 7508, 11000
modified: 19, 20, 21, 24, 43, 48, 51, 66, 68, 75, 76, 80, 86, 93, 95, 96, 310, 462, 664, 702, 766, 821, 910, 930, 965, 1030, 1605, 1610, 1613, 1615, 1620, 1640, 1642, 1644, 1646, 1650, 1660, 4200, 4310, 5046, 5049, 5408, 5803, 5820, 5852, 6212, 6400, 6450, 7002, 7508, 11000

I0: 0
read: 376, 378
modified: 376

I1: 0
read: 105, 116, 145, 156, 4413, 4432, 5580
modified: 4411, 4412, 4431, 4432, 5490, 5500, 5502, 5630, 5670

IA: 0
read: 5391, 5410, 5415, 7020
modified: 5046, 5391

IC: 251
read: 520
modified: 500

ID: 2
read: 475, 1002, 1010, 1020, 1210, 1900, 5045, 5701, 5824, 6300, 12040
modified: 1000

II: 11
read: 510, 600
modified: 510, 600

IN: 0
read: 7005
modified: 5284, 5391, 5450, 5803, 5910

IR: 4
read: 4130, 4140
modified: 4130

J: 152
read: 19, 20, 43, 60, 65, 66, 71, 75, 76, 86, 98, 310, 460, 462, 1605, 1610, 1613, 1615, 1620, 1650, 1660
modified: 19, 20, 43, 65, 68, 71, 73, 74, 310, 460, 655, 1605, 1610, 1613, 1615, 1620, 1650, 1660, 5045, 6140

J0: 59
read: 1605, 1610, 1613, 1615, 1620, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647
modified: 1600

JO: 0
read: 376, 402, 412
modified: 374, 376, 378

JX: 19
read: 104, 106, 107, 116, 156, 220, 230, 370, 372, 400, 410, 460
modified: 104, 106, 107, 116, 146, 147, 156, 210, 220, 230, 240, 310, 450, 600, 670, 680, 830, 5520, 5560

JY: 35
read: 116, 144, 146, 147, 156, 210, 240, 370, 372, 410, 460, 686
modified: 106, 107, 116, 144, 146, 147, 156, 210, 220, 230, 240, 310, 450, 600, 670, 680, 830, 5520, 5560

K: 1
read: 210, 220, 230, 240, 320, 602, 4410, 4411, 4412, 4413, 4414, 4430, 4431, 4432, 4433, 4434, 7040, 7050
modified: 200, 250, 300, 350, 830, 1600, 4410, 4430, 5415, 6990, 7031, 7033, 7040

K0: 2
read: 106, 107, 110, 116, 146, 147, 148, 156
modified: 100, 120, 140, 150

KF: 1
read: 201, 210, 220, 230, 240, 600, 5110, 5282, 5283, 5284, 5293, 5310, 5350, 5370, 5505, 5600, 5602, 5603, 5604, 5605, 5606, 5630, 5670, 5701, 5702, 5704
modified: 1602, 5310, 5350, 5370

KM: 0
read: 5590
modified: 12, 5391, 5490

KR: 7
read: 92, 93, 470, 475, 670, 679, 680, 682, 684, 695, 697, 700, 702, 800, 810, 820, 850, 4100, 4110, 4113, 4130, 4150, 4200, 4300, 4330, 5282, 5283, 5284, 5285, 5304, 5305, 5600, 5602, 5603, 5604, 5605, 5630, 5670, 5701, 5702, 5704, 5800, 5801, 5802, 5856, 6300, 6400, 6450, 7002, 7504
modified: 5000, 5284, 6410

L: 0
read: 66, 70, 101, 141, 462, 485, 600, 610, 664, 671, 766, 767, 769, 4300, 4310, 4350, 4411, 4431, 5047, 5304, 5307, 5308, 5850, 5852, 5854, 5856, 6200, 6205, 6210, 6211, 6220
modified: 65, 460, 490, 510, 520, 600, 670, 695, 710, 715, 767, 769, 4300, 4310, 4350, 4411, 4413, 4431, 4433, 5603, 5704, 6210

L1: 16
read: 101, 102, 103, 106, 116, 141, 142, 143, 146, 156
modified: 101, 141

L2: 25
read: 101, 102, 103, 107, 116, 142, 143, 147, 156
modified: 101, 102, 141, 142

L3: 8
read: 106, 110, 146, 148
modified: 103, 143

L4: 12
read: 107, 110, 147, 148
modified: 103, 143

LC: 16
read: 92, 93, 475, 481, 485, 6210, 7002
modified: 485

LE: 250
read: 500
modified: 500

LL: 10
read: 850, 4411, 4413, 4431, 4433
modified: 800, 840, 4411, 4431

LO: 33457
read: 374, 402, 412
modified: 370

LR: 7
read: 840, 4130, 4400, 4410, 4411, 4412, 4413, 4431, 4432, 4433, 5607
modified: 4100, 4130, 4150, 5304, 5605, 5702

LV: 1
modified: 1601

M: 0
read: 650, 5110, 5120, 5164, 5210, 5250, 5260, 5284, 5293, 5294, 7320, 7360, 7400, 7440, 7504, 7506
modified: 5046, 5110, 5120, 5164, 5210, 5250, 5260, 5284, 5288, 5415, 6400, 6450, 7255, 7310, 7504 

MM: 4
read: 650
modified: 5000

N: 28
read: 696, 697, 702, 710, 715, 5801, 5802, 5803
modified: 695, 4400, 5800

NB: 0
read: 345, 500, 696, 4117, 5046, 5278, 7000, 7001, 7003, 7060, 7250, 7500
modified: 482, 702, 4110, 4200, 4300, 4310, 5284, 7002, 7510

NN: 1
read: 402, 412
modified: 372

NS: 5
read: 4410, 4430, 5606, 5607
modified: 4120, 5606, 5607

NX: 15
read: 148
modified: 148

NY: 21
read: 110
modified: 110

PA: 12
read: 7020
modified: 1210

PB: 7
read: 5410, 5824
modified: 1210, 5824

PC: 16
read: 68, 98, 650, 5410, 7050
modified: 98, 5000, 7050

PS: 5
read: 7031
modified: 1020

PU: 0
read: 480, 5045
modified: 475, 5010, 5820

PW: 0
read: 4300, 4350, 5010
modified: 1900, 5045, 6220

Q: 30
read: 9, 10, 13, 80, 1605, 1610, 1613, 1615, 1620, 1640, 1642, 1644, 1646
modified: 9

Q1: 12
read: 9, 4310
modified: 9

R: .418109828
read: 5420, 5430, 7020, 7040
modified: 990, 5420, 7020

RM: 2
read: 74, 1330, 5490, 5495
modified: 1020, 5495

RS: 20
read: 73, 1330, 5500, 5502
modified: 1020, 5502

SE: 250
read: 500
modified: 1210

SM: 0
read: 91, 5415, 5824
modified: 1010, 5824

SP: 12
read: 7030
modified: 1020

TA: 100
read: 650, 655, 660, 5100, 5390
modified: 650, 655, 5000

TC: .6
read: 4990, 5044, 5045, 12020, 12040
modified: 4990, 5000, 5044

V: 0

V1: 13
read: 56, 310, 450, 600, 670, 680, 4108, 4220, 5030, 5040, 5260, 5282, 5288, 5297, 5303, 5306, 5520, 5560, 5640, 5670
modified: 860

V2: 31
read: 56, 825, 4220, 5030, 5210, 5288, 5295, 5620
modified: 860

V3: 13
read: 860, 4414, 4430, 4431, 4433
modified: 850

V4: 31
read: 860, 4410, 4431
modified: 850

W1: 32
read: 54, 4220, 5030, 5120, 5288, 5298, 5660
modified: 860

W2: 0
read: 54, 310, 450, 600, 670, 680, 826, 4108, 4220, 5030, 5040, 5164, 5282, 5288, 5299, 5303, 5306, 5520, 5560, 5630, 5680
modified: 860

W3: 32
read: 860, 4410, 4411, 4430
modified: 850

W4: 0
read: 860, 4411, 4413, 4434
modified: 850

WC: 90
read: 52, 650, 1330, 5802, 5854
modified: 1210, 5802, 5854

WM: 105
read: 5430
modified: 1020, 5824

WT: 225
read: 650
modified: 5010

X: 26
read: 95, 5520, 5560, 5580
modified: 52, 59, 64, 78, 4113, 4990, 5044, 5390, 5520, 5560, 7020

X0: 7
read: 7010
modified: 5046

XA: 20
read: 65, 201, 830, 4108, 5040, 5210, 5260, 5282, 5294, 5295, 5297, 5303, 5306
modified: 1601, 5294, 5295, 5297

XB: 1
read: 65, 201, 310, 450, 600, 670, 680, 830, 4410, 4414, 4430, 4433, 5520, 5560, 5620, 5640, 5670  
modified: 4101

XL: 7
read: 600, 697, 5046, 5400, 5520, 5550, 5555, 5801, 5856, 7300, 7360, 7440
modified: 4108, 5282, 5306

XX: 19
read: 56, 104, 105, 106, 107, 110, 116, 141, 210, 220, 230, 240, 7300, 7302
modified: 56, 201, 4410, 4414, 4430, 4433, 5620, 5640, 5670, 7300

Y: 14
read: 96, 4113, 5520, 5580
modified: 52, 59, 62, 64, 78, 4113, 4990, 5044, 5390, 5520, 5560, 7020

Y0: 6
read: 7010
modified: 5046

YA: 6
read: 65, 201, 830, 4108, 5040, 5120, 5164, 5282, 5293, 5298, 5299, 5303, 5306
modified: 1601, 5293, 5298, 5299

YB: 42
read: 65, 201, 310, 450, 600, 670, 680, 830, 4410, 4413, 4430, 4434, 5520, 5560, 5630, 5660, 5680  
modified: 4101

YL: 6
read: 600, 697, 5046, 5400, 5510, 5515, 5560, 5801, 5856, 7300, 7320, 7400
modified: 4108, 5282, 5306

YY: 36
read: 54, 101, 144, 145, 146, 147, 148, 156, 210, 220, 230, 240, 680, 7300, 7306
modified: 54, 201, 680, 4410, 4413, 4430, 4434, 5630, 5660, 5680, 7300

Z: 59468
read: 51, 900, 1000
modified: 49

YM: value uninitialized
read: 54, 55, 310, 450, 5400, 5510, 5515, 5580, 7010, 7270, 7275, 7300, 7320, 7400
modified: 54, 55, 702, 825, 826, 4220, 7270, 7275, 7320, 7400

XM: value uninitialized
read: 56, 57, 310, 450, 5400, 5550, 5555, 5580, 7010, 7260, 7265, 7300, 7360, 7440
modified: 56, 57, 702, 825, 4220, 7260, 7265, 7360, 7440

MQ: value uninitialized
read: 310, 470, 482, 880, 4117, 4200, 4215, 5408, 5415, 5420, 5502, 5580, 5900, 7007, 7010, 7015, 7016, 7018, 7295, 7508, 11010
modified: 482, 4200, 4330

W: value uninitialized
read: 462
modified: 462

SS: value uninitialized
read: 481
modified: 800

HT: value uninitialized
read: 481, 12040
modified: 810, 10000, 11000, 12020

IJ: value uninitialized
read: 600, 5630, 5670
modified: 600, 5700

ML: value uninitialized
read: 710, 5410, 7020
modified: 710, 4210

MD: value uninitialized
read: 830, 6212, 7040
modified: 710, 4210, 6212

IB: value uninitialized
read: 4120, 5281, 5286, 5304, 5306
modified: 5110, 5120, 5164, 5210, 5260, 5284, 5288, 5307, 6410

MH: value uninitialized
read: 5437, 5450
modified: 4210

IH: value uninitialized
modified: 4210

MS: value uninitialized
read: 5410, 7310
modified: 4210

MA: value uninitialized
modified: 4210

MP: value uninitialized
read: 5450, 6215, 7500, 7508, 11010
modified: 4210, 5450, 6215

MF: value uninitialized
read: 7310
modified: 4250, 7302, 7306

LS: value uninitialized
read: 4310
modified: 4310

T0: value uninitialized
read: 4990

M1: value uninitialized
read: 5288
modified: 5110, 5164, 5250

P: value uninitialized
read: 5420, 5430, 7020, 7040
modified: 5410, 5415, 7020

AK: value uninitialized
read: 5430, 5437, 5450
modified: 5430, 5437, 5590

UY: value uninitialized
read: 5520
modified: 5510, 5515

S: value uninitialized
read: 5520, 5560
modified: 5510, 5515, 5550, 5555

LY: value uninitialized
read: 5520
modified: 5510, 5515

LX: value uninitialized
read: 5560
modified: 5550, 5555

UX: value uninitialized
read: 5560
modified: 5550, 5555

EX: value uninitialized
read: 5802, 12040
modified: 5802

IM: value uninitialized
read: 7017
modified: 7010, 7017


integers:
---------
C%: 32767
read: 65, 75, 76, 86, 110, 148, 370, 460, 910, 930, 965
modified: 12

J%: 920
read: 910, 920
modified: 900, 920

K%: value uninitialized
read: 715, 720
modified: 715


strings:
--------
A$: h" 100"
read: 62, 75, 76, 86, 660, 990, 1601, 1602, 1604, 1605, 1610, 1613, 1615, 1620, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647
modified: 68, 73, 74, 655, 660, 880, 990, 1601, 1602, 1604, 1605, 1610, 1613, 1615, 1620, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 4117, 4215, 4300

B1$: c"           "
read: 48, 59
modified: 48

B2$: h"             "
read: 64
modified: 48

BL$: h"              "
read: 78
modified: 48

C$: c""
read: 71, 510, 767, 5048, 5049, 5110, 5585
modified: 510, 5580

D$: c""
modified: 510

O$: c"RLATPFMGEV!USY◄OD"
read: 5049
modified: 5000


float arrays:
-------------
CH(col 0-6) = 0, 0, 14, 13, 15, 16, 0
read: 68, 98, 650, 1020, 5000, 5010, 5410, 5701, 5900, 6300
modified: 13, 1010

H(col 0-3) = 0, 6, 12, 18
modified: 12, 20

TM(col 0-5) = 0, 10, 13, 2, 1, 1
read: 11, 5415
modified: 21

ZA(col 0-3) = 0, 0, 3, -6
read: 11, 5410
modified: 29

ZD(col 0-5) = 3, 0, 3, -2, 5, 5
read: 11, 7020
modified: 29

R(): value uninitialized
read: 5420, 5590, 5701, 5900, 6140, 6215, 6300, 7020, 7030, 7255


integer arrays:
---------------
D1%(row 0-30, col 0-3) =
    0,  0,  0,  0
    0,  0,  0,  7
    0,  0,  0,  7
    5,  0,  0,  7
    5,  0,  0,  7
    0,  0,  0,  7
    5,  7,  0,  0
    6,  7,  4, 12
    0, 12,  0,  0
    0,  2,  0,  0
    0,  2,  2,  2
    0,  0,  0,  6
   12,  7,  0,  0
    0,  0,  5,  0
    0,  0, 12,  0
    0,  0, 21,  5
    4,  7,  0,  0
    5,  5,  5,  0
    0,  0,  4,  0
    5,  7,  0,  0
    0,  0, 15,  6
    3,  0,  3,  0
    4,  6,  4,  0
    3,  0,  0,  0
    0, 12,  5,  0
   16,  7,  0,  0
    5,  0,  0,  0
    0,  0,  2, 12
    5,  0,  0,  4
    0, 12,  3,  0
    0,  0, 21, 12
read: 10, 4411, 4431, 4433, 5283, 5600, 5603, 5670, 5704
modified: 1613
Comment: TODO: loaded from 2nd file

D2%(row 0-30, col 0-3) =
    0,  0,  0,  0
    0,  0,  0, 12
    0,  0,  0, 12
    9,  0,  0, 12
    9,  0,  0, 12
    0,  0,  0, 12
    9, 12,  0,  0
   11, 12, 14, 17
    0, 17,  0,  0
    0,  6,  0,  0
    0,  6,  7,  6
    0,  0,  0, 10
   18, 12,  0,  0
    0,  0,  9,  0
    0,  0, 18,  0
    0,  0, 25, 10
    9, 12,  0,  0
    9, 10,  9,  0
    0,  0,  9,  0
    9, 12,  0,  0
    0,  0, 19, 11
    6,  0,  6,  0
    9, 11,  9,  0
    6,  0,  0,  0
    0, 17, 10,  0
   22, 12,  0,  0
   10,  0,  0,  0
    0,  0,  8, 17
    9,  0,  0,  9
    0, 17,  6,  0
    0,  0, 25, 17
read: 10, 4411, 4413, 4431, 5283, 5602, 5603, 5630, 5704
modified: 1615
Comment: TODO: loaded from 2nd file

K%(col 0-2) = 0, 160, 32
read: 9, 110, 148
modified: 49

LS%(col 0-2) = 4, 1, 8
read: 12, 19, 310
modified: 19

M%(row 0-12, col 0-9) =
    0,  0,  1,  0,  0,  0,  0,  0,  0,  0
    3,  0,  6,  0,  3,  1,  2,  5,  0,  1
    0,  2, 11,  2,  3,  0,  3,  2,  7, 10
    3,  1,  6,  0,  9,  1,  1,  3, 25,  8
    4,  1,  8,  0, 11,  2,  1,  1, 15,  7
    4,  1,  2,  0,  7,  1,  2,  0, 13,  9
    2,  1, 10,  0, 13,  1,  1,  3, 20,  4
    3,  2,  5,  0,  8,  3,  2,  2, 10,  5
    0,  1, 12,  0, 14,  4,  1,  1,  5,  4
    2,  1, 10,  0, 12,  5,  1,  0,  0,  3
    1,  5, 20,  0, 12,  0,  3,  0,  5,  2
    6,  3, 10,  2,  8,  0,  3,  0,  0, 10
    6,  0,  8,  0,  5,  2,  1,  1,  0, 12
read: 9, 310, 4210, 4310, 5408, 5415, 5502, 5900, 7010
modified: 1650, 1900
Comment: TODO: loaded from 2nd file

MT%(row 0-30, col 0-7) =
    0,  0,  0,  0,  0,  0,  0,  0
    9,  1,  2,  7,  6,  0,  2,  2
    0,  0,  2, 10,  6,  0,  2,  2
    0,  0,  2, 10, 12,  0,  2,  2
    0,  0,  2,  4, 13,  0,  2,  2
    0,  0,  2,  3,  6,  0,  2,  2
    5,  3,  2,  7, 15,  0,  2,  2
    0,  0,  0,  2,  2,  0,  2,  2
    5,  4,  0,  2,  2, 12,  7, 29
    3,  3,  1, 13,  5,  8,  4,  8
    0,  0,  1,  3,  4,  3, 10,  9
    0,  0,  1,  4,  5,  0,  2,  2
    3,  1,  2, 19, 13,  7,  9,  3
    9,  1,  3, 10,  8, 11,  4,  8
    1,  1,  0, 30, 16,  5,  6, 19
    0,  0,  1, 25,  5,  9,  5, 15
    0,  0,  5, 10,  8,  0,  2,  2
    0,  0,  3,  4, 11,  0,  2,  2
   10,  1,  0,  2,  2,  1, 17,  5
    7,  1,  1, 27, 12,  0,  2,  2
    6,  1,  0,  2,  2, 10, 21, 16
    0,  0,  3,  3,  3,  0,  2,  2
    0,  0,  0,  9, 10,  0,  2,  2
    0,  0,  3,  3,  3,  2,  3,  3
    7,  1,  3,  3,  8,  6,  4, 10
    4,  2,  0,  2,  2,  5,  5,  5
   10,  1,  0, 15,  4,  0,  2,  2
    0,  0,  0, 15, 15,  0,  2,  2
    0,  0,  4,  3,  3,  0,  2,  2
    4,  1,  8,  4, 13,  8,  4, 17
    8,  1,  2, 10, 12,  4, 15, 14
read: 10, 670, 679, 680, 682, 684, 695, 697, 702, 820, 4110, 4200, 5800, 5801, 5856, 6300, 7504    
modified: 470, 485, 700, 1620, 4330, 5802, 5856, 7504
Comment: TODO: loaded from 2nd file

N%(row 0-30, col 0-3) =
    0,  0,  0,  0
    0,  0,  0,  2
    0,  0,  0,  2
    2,  0,  0,  2
    2,  0,  0,  2
    0,  0,  0,  2
    3,  2,  0,  0
    1,  2,  2,  2
    0,  2,  0,  0
    0,  1,  0,  0
    0,  2,  1,  1
    0,  0,  0,  2
    2,  2,  0,  0
    0,  0,  3,  0
    0,  0,  2,  0
    0,  0,  2,  2
    2,  2,  0,  0
    3,  2,  2,  0
    0,  0,  2,  0
    2,  2,  0,  0
    0,  0,  2,  2
    2,  0,  3,  0
    2,  2,  2,  0
    3,  0,  0,  0
    0,  2,  3,  0
    2,  2,  0,  0
    3,  0,  0,  0
    0,  0,  2,  2
    2,  0,  0,  2
    0,  2,  2,  0
    0,  0,  3,  2
read: 10, 4130, 4412, 4432, 5282, 5600, 5701
modified: 1610, 5604, 5607, 5702
Comment: TODO: loaded from 2nd file

NO%(row 0-30, col 0-3) =
    0,  0,  0,  0
    0,  0,  0,  7
    0,  0,  0, 12
   15,  0,  0, 19
   20,  0,  0, 16
    0,  0,  0, 25
   30, 28,  0,  0
   10,  1,  0,  8
    0,  7,  0,  0
    0, 10,  0,  0
    0, 11,  7,  9
    0,  0,  0, 10
   14,  2,  0,  0
    0,  0, 17,  0
    0,  0, 12,  0
    0,  0,  3, 17
   22,  4,  0,  0
   13, 15, 19,  0
    0,  0, 22,  0
   17,  3,  0,  0
    0,  0,  4, 22
   29,  0, 23,  0
   18, 20, 16,  0
   21,  0,  0,  0
    0, 30, 26,  0
   27,  5,  0,  0
   24,  0,  0,  0
    0,  0, 25, 29
   11,  0,  0, 10
    0, 27, 21,  0
    0,  0,  6, 24
read: 10, 93, 4130, 5284, 5605
modified: 1605
Comment: TODO: loaded from 2nd file

NR%(col 0-1, row 0-1) =
   8, 4
   2, 1
read: 13, 372
modified: 43

P%(col 0-4) = 6, 7, 6, 7, 6
read: 11, 5040, 5283, 5303, 5600, 5602
modified: 5040, 5303

RT%(col 0-30) = 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 13, 4100, 4400
modified: 80, 4410

S%(col 0-4) = 0, 32, 18, 0, 0
read: 5602
modified: 11, 5030, 5288

SI%(col 0-12) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 13, 664, 800, 810, 830, 832, 5045, 5803
modified: 664, 1030, 5803, 6212

T%(row 0-12, col 0-5) =
     0,   0,   0,   0,   0,   0
     0,   0,  60,   3,   0,   0
     1,   1,  90,   9,   0,   0
     1,   2,  95,   0,   1,   3
     0,   4, 100,   0,   2,  50
    81,   0, 100,  12,   0,   0
     3,   5,   0,   0,   0,   0
   190,   6,   0,   0,   0,   0
     0,   7,   0,   0,   0,   0
     0,   0,   0,   0,   0,   0
     3,   3,   0,   0,   0,   0
     0,   4,   0,   0,   0,   0
     2,   8,   0,   0,   0,   0
read: 664, 697, 702, 710, 715, 5802, 5803, 5854, 6210
modified: 9, 1660
Comment: TODO: loaded from 2nd file

TB%(col 0-15) = 32, 108, 123, 98, 124, 225, 255, 254, 126, 127, 97, 252, 226, 251, 236, 160        
read: 13, 376, 402, 412
modified: 43

TT%(col 0-12) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 13, 5802, 5852, 6205
modified: 5802, 5854, 6212

TX%(row 0-3, col 0-1) =
    1,  1
    1,  2
   -1, -1
   -1, -2
read: 11, 600
modified: 20
Comment: TODO: loaded from 2nd file

TY%(row 0-3, col 0-1) =
   -1, -2
    1,  1
    1,  2
   -1, -1
read: 11, 600
modified: 20
Comment: TODO: loaded from 2nd file

X1%(col 0-30) = 0, 29, 29, 29, 29, 29, 29, 13, 1, 1, 17, 29, 1, 1, 1, 13, 1, 1, 1, 1, 19, 1, 1, 1, 1, 7, 1, 21, 28, 1, 13
read: 9, 850, 1641
modified: 1640, 1641

X2%(col 0-30) = 0, 43, 43, 43, 43, 43, 43, 31, 15, 19, 31, 43, 31, 15, 43, 43, 31, 15, 21, 31, 43, 9, 21, 9, 15, 31, 31, 43, 35, 23, 43
read: 13, 850, 1645
modified: 1644, 1645

XS%(row 0-9, col 0-2) =
    0,  0, -1
   -1,  0,  0
    1,  0,  1
    0,  0, -1
    0,  0,  1
    0,  0, -1
    0,  0,  1
    0,  0,  0
    0,  0,  0
    0,  0,  0
read: 12, 310
modified: 19
Comment: TODO: loaded from 2nd file

Y1%(col 0-30) = 0, 20, 20, 20, 20, 20, 20, 32, 32, 42, 42, 42, 20, 42, 42, 42, 20, 32, 42, 20, 42, 20, 34, 8, 42, 20, 20, 42, 60, 42, 42
read: 850, 1643
modified: 10, 1642, 1643

Y2%(col 0-30) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 30, 26, 0, 30, 18, 18, 0, 18, 32, 0, 18, 6, 18, 0, 18, 0, 0, 18, 67, 18, 18
read: 13, 850, 1647
modified: 1646, 1647

YS%(row 0-9, col 0-2) =
   -1,  0, -1
    0,  0, -1
    0,  0, -1
    1,  0,  0
    0,  0,  0
    0,  0,  1
    0,  0,  1
    0,  0,  1
    0,  0,  0
    0,  0,  0
read: 12, 310
modified: 19
Comment: TODO: loaded from 2nd file


string arrays:
--------------
M$(13) =
   M$(0) = c""
   M$(1) = h"SALAMANDER"
   M$(2) = h"FIRE ELEMENTL"
   M$(3) = h"HOUND"
   M$(4) = h"DIRE WOLF"
   M$(5) = h"VAMPIRE BAT"
   M$(6) = h"OGRE"
   M$(7) = h"GOLEM"
   M$(8) = h"GOLEM"
   M$(9) = h"SUIT OF ARMOR"
   M$(10) = h"CREEPING CRUD"
   M$(11) = h"GENIE"
   M$(12) = h"ÍORLOC"
read: 9, 880, 4117, 4215
modified: 1650

NS$(3) =
   NS$(0) = c""
   NS$(1) = c""
   NS$(2) = c""
read: 13

SD$(20) =
   SD$(0) = c"ROOM NO.:    "
   SD$(1) = c" "
   SD$(2) = c"WOUNDS:     %"
   SD$(3) = c"FATIGUE:    %"
   SD$(4) = c" "
   SD$(5) = c"WGT:     LBS"
   SD$(6) = c" "
   SD$(7) = c"ARROWS:     "
   SD$(8) = c"MAGIC AR:    "
   SD$(9) = c" "
   SD$(10) = c" "
   SD$(11) = c" "
   SD$(12) = c"°ÀÀÀÀÀÀÀÀÀÀÀÀÀ®"
   SD$(13) = c"Ý             Ý"
   SD$(14) = c"Ý             Ý"
   SD$(15) = c"­ÀÀÀÀÀÀÀÀÀÀÀÀÀ½"
   SD$(16) = c"°ÀÀÀÀÀÀÀÀÀÀÀ®"
   SD$(17) = c"Ý           Ý"
   SD$(18) = c"Ý           Ý"
   SD$(19) = c"­ÀÀÀÀÀÀÀÀÀÀÀ½"
read: 13, 48, 4113
modified: 48

T$(3) =
   T$(0) = c""
   T$(1) = c""
   T$(2) = c"6 FLOORS DOWN"
read: 9, 720
modified: 24
'''

if __name__ == "__main__":
    mem = c64_morlocs_tower_mem_dump()
