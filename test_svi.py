from arbitrage.frameworks.svi import SVI, SSVI, ReducedSVI
import numpy as np
# Axel Vogt arbitrage arbitrageable smile

vt, ut, ct, pt, vmt, t = .01742625, -.1752111, 1.316798, .6997381, .0116249, 1.0
svi = SVI(vt, ut, ct, pt, vmt, t)
k = np.linspace(-1.5,1.5,100).tolist()

w = [svi.get_total_variance(ki) for ki in k]
print(w)