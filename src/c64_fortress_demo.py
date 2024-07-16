import basicVarAnalysis

# Process variables in a C64 memory dump of Fortress (SSI, 1984)
# https://www.c64-wiki.com/wiki/Fortress_(SSI)

def c64_fortress_mem_dump():    
    mem = basicVarAnalysis.MemoryDump('C64')
    mem.find_vars("test_data/c64_fortress.bin")
    mem.add_formatting("AE", comment = "1 == game end")
    mem.add_formatting("FR", comment = "joystick fire button")
    mem.add_formatting("JV", comment = "joystick direction")
    mem.add_formatting("P",  comment = "player is either 1 or -1, inits to 0")
    mem.add_formatting("PN", comment = "player is either 1 or 2")
    mem.add_formatting("X",  comment = "cursor x position")
    mem.add_formatting("Y",  comment = "cursor Y position")
    mem.add_formatting("D8", comment = "TODO: Used in creating i8(),j8(),a1(),a2(),d1(),d2()")
    mem.add_formatting("V1", comment = "p=1's current territory count")
    mem.add_formatting("V2", comment = "p=-1's current territory count")
    mem.add_formatting("W$", comment = 'seige warning, "0" off, "1" on')
    mem.add_formatting("S",  comment = "SID base, also used in SEQ file processing")
    mem.add_formatting("V",  comment = "sprite pos base or char rom when banked in")
    mem.add_formatting("TG", comment = "game delay loops")
    mem.add_formatting("t1", comment = "number of game rounds (default 21)")

    mem.add_formatting("A0()", comment = "TODO: weights from SEQ file, guess: state of adjacent 5-square crosses")    
    mem.add_formatting("A1()", comment = "TODO: player 1 weights")
    mem.add_formatting("A2()", comment = "TODO: player 2 weights")
    mem.add_formatting("HA()", comment = "History adjacencies, gathered over game, sign indicates play with more influence")
    mem.add_formatting("D0()", comment = "TODO: weights from SEQ file, guess: state of cross of considered square")
    mem.add_formatting("D1()", comment = "TODO: player 1 weights")
    mem.add_formatting("D2()", comment = "TODO: player 2 weights")
    mem.add_formatting("HD()", comment = "History direct, gathered over game")
    mem.add_formatting("P0()", comment = "TODO: weights from SEQ file, guess: state of square's absolute position on board")
    mem.add_formatting("P1()", comment = "TODO: player 1 weights")
    mem.add_formatting("P2()", comment = "TODO: player 2 weights")
    mem.add_formatting("HP()", comment = "History position, gathered over game.  Harmless bug: DIMed at 14 instead of 5.")
    mem.add_formatting("I8()", width = 3, comment = "p1 strength eval. init 7, init border 10")
    mem.add_formatting("J8()", width = 3, comment = "p2 strength eval. init 7, init border 10")
    mem.add_formatting("C8()", width = 2, comment = "unweighted castle influences, if castle on 0 then drawbridge closed")
    mem.add_formatting("S8()", width = 2, comment = "castles (only) with strength (p1 1 to 3, p2 -1 to -3)")
    mem.add_formatting("L8()", width = 2, comment = "board's inherent static positional strengths")
    mem.add_formatting("SR()", comment = "music data triples (FreqHi, FreqLo, FreqCtrl)")
    mem.add_formatting("SX()", comment = "an X pos stack of size 20 (for recursion)")
    mem.add_formatting("SY()", comment = "a Y pos stack of size 20 (for recursion)")

    mem.print_basic_ranges()
    mem.print_variables()
    return mem

'''
parsing vars from memory dump...
- 40960 bytes (assuming $0000 to $9FFF)
- BASIC line number: 130
- BASIC line number on last exit: 0
- PEEK(774)==238, so LISTing may be disabled (26 to restore)
- PEEK(808)==234, so RUN/STOP key and/or LISTing may be disabled (237 to restore)

BASIC ranges:
-------------
TXTTAB $1001/4097: start of BASIC (default $0801/2049), 30486-byte extent
VARTAB $8716/34582: start of variables, 595-byte extent
ARYTAB $8969/35177: start of arrays, 5047-byte extent
STREND $9D20/40224: end of arrays (exclusive)
FRETOP $9F0F/40719: end (bottom) of string heap, 241-byte extent
MEMSIZ $A000/40960: start (top) of string heap + 1

floats:
-------
A: 0
read: 19030, 19035, 20030, 36240, 36250, 36260, 36300, 36320, 45290, 45372
modified: 19030, 19035, 20030, 23050, 23063, 25050, 25094, 26068, 26077, 31044, 31066, 32040, 32050, 33044, 33052, 36165, 36240, 36250, 36260, 36300, 36320, 45290, 45372

AA: 64
read: 40, 8222, 8224, 8225, 8228, 8301, 8303, 44526
modified: 30, 8220, 44526

AD: 0
read: 14002, 21226, 44507
modified: 43060

AE: 0
read: 18242
modified: 40, 8222, 18040
Comment: 1 == game end

BA: 2048
read: 45253, 45290, 45372
modified: 45230

BB: value uninitialized
read: 8301, 8303
modified: 8221

BF: value uninitialized
read: 23051, 23064, 23105, 31025, 33025, 59075
modified: 59060

BL: 0
modified: 60030

BT: value uninitialized
read: 36320, 36360
modified: 36290, 36320

C: 49
read: 3050, 3060, 3100, 3130, 3160, 3300, 18472, 21235, 21450, 21570, 21610, 35115, 36380, 36385, 36390, 40070, 40080
modified: 3042, 4035, 21235, 21445, 21450, 21545

C0: 0
read: 740, 780, 790, 820, 830, 950, 980, 1000, 1010, 10040, 10060, 14003, 14004
modified: 740, 950

C1: 15
read: 21235
modified: 3030, 21235

C9: value uninitialized
read: 16060, 16062, 16130, 16180
modified: 16060, 16062

CP: value uninitialized
read: 26046, 37265
modified: 37060, 37070, 41130

CR: value uninitialized
read: 62010, 62015

D7: 1
read: 240, 250, 260, 270, 280, 290, 300, 650
modified: 230, 240, 250, 260, 270, 280, 290, 625, 630, 640, 43050

D8: 1
read: 160, 500, 505, 510, 515, 650
modified: 160, 400, 410, 650, 43060
Comment: TODO: Used in creating i8(),j8(),a1(),a2(),d1(),d2()

DR: 650
read: 14008, 21240, 44531
modified: 14006, 21234, 44525

E: 27
read: 43124, 43126, 45230, 45253, 45290, 45372
modified: 43122, 43126

E3: value uninitialized
read: 16130, 16132, 16180, 16182
modified: 16130, 16180

EC: 3
read: 59083, 59084, 59086, 59088, 60042, 60400, 60401, 60402
modified: 5033, 6045, 23051, 23056, 23064, 23105, 25036, 25090, 26032, 26062, 31025, 32033, 33025, 35076

ER: 0
read: 5035, 6046, 6047, 23056, 23061, 23062, 26032, 26033, 26062, 26063, 31033, 31034, 31035, 32033, 32034, 33041, 33042, 36100, 60040, 60042, 60110, 60120, 60121, 60130, 60140, 60150, 60160, 60170, 60180, 60185, 60500
modified: 59005, 59077, 60020, 60030, 63010

FR: value uninitialized
read: 8210
modified: 8197
Comment: joystick fire button

G: 1
read: 18040, 18242, 18430, 18440, 18837, 31120, 31125, 31130, 36240, 36250, 36260, 36265, 36290, 41030, 41055, 41070, 41164, 41180
modified: 18030, 18040, 18242, 36240, 36250, 36260

G0: value uninitialized
read: 26076, 31034, 31042, 36140
modified: 32037, 41164, 41180, 41190

G3: value uninitialized
read: 26076, 31042, 31044, 36202
modified: 26066, 31034, 31041, 31042, 36202

G6: value uninitialized
read: 8174, 8180
modified: 8170, 8171, 8310, 8315, 8320, 8325, 8330, 8335

GG: value uninitialized
modified: 36074, 37124, 38076

GI: value uninitialized
read: 14045, 14050, 14055, 31145
modified: 14045, 14050, 14055, 18472, 31068, 33057

GS: value uninitialized
read: 54010, 54020
modified: 54010

HF: 0
read: 14008, 21240, 44527, 44529
modified: 14006, 21234, 44525

I: 3
read: 90, 100, 110, 120, 130, 140, 150, 160, 230, 240, 250, 260, 270, 294, 296, 3070, 3120, 3270, 3280, 3300, 3320, 3330, 3340, 7030, 7035, 7040, 7045, 8040, 9030, 9033, 9090, 12050, 14006, 14015, 14018, 16060, 16062, 16130, 16132, 16180, 16182, 17990, 17991, 18060, 18062, 18070, 18072, 18330, 18840, 21234, 21252, 26040, 26042, 26044, 26078, 28050, 28052, 28070, 28072, 30030, 30035, 33057, 36180, 36190, 36202, 36210, 36240, 36250, 36260, 36280, 36300, 36320, 40055, 40735, 40740, 41080, 41082, 42560, 42570, 43310, 44525, 44536, 45253, 45290, 45372
modified: 80, 3030, 3280, 3300, 3330, 6050, 6060, 6070, 7030, 7035, 7040, 7045, 8040, 8175, 9010, 12050, 14002, 14018, 16060, 16062, 16130, 16132, 16180, 16182, 17990, 17991, 18060, 18062, 18070, 18072, 18330, 18840, 21226, 21252, 23063, 23080, 23120, 25094, 26040, 26042, 26044, 26068, 26077, 28050, 28052, 28070, 28072, 30030, 30035, 31046, 31105, 31107, 32060, 33045, 33055, 34240, 35082, 36180, 36190, 36202, 36210, 36240, 36250, 36260, 36280, 36300, 36320, 39077, 40055, 40082, 40088, 40735, 40900, 41070, 42502, 42552, 42560, 42570, 43050, 43128, 43310, 44507, 44536, 45250, 45280, 45370, 53020

I1: 7
read: 105, 110, 125, 130, 240, 9030, 9036, 9040, 9093, 9096
modified: 100, 120, 9030, 9033, 9090, 43050

I2: 8
read: 105, 110, 125, 130, 250, 9036, 9040, 9093, 9096
modified: 100, 120, 9033, 9090, 43050

I3: 7
read: 105, 110, 125, 130, 260, 9036, 9040, 9093, 9096
modified: 100, 120, 9033, 9090, 43050

I4: 7
read: 105, 110, 125, 130, 270, 9036, 9080, 9093, 9130
modified: 100, 120, 9033, 9090, 43050

ID: 7
read: 110, 130, 9040, 9096
modified: 100, 120, 300, 9033, 9090, 43050

II: 0
read: 8040, 19030
modified: 8040, 19030, 20030, 43060

J: 5
read: 90, 100, 110, 120, 130, 140, 150, 160, 230, 240, 250, 260, 270, 294, 296, 3340, 8040, 9030, 9033, 9090, 17025, 17070, 18060, 18070, 18074, 31105, 31120, 32060, 33055, 35082, 35090, 36330, 43310 
modified: 80, 3340, 8040, 9010, 17025, 17050, 18060, 18070, 18074, 26078, 31090, 31100, 31120, 31130, 31145, 32050, 33052, 35079, 35082, 36290, 43050, 43310, 44527

JJ: 0
read: 20030
modified: 20030, 43060

JV: value uninitialized
read: 8197, 8200, 8306, 8308, 8310, 8315, 8320, 8325, 8330, 8335
modified: 8190, 8192, 8197, 8301, 8303
Comment: joystick direction

K0: 1
read: 300, 625, 630, 640, 740, 780, 800, 840, 850, 950, 1060, 1070, 10040, 10060, 11032
modified: 294, 296, 740, 950

L: 12
read: 3070, 20030, 31105, 31107, 44505
modified: 23063, 25094, 26077, 31066, 31105, 31107, 33044, 36165, 37212, 39040, 40710, 44314, 44505, 61713

LC: value uninitialized
read: 14003, 14004
modified: 14001

LF: 0
read: 14008, 21240, 44529
modified: 14006, 21234, 44525

LO: 1533
read: 10030, 10100, 10101, 10110, 10111, 10200, 10201, 10210, 10211, 11035, 11070, 12050, 13025, 13110, 13112, 13114, 13200, 13205, 13300, 13610, 13612, 13614, 13700, 13705, 13800, 14001, 14045, 14050, 14055, 39077
modified: 10030, 11030, 11035, 11070, 12030, 12050, 13025, 13110, 13112, 13200, 13205, 13300, 13610, 13612, 13700, 13705, 13800, 14001, 14045, 14050, 39077

LR: 1331
modified: 13025

LT: value uninitialized
read: 36160, 36162
modified: 36155

M: 2
read: 60, 160, 18210, 18220, 18230, 18240, 18270, 18280
modified: 18200

M1: 1
read: 18200, 18330
modified: 18030, 18330

M2: 2
read: 60, 160, 18200, 18330
modified: 18030, 18330

MI: 1
read: 40082, 40084, 40086, 40090, 40900, 40902, 40904
modified: 40080

NT: value uninitialized
read: 26067, 26068, 26076, 26077, 31041, 31043, 31044, 31046, 31067, 31068, 32040, 32050, 33045, 33052, 36150, 36155, 36160, 36162
modified: 26066, 31034, 31041, 31043, 32037, 33044, 36100

O: value uninitialized
read: 42560

P: -1
read: 90, 95, 300, 400, 410, 500, 505, 510, 515, 1430, 5030, 5060, 6030, 6080, 8040, 8190, 8192, 8910, 9030, 9040, 9080, 9096, 9130, 13032, 23030, 23130, 25030, 25110, 26030, 26080, 31030, 31160, 32030, 32070, 33030, 33060, 62010, 62100
modified: 5030, 5060, 6030, 6080, 18210, 18500, 23030, 23130, 25030, 25110, 26030, 26080, 31030, 31160, 32030, 32070, 33030, 33060, 43050, 43650, 62010, 62100
Comment: player is either 1 or -1, inits to 0

PN: 3
read: 7030, 7035, 7040, 7045, 28050, 28052, 28070, 28072, 31090, 31100, 34050, 34090, 34220, 34240, 34244, 34270, 41160, 41164, 41220, 41300
modified: 18044, 18045, 34030, 41150, 43180
Comment: player is either 1 or 2

PO: 1
read: 8160
modified: 8045, 8300, 8610, 43060

Q: 1
read: 740, 940, 950, 42560, 42570
modified: 1250, 1430, 42560, 42570

R: 22
read: 5038, 5040, 5050, 23057, 23058, 23062, 23063, 25040, 25052, 25092, 25094, 35070, 35082, 35090 
modified: 5038, 23057, 23062, 25040, 25092, 35080

RS: 0
read: 62010
modified: 5030, 5060, 23030, 23074, 23120, 23130, 25030, 25110

S: 54272
read: 5050, 8336, 8337, 13033, 13034, 13037, 13038, 13500, 13502, 13550, 13552, 14002, 14008, 21226, 21240, 21245, 21451, 34120, 36070, 37120, 37250, 38072, 41240, 44505, 44507, 44529, 44532, 44540   
modified: 5030, 5040, 5050, 8150, 13025, 14002, 21210, 23058, 25030, 25052, 43122, 43126, 44504     
Comment: SID base, also used in SEQ file processing

S0: 0
read: 740, 780, 940, 980, 1100, 8910, 10040, 10060
modified: 740, 940, 8910

S7: 0
read: 90
modified: 90, 43050

SP: 0
read: 1330, 1390, 1440
modified: 1330, 1390, 1440

SR: 240
read: 14002, 21226, 44507
modified: 43060

T: 2
read: 60, 160, 3080, 18180, 18300, 21550, 36160, 36162, 36165, 36385, 36390
modified: 18170, 21240, 21245, 34132, 36155, 36160, 36162, 36385, 36390, 37212, 37285, 39040, 39060, 40710, 41162, 41180, 41200, 43122, 43126, 44314, 44531, 44534, 61713, 63010

T1: 21
read: 60, 160, 18170, 18837, 31112, 40044, 40740, 41044
modified: 40740, 43580
Comment: number of game rounds (default 21)

T9: 5
read: 150
modified: 70, 150, 43050

TE: 0
read: 18420, 31112, 41054
modified: 18030, 18420

TG: 63
modified: 8337, 13034, 13037, 13500, 13550, 14008, 14016, 54020
Comment: game delay loops

TR: 0
modified: 60030

V: value uninitialized
read: 8150, 8160, 8174, 8180, 8338, 8610, 8995
modified: 8150
Comment: sprite pos base or char rom when banked in

V1: 8
read: 820, 840, 1000, 1060, 1070, 1110, 1464, 16040, 18400, 18410, 18420, 18430
modified: 820, 840, 1000, 1060, 1070, 1110, 18040
Comment: p=1's current territory count

V2: 4
read: 830, 850, 1010, 1060, 1070, 1120, 1470, 16040, 18400, 18410, 18420, 18430
modified: 830, 850, 1010, 1060, 1070, 1120, 18040
Comment: p=-1's current territory count

V3: -4.669299999
read: 140, 150, 8050, 18243
modified: 70, 140, 8040, 43050

V7: -5.308800001
read: 140, 150
modified: 110, 130, 43050

V9: value uninitialized
read: 16040, 16120, 16130, 16170, 16180
modified: 16040, 16120, 16170

W1: 0
read: 18400, 31090, 31100, 41050
modified: 18030, 18400

W2: 0
read: 18410, 31090, 31100, 41053
modified: 18030, 18410

WF: 32
read: 13034, 13038, 13502, 13552, 14008, 21245, 44532, 44540
modified: 43060

WS: 33
read: 13034, 13037, 13500, 13550, 14008, 21240, 44529
modified: 43060

WT: value uninitialized
read: 36300, 36350, 36355
modified: 36290, 36300

X: 2
read: 1330, 1340, 1360, 1390, 1430, 8160, 8170, 8171, 8300, 8310, 8315, 8320, 8325, 8330, 8335, 8910, 9010, 31112
modified: 140, 150, 1250, 1390, 8310, 8315, 8320, 8325, 8330, 8335, 18040, 31090, 31100, 43050      
Comment: cursor x position

X0: 5
read: 940, 950, 960, 1140, 1160, 1230, 1250, 1440
modified: 1340, 1360, 1390, 1430, 8300

X2: 5
read: 650, 730, 740, 10030, 11030, 12030, 13025, 14001
modified: 960, 1140, 1160

X9: 803
modified: 18440, 36400, 40904, 41330, 43650

Y: 5
read: 1330, 1340, 1360, 1390, 1430, 8160, 8300, 8306, 8308, 8315, 8320, 8330, 8335, 8910, 9010, 31112
modified: 140, 150, 1250, 1390, 8306, 8308, 8315, 8320, 8330, 8335, 18040, 31090, 31100, 43050      
Comment: cursor Y position

Y0: 3
read: 940, 950, 960, 1140, 1160, 1230, 1250, 1440
modified: 1340, 1360, 1390, 1430, 8300

Y2: 4
read: 650, 730, 740, 10030, 11030, 12030, 13025, 14001
modified: 960, 1140, 1160

Z0: 0
read: 755, 940, 1030, 1110, 1120, 10040, 10060, 10090, 10100, 10101, 10110, 10111, 10190, 10200, 10201, 10210, 10211, 13035, 13510
modified: 740, 940


strings:
--------
A$: h"COUNT VAUBAN(C)"
read: 5038, 5040, 15025, 31107, 31112, 33055, 35080, 36190, 36195, 36210, 36220, 36230, 36240, 36245, 36250, 36255, 36260, 36265, 36270, 36282, 36285, 36300, 36310, 36320, 36330, 36355, 36360, 36370, 39040, 39077, 41050, 41052, 41053, 41054, 41055, 41080, 41081, 41082, 41090, 41110, 41112, 41114, 41120, 41130
modified: 5038, 5040, 18190, 18220, 18270, 18290, 18400, 18410, 18420, 18442, 18470, 23080, 31034, 31041, 31107, 33044, 34050, 35080, 36040, 36190, 36210, 36240, 36250, 36260, 36265, 36280, 36300, 36320, 36350, 36355, 36360, 37060, 37070, 38040, 41050, 41053, 41054, 41055, 41080, 41082, 41110, 41112, 41120, 43060

B$: value uninitialized
read: 59060
modified: 59050

BS$: h"¶"
read: 3280
modified: 43100

C$: h"1"
read: 3040, 3042, 4030, 4035, 21440, 21445, 21540, 21545, 21640, 31112, 34155, 34160, 37295, 39065, 41164, 41180, 41200, 59100, 63010
modified: 3040, 4030, 21440, 21540, 31090, 31100, 59100

EN$: h"OK"
read: 60110, 60130, 60500
modified: 43122, 43126, 60030

F$: h"COUNT VAUBAN(C)"
read: 5040, 6030, 23059, 23066, 23100, 23110, 25050, 25052, 26030, 26060, 31030, 31042, 32030, 33030, 34090, 34157, 34220, 36140, 36163, 38100, 38110, 61715, 61716, 62025, 62030
modified: 34090, 36070, 37060, 37080, 37215, 38070, 41220, 43170, 61713, 61716

F1$: h"COUNT VAUBAN(C)W"
read: 6040, 23068, 23112, 26032, 26062, 26072, 31032, 31062, 32032, 33040, 38102, 38112
modified: 6030, 23066, 23110, 26030, 26060, 31030, 32030, 33030, 38100, 38110

FL$: c"**********************************"
read: 23080, 26078, 31145, 33044, 33057, 53020
modified: 43580

G$: value uninitialized
read: 36145, 36164
modified: 36140

G0$: value uninitialized
read: 32037, 32040
modified: 32037

G3$: value uninitialized
read: 26066, 31041
modified: 26066, 31040

H$: value uninitialized
read: 41195, 41250
modified: 41164

H1$: c"FORTRESS"
read: 40025, 44090
modified: 43112

H2$: c"A GAME OF STRATEGIC DEPLOYMENT"
read: 40026, 44090
modified: 43112

H3$: c"AND FORTIFICATION"
read: 40027, 44096
modified: 43116

H4$: c"COPYRIGHT (C) 1984 ICONOGRAPHICS, INC."
read: 40028, 44102
modified: 43116

J$: value uninitialized
read: 59040, 59060
modified: 59030, 59040, 59050

L$: value uninitialized
read: 31112, 41180, 41190, 41195, 41260
modified: 41164, 41180

N$: value uninitialized
read: 59060
modified: 59020

NT$: value uninitialized
read: 26066, 31041, 32037, 32040
modified: 26066, 31040, 32037

OK$: value uninitialized
read: 43130
modified: 43124, 43126

S$: h"COUNT VAUBAN(C)"
read: 3340, 19030, 20030, 23057, 23063, 25040, 25052, 25094, 26077, 31066, 31068, 31105, 31112, 33044, 33045, 33055, 34050, 34090, 35082, 36040, 36070, 36170, 36180, 36190, 36202, 36210, 36240, 36250, 36260, 36280, 36300, 36320, 37060, 37075, 37080, 37212, 37215, 38040, 38070, 39040, 39065, 39077, 40720, 40735, 44314, 44320, 61713
modified: 3320, 3340, 20030, 23057, 23058, 23059, 25040, 25052, 26068, 31043, 31044, 31046, 31105, 32040, 32060, 35082, 39065

T$: h"  2"
read: 18180, 18190, 18290, 34090, 37140, 37215, 37320, 38110, 39065, 61716
modified: 18180, 39065

V1$: h"  8"
read: 1464, 1466
modified: 1464, 18040

V2$: h"  4"
read: 1470, 1474
modified: 1470, 18040

W$: c"1"
read: 755, 1090, 14003, 14004, 31112, 40048, 40049, 40810, 40815
modified: 40810, 40815, 43580
Comment: seige warning, "0" off, "1" on


float arrays:
-------------
A0(col 0-15) = -2.069399999, -1.5024, 17.370999999, 0, 0, -1.8032, -1.4412, -1.3477, -1.8689, -1.7614, -1.531699999, 0, -.6519, -1.752400001, -1.6412, 0
read: 7030, 7040, 26040, 43072
modified: 6050, 28050, 28070, 30030
Comment: TODO: weights from SEQ file, guess: state of adjacent 5-square crosses

A1(col 0-14) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 110, 400, 500, 16130, 28050
modified: 500, 7030, 16130, 43070
Comment: TODO: player 1 weights

A2(col 0-14) = -2.069399999, -1.5024, 17.370999999, 0, 0, -1.8032, -1.4412, -1.3477, -1.8689, -1.7614, -1.531699999, 0, -.6519, -1.752400001, -1.6412
read: 130, 410, 510, 16180, 28070, 43070
modified: 510, 7040, 16180
Comment: TODO: player 2 weights

BS(col 0-15) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 18430, 31120, 41082, 41120, 43074
modified: 18030, 18430

C8(col 0-7, row 0-7) =
    0,  0,  0,  0,  0,  0,  0,  0
    0,  1,  0,  0,  0,  0,  0,  0
    0,  1,  1, -1,  0,  1,  0,  0
    0,  1, -1, -1,  0,  1,  1,  0
    0,  0,  0, -1,  0,  1,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
read: 230, 740, 950, 1230, 43070
modified: 740, 950, 18060
Comment: unweighted castle influences, if castle on 0 then drawbridge closed

D0(col 0-15) = 0, 0, 0, 0, 0, -1.0456, -.2623, .4473, .105, .0102, 0, 0, 1.0127, -.2593, -.1278, 0  
read: 7030, 7040, 26042, 43072
modified: 6060, 28050, 28070, 30030
Comment: TODO: weights from SEQ file, guess: state of cross of considered square

D1(col 0-14) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 110, 505, 16130, 28050, 43070
modified: 505, 7030, 16130
Comment: TODO: player 1 weights

D2(col 0-14) = 0, 0, 0, 0, 0, -1.0456, -.2623, .4473, .105, .0102, 0, 0, 1.0127, -.2593, -.1278     
read: 130, 515, 16180, 28070, 43070
modified: 515, 7040, 16180
Comment: TODO: player 2 weights

FA(col 0-2) = 0, 0, 0
read: 43072

FY(col 0-6) = 0, 0, 4, 7, 10, 14, 17
modified: 42570

GX(col 0-6) = 0, 46, 94, 142, 190, 238, 30
read: 8160
modified: 42552

GY(col 0-6) = 0, 58, 82, 106, 130, 154, 178
read: 8160, 42552
modified: 42552

HA(col 0-14) = 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0
read: 9040, 9080, 9096, 9130, 16060, 16130, 16180, 43072
modified: 9040, 9080, 9096, 9130, 18062
Comment: History adjacencies, gathered over game, sign indicates play with more influence

HD(col 0-14) = 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
read: 9040, 9096, 16060, 16130, 16180, 43072
modified: 9040, 9096, 18062
Comment: History direct, gathered over game

HP(col 0-14) = -1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 9030, 16062, 16132, 16182, 43072
modified: 9030, 18062
Comment: History position, gathered over game.  Harmless bug: DIMed at 14 instead of 5.

I8(col 0-7, row 0-7) =
    10,  10,  10,  10,  10,  10,  10,  10
    10,   8,   7,   7,   7,   7,   7,  10
    10,  13,   8,   6,   7,   8,   7,  10
    10,   8,   6,   1,   7,  13,   8,  10
    10,   7,   7,   6,   7,   8,   7,  10
    10,   7,   7,   7,   7,   7,   7,  10
    10,   7,   7,   7,   7,   7,   7,  10
    10,  10,  10,  10,  10,  10,  10,  10
read: 100, 9033, 43070
modified: 650, 18070, 18072, 18074
Comment: p1 strength eval. init 7, init border 10

J8(col 0-7, row 0-7) =
    10,  10,  10,  10,  10,  10,  10,  10
    10,   6,   7,   7,   7,   7,   7,  10
    10,   1,   6,   8,   7,   6,   7,  10
    10,   6,   8,  13,   7,   1,   6,  10
    10,   7,   7,   8,   7,   6,   7,  10
    10,   7,   7,   7,   7,   7,   7,  10
    10,   7,   7,   7,   7,   7,   7,  10
    10,  10,  10,  10,  10,  10,  10,  10
read: 120, 9090
modified: 650, 18070, 18072, 18074, 43072
Comment: p2 strength eval. init 7, init border 10

L8(col 0-6, row 0-6) =
    0,  0,  0,  0,  0,  0,  0
    0,  5,  4,  3,  3,  4,  5
    0,  4,  2,  1,  1,  2,  4
    0,  3,  1,  0,  0,  1,  3
    0,  3,  1,  0,  0,  1,  3
    0,  4,  2,  1,  1,  2,  4
    0,  5,  4,  3,  3,  4,  5
read: 110, 130, 9030, 43072
modified: 43310
Comment: board's inherent static positional strengths

MD(): value uninitialized
read: 26068, 26077, 31046, 31068, 36165

NR(col 0-2) = 0, 10, 11
read: 34240, 43074
modified: 43077

P0(col 0-6) = .3817, .1578, .2742, .0406, -.1871, -.6673, 0
read: 7035, 7045, 26044, 43072
modified: 6070, 28052, 28072, 30035
Comment: TODO: weights from SEQ file, guess: state of square's absolute position on board

P1(col 0-5) = 0, 0, 0, 0, 0, 0
read: 110, 16132, 28052, 43070
modified: 7035, 16132
Comment: TODO: player 1 weights

P2(col 0-5) = .3817, .1578, .2742, .0406, -.1871, -.6673
read: 130, 16182, 28072, 43070
modified: 7045, 16182
Comment: TODO: player 2 weights

S8(col 0-7, row 0-7) =
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  1,  0,  0,  0,  0,  0,  0
    0,  0,  0, -1,  0,  1,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
    0,  0,  0,  0,  0,  0,  0,  0
read: 90, 240, 250, 260, 270, 294, 296, 650, 740, 940, 1230, 1250, 8040, 8910, 43070
modified: 940, 18060
Comment: castles (only) with strength (p1 1 to 3, p2 -1 to -3)

SA(col 0-2) = 0, 0, 0
read: 43072

SR(col 0-378) = 0, 9, 104, 437, 8, 225, 62, 7, 233, 437, 8, 225, 62, 9, 104, 250, 10, 143, 250, 11, 218, 250, 9, 104, 250, 12, 143, 250, 11, 218, 250, 10, 143, 250, 9, 104, 250, 8, 225, 250, 7, 233, 250, 8, 225, 250, 7, 12, 250, 9, 104, 437, 8, 225, 62, 7, 233, 437, 8, 225, 62, 9, 104, 250, 10, 143, 250, 11, 218, 250, 15, 210, 250, 14, 24, 62, 11, 218, 437, 10, 143, 437, 11, 218, 62, 9, 104, 750, 0, 0, 650, 9, 104, 375, 8, 225, 62, 7, 233, 437, 8, 225, 62, 9, 104, 250, 10, 143, 250, 11, 218, 250, 9, 104, 250, 12, 143, 250, 11, 218, 250, 10, 143, 250, 9, 104, 250, 8, 225, 250, 7, 233, 250, 8, 225, 250, 7, 12, 250, 9, 104, 437, 8, 225, 62, 7, 233, 437, 8, 225, 62, 9, 104, 250, 10, 143, 250, 11, 218, 250, 15, 210, 250, 14, 24, 437, 11, 218, 62, 10, 143, 437, 11, 218, 62, 9, 104, 750, 0, 0, 650, 10, 143, 437, 9, 104, 62, 8, 225, 437, 9, 104, 62, 10, 143, 250, 10, 143, 250, 0, 0, 650, 14, 24, 437, 12, 143, 62, 11, 218, 437, 12, 143, 62, 14, 24, 250, 14, 24, 250, 0, 0, 438, 14, 24, 62, 14, 24, 438, 12, 143, 62, 11, 218, 437, 12, 143, 62, 14, 24, 437, 12, 143, 62, 11, 218, 437, 12, 143, 62, 14, 24, 45, 15, 210, 15, 14, 24, 45, 12, 143, 15, 11, 218, 45, 10, 143, 15, 11, 218, 45, 12, 143, 15, 14, 24, 250, 14, 24, 250, 0, 0, 650, 15, 210, 250, 15, 210, 250, 14, 24, 250, 14, 24, 250, 12, 143, 250, 12, 143, 250, 11, 218, 250, 11, 218, 250, 10, 143, 250, 12, 143, 60, 11, 218, 60, 10, 143, 250, 9, 104, 250, 8, 225, 250, 7, 233, 250, 8, 225, 250, 7, 12, 250, 9, 104, 437, 8, 225, 62, 7, 233, 437, 8, 225, 62, 9, 104, 250, 10, 143, 250, 11, 218, 250, 15, 210, 1250, 14, 24, 62, 11, 218, 437, 10, 143, 437, 11, 218, 62, 9, 104, 750, 0, 0, 260, -1, -1, -1
read: 13034, 13037, 13500, 13550, 14006, 21234, 44525
modified: 42502
Comment: music data triples (FreqHi, FreqLo, FreqCtrl)

SX(col 0-19) = 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 1390
modified: 1330, 1440, 43075
Comment: an X pos stack of size 20 (for recursion)

SY(col 0-19) = 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 1390, 43075
modified: 1330, 1440
Comment: a Y pos stack of size 20 (for recursion)

WS(col 0-15) = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
read: 18430, 31120, 41080, 41110, 41112, 43074
modified: 18030, 18430


integer arrays:
---------------
S%(col 0-20) = 0, 67, 79, 85, 78, 84, 32, 86, 65, 85, 66, 65, 78, 0, 0, 0, 0, 0, 0, 0, 0
read: 3330, 3340, 43074
modified: 3300


string arrays:
--------------
M1$(3) =
   M1$(0) = c""
   M1$(1) = c"WHITE PLAYER: "
   M1$(2) = c"BLACK PLAYER: "
read: 34050, 40040, 40042, 41043, 43074
modified: 43550

MN$(9) =
   MN$(0) = c""
   MN$(1) = c"[1] BEGIN PLAY    "
   MN$(2) = c"[2] CHANGE PLAYERS"
   MN$(3) = c"[3] DISPLAY ROSTER"
   MN$(4) = c"[4] REPORT HISTORY"
   MN$(5) = c"[5] COPY PLAYER"
   MN$(6) = c"[6] REMOVE PLAYER"
   MN$(7) = c"[7] SET GAME LENGTH"
   MN$(8) = c"[8] SET SIEGE WARN"
read: 40055, 40086, 40904, 43074
modified: 43460, 43480, 43500, 43520

NM$(3) =
   NM$(0) = c""
   NM$(1) = h"THE SQUIRE(C)"
   NM$(2) = h"COUNT VAUBAN(C)"
read: 16160, 18043, 18220, 18270, 18400, 18410, 31105, 34244, 40040, 40042, 41043, 41160, 41220, 41290, 43170
modified: 34090, 34220, 43074, 43170, 44320

PT$(3) =
   PT$(0) = c""
   PT$(1) = c"C"
   PT$(2) = c"C"
read: 8600, 16110, 16160, 18042, 18043, 18044, 18230, 18240, 41164, 43074
modified: 34090, 34220, 43170, 44320
'''


if __name__ == "__main__":
    mem = c64_fortress_mem_dump()
