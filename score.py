from pippi import dsp
from pippi import tune
import rhodes

# interval map for chords...
maj = [1, 3, 5, 6, 8, 10, 12]
chords = {
        1: [1, 5, 8],
        2: [2, 5, 8],
        3: [3, 6, 10],
        4: [4, 6, 10],
        5: [5, 8, 12], 
        6: [6, 8, 12], 
        7: [7, 10, 1], 
        8: [8, 10, 1], 
        9: [9, 12, 3],
        10: [10, 1, 5], 
        11: [11, 3, 5],
        12: [12, 3, 6],
        }

def choose_interval(lastroot):
    interval = dsp.randchoose([3, 4, -3, -4])
    if interval + lastroot >= 1 and interval + lastroot <= 12:
        nextroot = lastroot + interval
    else:
        nextroot = choose_interval(lastroot)

    return nextroot

roots = []
lastroot = 1
for root in range(6):
    roots += [ lastroot ]
    nextroot = choose_interval(lastroot)
    lastroot = nextroot

print roots

freqs = [ tune.fromdegrees([ cr - 1 for cr in chords[root]], 3, 'c', scale=range(12)) for root in roots ]

out = ''

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
