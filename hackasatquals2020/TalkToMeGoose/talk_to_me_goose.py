f = open("C:\\Users\\Username\\Downloads\\\LaunchDotCom_Carnac_2\\out1.dat","rb")
d = f.read()
f.close()

b = ''.join(format(x, '08b') for x in d)

def flg_force_decode(b,prepend):
    #b = ''.join(format(x, '08b') for x in d)
    b = '0'*prepend + b
    n = 7
    out = ''.join([chr(int("0"+b[i:i+n],base=2)) for i in range(0, len(b), n)])
    return out



#for x in range(7):
#   print(decode(d,x))
#   print()


def get(b, index, length):
    return b[index:index+length]

def getI(b, index, length):
    return int(b[index:index+length], base=2)

ecs_num = format(101, "016b")
flag_num = format(102, "016b")
eps_num = format(103, "016b")

payload_num = format(105, "016b")

SSC = 0



def payload_decode(d,start=0):
    index = b.find(payload_num,start)
    print("Payload\n\n")
    return index+1


def ecd_decode(d,start=0):
    index = b.find(payload_num,start)
    print("ECS packet\n\n")
    return index+1
flag_raw = ""

def flag_decode(b,start=0):
    global flag_raw
    flag_raw = b
    index = b.find(flag_num,start)
    print("Flag!!!")
    d=get(b, index+56, 840)
    n = 7
    out = ''.join([chr(int("0"+d[i:i+n],base=2)) for i in range(0, len(d), n)])

    print(out)
    print("\n\n\n")

    return "done!"

def eps_decode(b, start=0): #always starts with 0000000001100111
    global SSC
    index = b.find(eps_num,start)
    SSC = getI(b, index+18, 14)
    batt_temp = getI(b, index+48, 16)
    batt_volt = getI(b, index+64, 16)
    low_pwr_thresh = getI(b, index+80, 16)
    low_pwr_mode = getI(b, index+96, 1)
    batt_htr = getI(b, index+97, 1)
    payload_pwr = getI(b, index+98, 1)
    flag_pwr = getI(b, index+99, 1)
    adcs_pwr = getI(b, index+100, 1)
    radio1_pwr = getI(b, index+101, 1)
    radio2_pwr = getI(b, index+102, 1)

    payload_en = getI(b, index+104, 1)
    flag_en = getI(b, index+105, 1)
    adcs_en = getI(b, index+106, 1)
    radio1_en = getI(b, index+107, 1)
    radio2_en = getI(b, index+108, 1)

    bad_cmd_cnt = getI(b, index+112, 32)

    print("EPS:")
    print("CCSDS_SSC:", SSC)
    print("batt_temp", batt_temp)
    print("batt_volt", batt_volt)
    print("low_pwr_thresh", low_pwr_thresh)
    print("low_pwr_mode", low_pwr_mode)
    print("batt_htr", batt_htr)
    print("payload_pwr", payload_pwr)
    print("flag_pwr", flag_pwr)
    print("adcs_pwr", adcs_pwr)
    print("radio1_pwr", radio1_pwr)
    print("radio2_pwr", radio2_pwr)
    print("payload_en", payload_en)
    print("flag_en", flag_en)
    print("adcs_en", adcs_en)
    print("radio1_en", radio1_en)
    print("radio2_en", radio2_en)
    print("bad_cmd_cnt", bad_cmd_cnt)
    print("\n")
    return index+144

def decode(d, start=0):
    flag_index = d.find(flag_num, start)
    eps_index = d.find(eps_num, start)
    payload_index = d.find(payload_num, start)
    if (flag_index >= 0 and (eps_index==-1 or eps_index>flag_index) and (payload_index==-1 or payload_index>flag_index)):
        return flag_decode(d,start)
    elif (eps_index >= 0 and (flag_index==-1 or flag_index>eps_index) and (payload_index==-1 or payload_index>eps_index)):
        return eps_decode(d,start)
    elif (payload_index >= 0 and (flag_index==-1 or flag_index>payload_index) and (eps_index==-1 or eps_index>payload_index)):
        return payload_decode(d,start)
    else:
        return "err"

ENABLED = format(1, "08b")
DISABLED = format(0, "08b")

def makeHeader(apid, plength):
    ssc_s = format(SSC, "014b")
    return "00010" + format(apid, "011b") + "11" + ssc_s + format(plength, "016b")

def makeLowPowerThresh(val):
    header = makeHeader(103, 3)
    cmd = format(0, "08b")
    param = format(12, "08b")
    thresh = format(val,"016b")

    return s(header+cmd+param+thresh)

def makeDisableRadio(): #radio2
    header = makeHeader(103,2)
    cmd = format(0, "08b")
    param = format(5, "08b")
    powerstate = DISABLED
    return s(header+cmd+param+powerstate)

def makeDisablePayload():
    header = makeHeader(103,2)
    cmd = format(0, "08b")
    param = format(0, "08b")
    powerstate = DISABLED
    return s(header+cmd+param+powerstate)

def makeDisableADCS():
    header = makeHeader(103,2)
    cmd = format(0, "08b")
    param = format(4, "08b")
    powerstate = DISABLED
    return s(header+cmd+param+powerstate)

def makeFlagEnable():
    header = makeHeader(103, 2)
    cmd = format(0, "08b")
    param = format(2, "08b")
    powerstate = ENABLED
    return s(header+cmd+param+powerstate)

def s(b):
    #n=8
    #return ''.join([chr(int("0"+b[i:i+n],base=2)) for i in range(0, len(b), n)])
    return int(b, 2).to_bytes(len(b) // 8, byteorder='big')

def decodeLoopFromData(d):
    b = ''.join(format(x, '08b') for x in d)
    a=0
    try:
        while True:
            b=decode(b,a)
    except Exception as e:
        if (str(e) == "'int' object has no attribute 'find'"):
            return
        else:
            print(e)
        return

def rxPacket():
    sleep(1)
    data = s2.recv(1024)
    decodeLoopFromData(data)

import socket
from time import sleep
ticket = "ticket{delta71034romeo:REDACTED FOR WRITEUP}\n"
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(("goose.satellitesabove.me", 5033))
data = s1.recv(1024)
s1.sendall(ticket)
data2 = str(s1.recv(1024))

sleep(4)

ip = data2[(data2.find("at ")+3) : (data2.find(":"))]
port = data2[(data2.find(":")+1) : -3]
print(ip, port)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((ip, int(port)))

data = s2.recv(1024) #get first packet, so wait for connection
decodeLoopFromData(data)

print("*** Disabling radio ***\n")
s2.sendall(makeDisableRadio())

print("*** Disable Payload ***\n")
s2.sendall(makeDisablePayload())

print("*** makeDisableADCS ***\n")
s2.sendall(makeDisableADCS())

print("*** makeFlagEnable ***\n")
s2.sendall(makeFlagEnable())

rxPacket()

#for i in range(900,1000,1): #>900 is valid apparently. I don't understand this conversion.
print("*** LowPowerThresh=",1000," ***\n")
s2.sendall(makeLowPowerThresh(1000))

rxPacket()
rxPacket()



try:
    while True:
        rxPacket()
finally:
    s2.close()
    s1.close()
    print("closed ports")
    print("flag (for real:)")
    print(flg_force_decode(flag_raw[6+7*6:],0)) #meh it works