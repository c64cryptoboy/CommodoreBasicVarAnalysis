import basicVarAnalysis

# Process variables in a VIC-20 (16K-expanded) memory dump of Sword of Fargoal (Epyx, 1982)
# https://sleepingelephant.com/denial/wiki/index.php?title=Sword_of_Fargoal

def vic20_sword_of_fargoal_mem_dump():
    mem = basicVarAnalysis.MemoryDump('VIC20+8K+')
    mem.find_vars("test_data/vic20_SOF.bin")

    mem.add_formatting("A",  comment = "char for player graphic")
    mem.add_formatting("A$", comment = "keyboard input")
    mem.add_formatting("A1", comment = "counter to balance key input with monster movement")
    mem.add_formatting("B",  comment = "joystick direction") 
    mem.add_formatting("BG", comment = "count of magic sacks in inventory")
    mem.add_formatting("BS", comment = "battle skill")
    mem.add_formatting("C",  comment = "a screen character")
    mem.add_formatting("CL", comment = "1 = trap sprung, 0 = evaded")  
    mem.add_formatting("CM", comment = "an offset used for color memory")  
    mem.add_formatting("D%", comment = "the constant 506 (= 22 * 23 screen locations)")  
    mem.add_formatting("DD", comment = "VIA2 DDR register")      
    mem.add_formatting("DE", comment = "deepest level reached")
    mem.add_formatting("E",  comment = "experience points")
    mem.add_formatting("EL", comment = "experience level")            
    mem.add_formatting("FA", comment = "count of drift spells in inventory")
    mem.add_formatting("F3", comment = "used to keep opponent from getting stuck when moving")
    mem.add_formatting("FL", comment = "1 if leaving a fight via teleport spell")      
    mem.add_formatting("FR", comment = "joystick fire button")      
    mem.add_formatting("GD", comment = "gold bury count for level (0 to 9)")       
    mem.add_formatting("HP", comment = "count of healing potions in inventory")
    mem.add_formatting("HT", comment = "hit points")    
    mem.add_formatting("IV", comment = "count of invisibility spells in inventory")
    mem.add_formatting("K",  comment = "value at a screen location under player") 
    mem.add_formatting("L",  comment = "current dungeon level")       
    mem.add_formatting("L1", comment = "current light spell: 0=none, 1=on, 2=off")    
    mem.add_formatting("LG", comment = "count of light spells in inventory")
    mem.add_formatting("M",  comment = "a memory address")
    mem.add_formatting("M2", comment = "0 if opponent is monster, 1 if human-like")    
    mem.add_formatting("MK", comment = "count of opponents killed")    
    mem.add_formatting("N1", comment = "oscillator 1 freq register")
    mem.add_formatting("N2", comment = "oscillator 2 freq register")
    mem.add_formatting("N3", comment = "oscillator 3 freq register")
    mem.add_formatting("N4", comment = "noise freq register")
    mem.add_formatting("NM", comment = "number of non-human opponents on level")    
    mem.add_formatting("NN", comment = "number of human-like opponents on level")
    mem.add_formatting("O",  comment = "screen memory offset")  
    mem.add_formatting("PA", comment = "port A (for joystick reads)")
    mem.add_formatting("PB", comment = "port B (for joystick reads)")
    mem.add_formatting("PL", comment = "enchanted weapon level")    
    mem.add_formatting("QL", comment = "dungeon level that contains the sword of fargoal")        
    mem.add_formatting("R1", comment = "regeneration rate")
    mem.add_formatting("R2", comment = "1 = player in temple, 0 if not")      
    mem.add_formatting("RG", comment = "count of regenerate spells in inventory")
    mem.add_formatting("S",  comment = "monster speed")
    mem.add_formatting("S1", comment = "1 if shield spell active")
    mem.add_formatting("SF", comment = "1 if sword of fargoal in inventory")   
    mem.add_formatting("SH", comment = "count of shield spells in inventory")
    mem.add_formatting("SR", comment = "start-of-game indicator")
    mem.add_formatting("T",  comment = "gold in inventory")
    mem.add_formatting("T3", comment = "game timer after sword found")
    mem.add_formatting("T4", comment = "total game time")
    mem.add_formatting("TH", comment = "maximum hit points")  
    mem.add_formatting("TM", comment = "number of maps in inventory")        
    mem.add_formatting("TP", comment = "count of teleport spells in inventory")
    mem.add_formatting("V1", comment = "1 if player is invisible, 0 if not")
    mem.add_formatting("V2", comment = "volume")
    mem.add_formatting("V3", comment = "computed values for sound effects")  
    mem.add_formatting("X1", comment = "opponent skill divided by player's battle skill")

    mem.add_formatting("A$()", comment = 'monster "A"s or "AN"s')
    mem.add_formatting("B$()", comment = "monster names")    
    mem.add_formatting("B%()", comment = "human-like opponents'hit points")
    mem.add_formatting("C$()", comment = 'human-like opponents'' "A"s or "AN"s')    
    mem.add_formatting("D()",  comment = "22-col direction offsets")
    mem.add_formatting("D$()", comment = "human-like opponents'names")     
    mem.add_formatting("G%()", comment = "piles of buried gold (up to 10)")        
    mem.add_formatting("H%()", comment = "monsters' hit points")
    mem.add_formatting("J%()", comment = "joystick screen-offset decoding for x,y")
    mem.add_formatting("M%()", comment = "monster-likes' locations")      
    mem.add_formatting("N%()", comment = "human-like opponents' locations")    
    mem.add_formatting("R%()", comment = "human-like opponents' skill levels")
    mem.add_formatting("S$()", comment = "monster battle sounds")             
    mem.add_formatting("S%()", comment = "monsters' skill levels")
    mem.add_formatting("T$()", comment = "human-like opponents' battle sounds")      
    mem.add_formatting("T%()", comment = "list of up to 10 level maps (unsorted)")
    mem.add_formatting("V()",  comment = "constants used in random dungeon creation")
    mem.add_formatting("V%()", comment = "sound data")
    mem.add_formatting("W%()", comment = "sound data")
    mem.add_formatting("X()",  comment = "character to display for monster types")
    mem.add_formatting("Y()",  comment = "character to display for human-like types")
    mem.add_formatting("X$()", comment = "monster descriptions for level")              
    mem.add_formatting("X%()", comment = "sound data")
    mem.add_formatting("Y$()", comment = "human-like opponent descriptions for level")      
    mem.add_formatting("Y%()", comment = "sound data")           
    mem.add_formatting("Z%()", comment = "sound data") 

    mem.print_basic_ranges()
    mem.print_variables()    
    return mem

'''
parsing vars from memory dump...
- 24576 bytes (assuming $0000 to $5FFF)
- BASIC line number: 38
- BASIC line number on last exit: 0

BASIC ranges:
-------------
TXTTAB $1601/5633: start of BASIC (default $1201/4609), 12723-byte extent
VARTAB $47B3/18355: start of variables, 483-byte extent
ARYTAB $4996/18838: start of arrays, 1189-byte extent
STREND $4E3B/20027: end of arrays (exclusive)
FRETOP $5FCD/24525: end (bottom) of string heap, 51-byte extent
MEMSIZ $6000/24576: start (top) of string heap + 1

floats:
-------
A: 26
read: 33, 52, 63, 171, 178, 207, 226, 272, 311, 329
modified: 343
Comment: char for player graphic

A1: 8
read: 38
modified: 38
Comment: counter to balance key input with monster movement

B: 0
read: 57, 60, 264, 279
modified: 143
Comment: joystick direction

BS: 13
read: 3, 88, 187, 217, 228, 236, 246, 265, 272, 325, 343
modified: 88, 187, 228, 272, 343
Comment: battle skill

C: 41
read: 22, 147, 220, 231, 287, 297, 317
modified: 8, 28, 279, 283, 287
Comment: a screen character

CM: 33792
read: 33, 52, 60, 63, 112, 140, 166, 167, 178, 207, 304, 317
modified: 338
Comment: an offset used for color memory

D: 1
read: 147, 220, 275, 290, 305, 311, 315
modified: 28, 213, 215, 226, 259, 263, 282, 287

DD: 37154
read: 143, 145
modified: 343
Comment: VIA2 DDR register

DE: 1
read: 3, 325
modified: 3
Comment: deepest level reached

EL: 1
read: 3, 88, 234, 325, 332
modified: 88, 234, 343
Comment: experience level

EP: 200
read: 58, 88
modified: 88, 347

F: 2
read: 21
modified: 17, 18

F2: 0
read: 310
modified: 293, 310

FL: 0
read: 283, 288
modified: 231, 232, 283
Comment: 1 if leaving a fight via teleport spell

GD: 0
read: 95, 96, 155, 156, 160
modified: 2, 96, 156
Comment: gold bury count for level (0 to 9)

H: 2
read: 8
modified: 8

HP: 1
read: 41, 53, 83, 103, 183
modified: 53, 183, 347
Comment: count of healing potions in inventory

HT: 11
read: 37, 53, 55, 56, 168, 202, 219, 222, 223, 268, 279, 325, 343, 347
modified: 53, 56, 168, 202, 219, 268, 343
Comment: hit points

I: 9
read: 8, 28, 40, 112, 113, 115, 116, 118, 120, 123, 124, 128, 130, 140, 148, 149, 150, 242, 243, 244, 252, 253, 254, 329
modified: 8, 28, 40, 82, 112, 113, 115, 116, 118, 120, 122, 123, 124, 128, 130, 140, 145, 147, 148, 156, 276, 325, 329, 335, 338, 343, 347

I1: 2
read: 33, 102, 126, 133, 134, 135, 136, 137, 209
modified: 33, 102, 118, 120, 126, 133, 134, 135, 136, 137, 209, 320

I2: 16
read: 134, 209
modified: 126, 134, 136, 137, 209

J: 1
read: 8, 22, 118, 120, 122, 123, 124, 130, 140, 160, 166, 168, 212, 213, 214, 215, 226, 231, 232, 256, 260, 282, 283, 285, 286, 287, 290, 329
modified: 8, 17, 22, 88, 113, 116, 118, 120, 122, 123, 124, 128, 130, 140, 160, 166, 205, 236, 246, 256, 260, 282, 286, 329, 343

K: 32
read: 33, 52, 60, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 95, 98, 99, 100, 102, 154, 156, 163, 168, 171, 172, 173, 177, 178, 180, 231, 257, 261, 272, 275, 279, 294, 311
modified: 52, 60, 62, 79, 98, 99, 100, 154, 156, 163, 168, 171, 172, 173, 177, 178, 180, 193, 228, 231, 257, 261, 272, 275, 347
Comment: value at a screen location under player

L: 1
read: 2, 3, 5, 7, 27, 28, 33, 53, 98, 99, 153, 168, 172, 174, 177, 180, 188, 193, 219, 221, 228, 236, 240, 246, 250, 266, 268, 272, 332
modified: 98, 99, 174, 193, 343
Comment: current dungeon level

L1: 0
read: 48, 63, 91, 287, 295
modified: 2, 44, 91, 92
Comment: current light spell: 0=none, 1=on, 2=off

M: 4751.5
read: 8, 18, 19, 22, 24, 79, 107, 154, 156, 163, 171, 172, 177, 178, 180, 231, 232, 256, 257, 260, 261, 272, 275
modified: 8, 18, 24, 63, 209
Comment: a memory address

M2: 0
read: 209, 231, 270, 272, 291, 313, 316
modified: 70, 71, 282, 286
Comment: 0 if opponent is monster, 1 if human-like

N: 4256
read: 27, 28, 33, 52, 110, 112, 147, 148, 149, 150, 178
modified: 110, 112, 148, 149, 150

N1: 36874
read: 113, 115, 116, 120, 126, 136, 137, 139
modified: 338
Comment: oscillator 1 freq register

N2: 36875
read: 118, 120, 123, 124, 126, 134, 139, 209
modified: 338
Comment: oscillator 2 freq register

N3: 36876
read: 40, 115, 118, 120, 122, 123, 124, 126, 128, 130, 133, 139, 209
modified: 338
Comment: oscillator 3 freq register

N4: 36877
read: 64, 113, 116, 128, 134, 135, 136, 137, 139, 166, 168
modified: 338
Comment: noise freq register

NM: 2
read: 28, 256, 282
modified: 28
Comment: number of non-human opponents on level

NN: 0
read: 28, 260, 286
modified: 28
Comment: number of human-like opponents on level

O: 4233
read: 33, 52, 60, 63, 96, 102, 108, 112, 148, 150, 156, 160, 166, 167, 168, 171, 172, 174, 177, 178, 207, 209, 272, 320, 329
modified: 33, 52, 60, 62, 178
Comment: screen memory offset

P: 255
read: 18, 21, 110, 143, 145, 285, 290, 297, 303, 304, 305, 313, 314, 316, 322
modified: 18, 110, 143, 145, 226, 283, 287, 305, 310, 311, 313, 314, 323

P1: 0
read: 174, 193, 203
modified: 2, 100, 172, 173

PA: 37137
read: 143, 145
modified: 343
Comment: port A (for joystick reads)

PB: 37152
read: 143
modified: 343
Comment: port B (for joystick reads)

QL: 17
read: 27
modified: 347
Comment: dungeon level that contains the sword of fargoal

R: 1
read: 8, 147, 165, 196, 241, 251, 320
modified: 8, 28, 165, 241, 251, 320

R1: 50
read: 45, 56, 59, 86
modified: 2, 45, 59, 86
Comment: regeneration rate

S: 19
read: 2, 38
modified: 2
Comment: monster speed

SP: 122
read: 56
modified: 56

SR: 0
read: 25
modified: 25, 347
Comment: start-of-game indicator

T1: 100
read: 153, 156, 158, 161, 164, 184
modified: 184, 347

T4: 1214
read: 328
modified: 343
Comment: total game time

TH: 11
read: 3, 53, 56, 88
modified: 88, 347
Comment: maximum hit points

TP: 1
read: 42, 52, 103, 190, 200, 230
modified: 52, 190, 233, 347
Comment: count of teleport spells in inventory

V: 1
read: 16, 62, 124, 130, 161, 164, 257, 259, 261, 263, 271, 272, 275, 276, 278
modified: 15, 60, 68, 69, 98, 99, 130, 160, 256, 260

V2: 36878
read: 40, 64, 113, 115, 116, 118, 120, 122, 123, 124, 126, 128, 130, 133, 134, 135, 136, 137, 139, 168, 209
modified: 338
Comment: volume

W: 3
read: 8, 98, 99, 124, 131, 132, 291, 292, 310
modified: 8, 68, 69, 98, 99, 291, 297

W0: 0
read: 143
modified: 143

W1: 0
read: 126, 143
modified: 125, 143, 180, 272

W2: 0
read: 126, 143
modified: 126, 143

W3: 0
read: 126, 143
modified: 125, 143, 180, 272

X: 1
read: 8, 20, 53, 107, 140, 143, 147, 148, 153, 154, 156, 174, 176, 180, 188, 193, 236, 240, 243, 244, 246, 250, 253, 254, 266, 268, 293, 299, 300, 307, 329
modified: 8, 53, 65, 107, 108, 140, 143, 147, 148, 153, 174, 180, 188, 236, 240, 241, 246, 250, 251, 265, 296, 329, 343

XL: 20
read: 293, 299, 300, 307
modified: 108

Y: 1
read: 8, 22, 107, 108, 140, 143, 174, 236, 239, 246, 249, 293, 301, 302, 307
modified: 8, 17, 107, 108, 140, 143, 174, 236, 246, 296

YL: 16
read: 108, 293, 301, 302, 307
modified: 108

Z: 372
read: 15, 16, 18, 24, 108, 161, 163, 164, 305, 308, 309, 311
modified: 8, 16, 108, 161, 297, 303, 308, 309, 310

Z1: 15
read: 293, 319
modified: 293

Z2: 10
read: 293, 319
modified: 293

E: value uninitialized
read: 3, 37, 58, 79, 86, 98, 176, 180, 228, 234, 272, 325
modified: 79, 86, 98, 176, 180, 228, 234, 272
Comment: experience points

T2: value uninitialized
read: 5, 6, 79
modified: 79

MK: value uninitialized
read: 5, 228, 272, 325
modified: 228, 272
Comment: count of opponents killed

T3: value uninitialized
read: 6, 7, 325, 328
modified: 6, 325, 328
Comment: game timer after sword found

SF: value uninitialized
read: 27, 28, 220, 225
modified: 79, 225
Comment: 1 if sword of fargoal in inventory

TM: value uninitialized
read: 33, 102, 188
modified: 188
Comment: number of maps in inventory

T: value uninitialized
read: 37, 49, 86, 96, 153, 154, 156, 161, 163, 164, 220, 226, 276
modified: 86, 96, 154, 158, 163, 164, 226, 276
Comment: gold in inventory

SH: value uninitialized
read: 43, 103, 185
modified: 43, 185, 233
Comment: count of shield spells in inventory

S1: value uninitialized
read: 168, 218, 267
modified: 43, 170, 228, 272, 280
Comment: 1 if shield spell active

LG: value uninitialized
read: 44, 103, 186
modified: 44, 186, 233
Comment: count of light spells in inventory

RG: value uninitialized
read: 45, 103, 182
modified: 45, 182, 233
Comment: count of regenerate spells in inventory

SK: value uninitialized
read: 65
modified: 46, 65

IV: value uninitialized
read: 47, 103, 192
modified: 47, 192, 233
Comment: count of invisibility spells in inventory

V1: value uninitialized
read: 295
modified: 47, 272
Comment: 1 if player is invisible, 0 if not

R2: value uninitialized
read: 59
modified: 59, 86
Comment: 1 = player in temple, 0 if not

Q: value uninitialized
read: 62
modified: 60

P2: value uninitialized
read: 174
modified: 100, 173

FA: value uninitialized
read: 103, 191, 197, 198
modified: 191, 198, 233
Comment: count of drift spells in inventory

BG: value uninitialized
read: 103, 184
modified: 184
Comment: count of magic sacks in inventory

PL: value uninitialized
read: 103, 187, 221, 266
modified: 187
Comment: enchanted weapon level

V3: value uninitialized
read: 134, 137
modified: 134, 137
Comment: computed values for sound effects

FR: value uninitialized
read: 145, 194, 216, 223
modified: 145
Comment: joystick fire button

CL: value uninitialized
read: 206
modified: 168, 172, 177, 178, 198, 201, 208
Comment: 1 = trap sprung, 0 = evaded

H1: value uninitialized
read: 202, 228, 272
modified: 172, 174, 177, 217, 265

PT: value uninitialized
read: 174, 176
modified: 173

F1: value uninitialized
modified: 196

X1: value uninitialized
read: 219, 220, 221
modified: 217
Comment: opponent skill divided by player's battle skill

DY: value uninitialized
read: 303, 309
modified: 297, 301, 302

DX: value uninitialized
read: 303, 308, 309
modified: 297, 299, 300

F3: value uninitialized
read: 308, 309
modified: 297, 308, 309
Comment: used to keep opponent from getting stuck when moving

M1: value uninitialized
read: 303, 304, 311, 317, 322
modified: 297, 311, 323

K2: value uninitialized
read: 304, 320, 322
modified: 303, 320, 322

K1: value uninitialized
read: 311, 315, 317
modified: 311

M3: value uninitialized
read: 320, 322, 323
modified: 320


integers:
---------
D%: 506
read: 33, 52, 63, 96, 102, 112, 149, 150, 178, 209, 297, 322, 329
modified: 338
Comment: the constant 506 (= 22 * 23 screen locations)

H%: 15
read: 217, 221, 236, 244, 246, 254, 265, 266, 271, 278
modified: 213, 215, 221, 236, 244, 246, 254, 259, 263, 266

M%: 4974
read: 108, 282, 285, 286, 290, 297, 303, 305, 311, 317, 322
modified: 225, 228, 235, 282, 286, 311, 315, 316, 322

S%: 9
read: 212, 214, 217, 228, 236, 244, 246, 254, 257, 261, 265, 272
modified: 212, 214, 236, 244, 246, 254, 257, 261


strings:
--------
A$: h""
read: 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 334, 335, 336
modified: 38, 334
Comment: keyboard input

S$: h"A "
read: 94, 243, 244, 253, 254
modified: 43, 44, 45, 47, 236, 239, 243, 246, 249, 253

P$: value uninitialized
read: 176
modified: 100, 173

X$: value uninitialized
read: 216, 222, 228, 264, 272
modified: 213, 215, 259, 263


float arrays:
-------------
A(col 0-10) = 31, 27, 27, 0, 0, 0, 0, 0, 0, 0, 0
read: 28, 283
modified: 242, 243

B(col 0-10) = 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 28, 287
modified: 252, 253

D(col 0-10) = 0, 1, -1, 22, -22, -21, 21, -23, 23, 0, 0
read: 18, 24, 112, 148, 149, 320
modified: 343
Comment: 22-col direction offsets

E(col 0-10) = 0, 43, 38, 61, 59, 0, 0, 0, 0, 0, 0
read: 168
modified: 347

R(col 0-10) = 0, 4787.5, 4991, 4939.5, 4914.5, 5029, 4978, 4830.5, 5044, 5002.5, 4764.5
read: 8
modified: 8

V(col 0-10) = 0, 2, 1, 4, 3, 0, 0, 0, 0, 0, 0
read: 16
modified: 343
Comment: constants used in random dungeon creation

X(col 0-10) = 31, 27, 27, 27, 28, 27, 30, 29, 30, 30, 0
read: 243
modified: 347
Comment: character to display for monster types

Y(col 0-10) = 42, 41, 41, 43, 41, 41, 41, 41, 40, 41, 0
read: 253
modified: 347
Comment: character to display for human-like types

W(): value uninitialized
modified: 148

F(): value uninitialized
read: 150

G(): value uninitialized
read: 276
modified: 226


integer arrays:
---------------
A%(col 0-4) = 8, 10, 15, 0, 0
read: 213, 259, 343
modified: 244, 271

B%(col 0-3) = 7, 0, 0, 0
read: 215, 263, 343
modified: 254, 278
Comment: human-like opponents'hit points

C%(col 0-10) = 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 4
read: 120
modified: 338

D%(col 0-3) = 1, 0, 0, 0
read: 263, 287, 343
modified: 28, 290

J%(col 0-2, row 0-2) =
   -23, -22, -21
   -1, 0, 1
   21, 22, 23
read: 143, 343
modified: 343
Comment: joystick screen-offset decoding for x,y

M%(col 0-4) = 4983, 4881, 4978, 0, 0
read: 256, 282
modified: 28, 232, 257, 272, 285, 343
Comment: monster-likes' locations

N%(col 0-3) = 4974, 0, 0, 0
read: 260, 286, 343
modified: 28, 231, 261, 275, 290
Comment: human-like opponents' locations

P%(col 0-4) = 32, 32, 32, 0, 0
read: 257, 272, 283, 343
modified: 28, 285

Q%(col 0-3) = 32, 0, 0, 0
read: 261, 275, 287, 343
modified: 28, 290

R%(col 0-3) = 11, 0, 0, 0
read: 214, 261, 343
modified: 252, 254
Comment: human-like opponents' skill levels

S%(col 0-4) = 2, 11, 9, 0, 0
read: 212, 257, 343
modified: 242, 244
Comment: monsters' skill levels

T%(col 0-10) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 33
modified: 102, 188
Comment: list of up to 10 level maps (unsorted)

V%(col 0-10) = 157, 157, 157, 157, 172, 169, 169, 157, 157, 152, 157
read: 118
modified: 338
Comment: sound data

W%(col 0-10) = 6, 4, 2, 6, 4, 2, 4, 2, 4, 2, 8
read: 118
modified: 338
Comment: sound data

X%(col 0-10) = 219, 231, 226, 231, 237, 231, 226, 231, 226, 219, 207
read: 120
modified: 338
Comment: sound data

Y%(col 0-10) = 0, 219, 0, 0, 226, 0, 0, 226, 0, 0, 226
read: 120
modified: 338
Comment: sound data

Z%(col 0-10) = 0, 226, 0, 0, 231, 0, 0, 219, 0, 0, 219
read: 120
modified: 338
Comment: sound data

G%(): value uninitialized
read: 161
modified: 96, 156, 164
Comment: piles of buried gold (up to 10)

L%(): value uninitialized
read: 160
modified: 96, 156


string arrays:
--------------
A$(col 0-10) = c"A", c"AN", c"A", c"A", c"A", c"A", c"A", c"A", c"A", c"A", c""
read: 243
modified: 347
Comment: monster "A"s or "AN"s

B$(col 0-10) = c"DIRE WOLF", c"OGRE", c"HOBGOBLIN", c"WEREBEAR", c"GARGOYLE", c"TROLL", c"WYVERN", c"DIMENSION SPIDER", c"SHADOW DRAGON", c"FYRE DRAKE", c""
read: 244
modified: 347
Comment: monster names

C$(col 0-10) = c"A", c"A", c"AN", c"A", c"A", c"A", c"A", c"A", c"AN", c"A", c""
read: 253
modified: 347
Comment: human-like opponents "A"s or "AN"s

D$(col 0-10) = c"ROGUE", c"BARBARIAN", c"ELVIN RANGER", c"DWARVEN GUARD", c"MERCENARY", c"SWORDSMAN", c"MONK", c"DARK WARRIOR", c"ASSASSIN", c"WAR LORD", c""
read: 254
modified: 347
Comment: human-like opponents'names

S$(col 0-10) = c"", c"CRUNCH", c"CLAW", c"GNARL", c"UGH!", c"GROWL!", c"SHRED", c"THUMP", c"", c"", c""
read: 291
modified: 347
Comment: monster battle sounds

T$(col 0-10) = c"", c"CLANG", c"OUCH!", c"SLASH", c"CLINK", c"CHOP", c"THUD", c"SHRIEK!", c"", c"", c""
read: 292
modified: 347
Comment: human-like opponents' battle sounds

X$(col 0-10) = h"WEAK DIRE WOLF", h"A WEREBEAR", h"A WEREBEAR", c"", c"", c"", c"", c"", c"", c"", c""
read: 213, 259
modified: 244
Comment: monster descriptions for level

Y$(col 0-10) = h"A BARBARIAN", c"", c"", c"", c"", c"", c"", c"", c"", c"", c""
read: 215, 263
modified: 254
Comment: human-like opponent descriptions for level
'''

if __name__ == "__main__":
    mem = vic20_sword_of_fargoal_mem_dump()

