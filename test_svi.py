from arbitrage.frameworks.svi import SVI
import numpy as np
import matplotlib.pyplot as plt

# Axel Vogt arbitrage arbitrageable smile
vt, ut, ct, pt, vmt, t = .01742625, -.1752111, 1.316798, .6997381, .0116249, 1.0
svi = SVI(vt, ut, ct, pt, vmt, t)
k = np.linspace(-1.5,1.5,100).tolist()
w = [svi.get_total_variance(ki) for ki in k]
rnd = [svi.get_risk_neutral_density(ki) for ki in k]
svi.set_vmt(0.01548182)
svi.set_ct(.3493158)
w2 = [svi.get_total_variance(ki) for ki in k]
rnd2 = [svi.get_risk_neutral_density(ki) for ki in k]
svi.set_vmt(0.0116249)
svi.set_ct(.8564763)
w3 = [svi.get_total_variance(ki) for ki in k]
rnd3 = [svi.get_risk_neutral_density(ki) for ki in k]

plt.plot(k, w)
plt.plot(k, w2)
plt.plot(k, w3)
plt.title('SVI Total Variance')
plt.legend(['Vogt', 'Guaranteed Arbitrage free', 'Optimal Arbitrage free'])
plt.show()

plt.plot(k, rnd)
plt.plot(k, rnd2)
plt.plot(k, rnd3)
plt.title('SVI Risk Neutral Density')
plt.legend(['Vogt', 'Guaranteed Arbitrage free', 'Optimal Arbitrage free'])
plt.show()