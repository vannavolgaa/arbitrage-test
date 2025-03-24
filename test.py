from arbitrage.datastructures.datetime import DateTime

from arbitrage.math.quadratures import GaussLaguerreQuadrature

test = GaussLaguerreQuadrature(20)

test.get_roots()
test.get_weights()

