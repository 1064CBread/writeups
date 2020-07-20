# make_raw.py

f_pcap = open("./recv.pcap", "rb")
f_raw = open("./recv.raw", "wb")

data = f_pcap.read()
pos = 0

while pos != -1:
    pos = data.find("\x01\x01\x30")
    data = data[pos+3:]
    f_raw.write(data[:0x30])

f_pcap.close()
f_raw.close()