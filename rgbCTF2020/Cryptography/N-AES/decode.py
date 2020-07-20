from n_aes import *

challenge = b64encode(urandom(64))
padded = pad(challenge, BLOCK_SIZE)

import socket

CNT = 128

class RealServer:
    def __init__(self):
        # create an INET, STREAMing socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect(("challenge.rgbsec.xyz", 34567))
        self.rsock = self.sock
        self.ssock = self.sock

        r = self.recv()
        start_lines = self.split_line(r)
        self.enc_chal = start_lines[0]

    def split_line(self, s):
        return s.decode("ascii").split("\n")

    def send(self, b):
        self.ssock.send(b)

    def recv(self):
        return self.rsock.recv(1024)
        
    def get_enc_chal(self):
        return b64decode(self.enc_chal)

    def encrypt(self, text, seed_bytes):
        text = b64encode(text)
        seed_bytes = b64encode(seed_bytes)

        self.send(b"1\n")
        self.recv()
        self.send(text + b"\n")
        r = self.recv()
        self.send(seed_bytes + b"\n")
        r = self.recv()
        d = self.split_line(r)[0]

        if d[:2] == "b'" and d[-1] == "'":
            d = d[2:-1]
        return b64decode(d)

    def decrypt_bs(self, ciphertext, seed_bytes):
        plaintext = ciphertext
        seed_bytes = seed_bytes

        for byte in reversed(seed_bytes):
            byte = bytes(bytearray([byte]))
            ks = rand_block(byte)
            plaintext = AES.new(rand_block(byte), AES.MODE_ECB).decrypt(plaintext)
        try:
            return unpad(plaintext, BLOCK_SIZE)
        except:
            return None

    def decrypt(self, text, seed_bytes):
        text = b64encode(text)
        seed_bytes = b64encode(seed_bytes)

        self.send(b"2\n")
        self.recv()
        self.send(text + b"\n")
        r = self.recv()
        self.send(seed_bytes + b"\n")
        r = self.recv()
        d = self.split_line(r)[0]
        if d == "Error!":
            return None

        if d[:2] == "b'" and d[-1] == "'":
            d = d[2:-1]
        return b64decode(d)

    def submit(self, guess):
        text = b64encode(guess)

        self.send(b"3\n")
        self.recv()
        self.send(text + b"\n")
        r = self.recv()
        print(r.decode("ascii"))
        return
        d = self.split_line(r)[0]
        if d == "Error!":
            return None

        if d[:2] == "b'" and d[-1] == "'":
            d = d[2:-1]
        return b64decode(d)

    def __del__(self):
        self.sock.close()

class Client:
    def __init__(self, serv):
        self.serv = serv

    def solve(self):
        print("Get challenge")
        e_chal = self.serv.get_enc_chal()
        print(f"Challenge {e_chal}")

        for i in range(256):
            print(f"Trying byte {i}")
            sb = bytes(bytearray([i] * CNT))
            
            d = self.serv.decrypt_bs(e_chal, sb)
            if d is not None:
                try:
                    dec_guess = b64decode(d)
                    print("dg", dec_guess)
                    assert len(dec_guess) == 64
                except:
                    continue
                guess = d
                print(f"Have guess {guess}")
                self.serv.submit(guess)
                break

def main():
    s = RealServer()

    c = Client(s)
    c.solve()
                
if __name__ == "__main__":
    main()

