from pippi import dsp
from pippi import tune
import rhodes

#freqs = tune.fromdegrees([0,1,2,3,4,5,6,9], 3, 'c', scale=range(12))

# interval map for chords...
chords = {
        1: [1, 4, 7],
        2: [2, 5, 8],
        3: [3, 6, 9],
        4: [4, 7, 10],
        5: [5, 8, 11], 
        6: [6, 9, 12], 
        7: [7, 10, 1], 
        8: [8, 11, 2], 
        9: [9, 12, 3],
        10: [10, 1, 4], 
        11: [11, 2, 5],
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
for root in range(12):
    roots += [ lastroot ]
    nextroot = choose_interval(lastroot)
    lastroot = nextroot

print roots

freqs = [ tune.fromdegrees([ cr - 1 for cr in chords[root]], 3, 'c', scale=range(12)) for root in roots ]

out = ''

#f = [ dsp.randchoose(freqs) for f in range(3) ]

for r in range(50):
    layers = []

    for i in range(3):
        #if r % 5 == 0:
            #f = [ dsp.randchoose(freqs) for f in range(3) ]

        f = freqs[r % len(freqs)]

        notes = []
        for n in range(dsp.randint(10, 20)):
            notes += [ rhodes.rhodes(dsp.mstf(dsp.rand(80, 90)), f[n % len(f)]) ]

        layers += [ ''.join(notes) ]

    out += dsp.mix(layers)

dsp.write(out, 'riley')
