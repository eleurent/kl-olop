import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
from rl_agents.utils import bernoulli_kullback_leibler

vkl = lambda p, q: p * np.log(p/q) + (1 - p)*np.log((1-p)/(1-q))
kl = bernoulli_kullback_leibler
diff_ukl = lambda S, N, f, v: np.array([N*kl(S/N, q) - f for q in v])

def ukl(S, N, f, count=100):
    xx = np.linspace(0, 1, count)
    dd = diff_ukl(S, N, f, xx)
    i = np.nonzero(dd < 0)[0][-1]
    return xx[i]

def lkl(S, N, f, count=100):
    xx = np.linspace(0, 1, count)
    dd = diff_ukl(S, N, f, xx)
    i = np.nonzero(dd < 0)[0][1]
    return xx[i]


mu = 0.4
N = 10
S = mu*N
f = 0.4*N  # compare to KL = f/N


plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(0, 1, 1000)
plt.text(mu, f/N, r'$\frac{1}{T_a}f(m)$', rotation=0, horizontalalignment="center", verticalalignment="bottom")
plt.plot(x, vkl(S/N, x), label=r"$d(\hat{\mu}_a, q)$")
plt.xlim([0, 1])
plt.ylim([0, 1.5])
plt.legend()
xticks = [0, lkl(S, N, f), mu, ukl(S, N, f), 1]
plt.xticks(xticks, ('0', r'$L^{\mu}_a$', r'$\hat{\mu}_a$', r'$U^{\mu}_a$', '1'))
plt.yticks([])
xticks_grid = [lkl(S, N, f), ukl(S, N, f)]
yticks_grid = [0, f / N]
ax.set_xticks(xticks_grid, minor=True)
ax.set_yticks(yticks_grid, minor=True)
ax.grid(which='minor')
plt.savefig("img/ukl.eps")
plt.show()

