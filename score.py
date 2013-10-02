from pippi import dsp
from pippi import tune
import rhodes

freqs = tune.fromdegrees([0,1,2,3,4,5,6,9], 3, 'c', scale=range(12))

out = ''

f = [ dsp.randchoose(freqs) for f in range(3) ]

for r in range(50):
    layers = []

    for i in range(3):
        if r % 5 == 0:
            f = [ dsp.randchoose(freqs) for f in range(3) ]

        notes = []
        for n in range(dsp.randint(10, 20)):
            notes += [ rhodes.rhodes(dsp.mstf(dsp.rand(80, 90)), f[n % len(f)]) ]

        layers += [ ''.join(notes) ]

    out += dsp.mix(layers)

dsp.write(out, 'riley')
