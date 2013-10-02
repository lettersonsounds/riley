from pippi import dsp
from pippi import tune
import rhodes

# interval map for chords...
maj = [1, 3, 5, 6, 8, 10, 12]
#      C  D  E  F  G  A   B

chords = {
        1: [1, 5, 8],   # C  E  G
        2: [2, 5, 8],   # C# E  G
        3: [3, 6, 10],  # D  F  A
        4: [4, 6, 10],  # Eb F  A
        5: [5, 8, 12],  # E  G  B
        6: [6, 8, 12],  # F  G  B
        7: [7, 10, 1],  # F# A  C
        8: [8, 10, 1],  # G  A  C
        9: [9, 12, 3],  # G# B  D
        10: [10, 1, 5], # A  C  E
        11: [11, 3, 5], # Bb D  E
        12: [12, 3, 6], # B  D  F
        }

def choose_interval(lastroot):
    interval = dsp.randchoose([3, 4, -3, -4])
    if interval + lastroot >= 1 and interval + lastroot <= 12:
        nextroot = lastroot + interval
    else:
        nextroot = choose_interval(lastroot)

    return nextroot

def make_chords():
    roots = []
    lastroot = 1
    for root in range(6):
        roots += [ lastroot ]
        nextroot = choose_interval(lastroot)
        lastroot = nextroot

    print roots

    freqs = [ tune.fromdegrees([ cr - 1 for cr in chords[root]], 3, 'c', scale=range(12)) for root in roots ]

    return freqs

out = ''

for times in range(6):
    freqs = make_chords()

    for r in range(50):
        layers = []

        for i in range(3):
            f = freqs[r % len(freqs)]

            notes = []
            for n in range(dsp.randint(10, 20)):
                notes += [ rhodes.rhodes(dsp.mstf(dsp.rand(80, 90)), f[n % len(f)]) ]

            layers += [ ''.join(notes) ]

        out += dsp.mix(layers)

dsp.write(out, 'riley')
