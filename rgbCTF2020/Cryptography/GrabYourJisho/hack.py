import re
import numpy as np
import os
import scipy.stats

os.system("touch soln_tbl")

#['\n', ' ', '!', '"', '$', '%', '&', "'", '(', ')', '*', ',', '-', '.', '/', ':', ';', '=', '?', '@', '[', ']', '_']

class Workpad:
    def __init__(self, s, wf):
        self.s = s
        self.wf = {w.upper(): f for w, f in wf.items()}

        self.add_contractions()

        del self.wf["RE"]
        
        sw = sorted(list(self.wf.keys()), key=lambda w: self.wf[w])
        sw = sw[::-1]
        self.flat_dict = (" " + " ".join(sw) + " ").upper()
        self.soln = {}
        self.exclude = []

    def add_contractions(self):
        with open("/usr/share/dict/words") as f:
            for line in f:
                line = line.rstrip()
                if "'" in line:
                    self.add_contraction(line)

    def add_contraction(self, w):
        w = w.upper()
        assert "'" in w
        i = w.index("'")
        start = w[:i]
        if start in self.wf:
            if w in self.wf:
                old = self.wf[w]
            else:
                old = -100.
            self.wf[w] = max(old, self.wf[start])

    def separate_words(self):
        self.words = re.split("[-\n !\"\$%&()\*,\./:;=?@\[\]_]+",self.s)
        self.words = self.words[:-1]

        self.confs = np.array([0.0 for w in self.words])
        self.guesses = ["" for w in self.words]

        return
        for w in self.words:
            if "'" in w:
                print(w)

    def get_conf(self, w):
        # Get confidence of a word
        # Convert w to a regex
        return 0.0, ""
        guessed = [c for c in w if (ord(c) < 256 and c != "'")]
        if len(guessed) == 0:
            return 0.0, ""

        guessed = [c for c in w if (ord(c) > 256)]
        if len(guessed) == 0:
            return 0.0, ""

        match = self.get_possibilities(w)

        if len(match) == 1:
            w = match[0]
            if self.wf[w] > -4.5:
                return 5. + self.wf[w], w
        return 0.0, ""

        if len(match) > 0 and len(match) < 300:
            scores = np.array([self.wf[x] for x in match])
            score = np.exp(scores[0]) / (np.sum(np.exp(scores)) + np.exp(2.5))
            if "'" in r:
                #print(r)
                #print(scores[:10])
                pass
            return score, match[0][1:-1]
            #print(score)
            if len(scores) == 1:
                return scores[0], match[0]
            else:
                return scores[0] - scores[1], match[0]
        else:
            return 0.0, ""
            #return score * 1.

    def subs(self, ct, pt):
        if len(pt) != len(ct):
            print(pt, ct)
            raise

        for c, p in zip(ct, pt):
            if ord(c) >= 256 and c not in self.soln:
                self.soln[c] = p.upper()

        for i, w in enumerate(self.words):
            w0 = w[:]
            for c, p in zip(ct, pt):
                if ord(c) >= 256:
                    w = w.replace(c, p.upper())

            if w != w0:
                if i % 100 == 0 and False:
                    print(i / len(self.words))
                self.words[i] = w
                s, g = self.get_conf(w)
                self.confs[i] = s
                self.guesses[i] = g

    def save(self):
        s = ""
        for x, y in self.soln.items():
            s += x
            s += y
        with open("soln_tbl", "w") as f:
            f.write(s)

    def save_doc(self):
        with open("soln", "w") as f:
            f.write("\n".join(self.words))

    def load(self):
        with open("soln_tbl", "r") as f:
            d = f.read()
        assert len(d) % 2 == 0
        pt = ""
        ct = ""
        for i in range(0, len(d), 2):
            self.soln[d[i]] = d[i + 1]
            ct += d[i]
            pt += d[i + 1]

        self.subs(ct, pt)

    def get_possibilities(self, w):
        r = " " + "".join(["[A-Z]" if ord(c) >= 256 else c.upper() for c in w]) + " "
        match = re.findall(r, self.flat_dict)
        return [m[1:-1] for m in match]
    
    def get_log_prob(self, w):
        V = 1.
        match = self.get_possibilities(w)

        if len(match) == 0:
            return np.log(0.0001)

        if len(match) > 30:
            match = match[:30]

        scores = np.array([self.wf[x] for x in match])
        #return scores[0]

        s = np.log(np.sum(np.exp(scores)) + 0.0001)
        return s

    def score_candidate(self, wl, c, p):
        score = 0.0
        if len(wl) > 100:
            print(len(wl))
            wl = wl[:100]
            
        for w in wl:
            w = w.replace(c, p)
            score += self.get_log_prob(w)
        print(p, score)
            
        return score
    
    def find_candidate(self, wl, c):
        cands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        scores = np.zeros(len(cands))
        
        for i, p in enumerate(cands):
            scores[i] = self.score_candidate(wl, c, p)

        best_i = np.argmax(scores)
        return cands[best_i]

    def scores_for_word(self, w, cands, ind):
        match = self.get_possibilities(w)

        scores = np.zeros(len(cands))
        total = 0.

        if len(match) == 0:
            return scores

        for m in match:
            C = m[ind]
            assert C in cands
            j = cands.index(C)
            scores[j] += np.exp(self.wf[m])
            total += np.exp(self.wf[m])
        return scores / total

    def find_candidate2(self, wl, c):
        cands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        scores = np.zeros(len(cands))

        if len(wl) > 1000:
            wl = wl[:1000]

        for w in wl:
            ind = w.index(c)
            scores += self.scores_for_word(w, cands, ind)

        ss = sorted(list(scores))[::-1]
        print(ss[0] / ss[1])
        winner = np.argmax(scores)
        print(cands[winner])
        #if ss[0] / ss[1] < 2:
        #return None
        
        return cands[winner]

    def improve2(self):
        # What is the most popular unsolved char?
        all_ = np.array([ord(c) for c in "".join(self.words) if c not in self.exclude])
        all_ = all_[all_ >= 256]
        most_common = chr(scipy.stats.mode(all_)[0][0])

        #w = [w for w in self.words if "RGBCTF" in w][0]
        #w = [c for c in w if ord(c) >= 256]
        #most_common = w[0]

        wl = [w for w in self.words if most_common in w]
        p = self.find_candidate2(wl, most_common)
        print("Candidate says", p)
        #p = self.find_candidate(wl, most_common)
        print(most_common, p)
        print()
        if p is not None:
            self.subs(most_common, p)
        else:
            self.exclude.append(most_common)

        return True
        
        pass
        
    def solve(self):
        self.separate_words()
        self.load()

        URL = "昒鏽霱彊://鱓攫襵.扺譸醸叏褖𠆢夳鯁曵.蕐屩形/"
        self.subs(URL[:4], "http")
        self.subs(URL[7:10], "www")
        self.subs(URL[-4:-1], "com")

        for i in range(100000):
            if not self.improve2():
                self.save()
                self.save_doc()
                break
            
            self.save()

            self.save_doc()
            
        
def get_wordfreqs():
    wf = {}
    words = []
    counts = []
    with open("word_freqs.txt") as f:
        f.readline()
        for line in f:
            data = line.split()
            w = data[0]
            lf = float(data[6])
            c = int(data[1])
            words.append(w)
            counts.append(c)

    counts = np.array(counts, dtype='float')
    s = np.sum(counts)
    counts /= np.sum(counts)

    counts = np.log(counts)

    for i in range(len(words)):
        wf[words[i]] = counts[i]

    return wf
    
def main():
    with open("grab your jisho.txt", "rb") as f:
        data = f.read()

    decoded = data.decode("utf-8")

    wf = get_wordfreqs()

    wp = Workpad(decoded, wf)

    wp.solve()
        
if __name__ == "__main__":
    main()
