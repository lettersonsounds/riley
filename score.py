from pippi import dsp
from pippi import tune
import rhodes

freqs = tune.fromdegrees([1,3,5,6,9], 3, 'c')

layers = []
for i in range(3):
    f = [ dsp.randchoose(freqs) for f in range(3) ]
    layers += [ ''.join([ rhodes.rhodes(dsp.mstf(dsp.rand(80, 90)), f[ ii % len(f) ]) for ii in range(dsp.randint(10, 20)) ]) ]

out = dsp.mix(layers)

dsp.write(out, 'riley')
