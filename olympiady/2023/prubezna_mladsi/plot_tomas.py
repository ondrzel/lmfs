import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

t = [0, 5, 7, 8, 10, 11, 14, 14]
v = [0, 150, 150, 80, 80, 140, 140, 0]

dpi = 100.
lw = 2.*plt.rcParams['lines.linewidth']
plt.rcParams.update({'text.usetex': True,
                     'figure.dpi': dpi,
                     'figure.figsize': [800/dpi, 400/dpi],
                     'font.size': 16,
                     'lines.linewidth': lw})

gridspec_kw = dict(left=0.1, right=0.99, bottom=0.16, top=0.95)
fig, ax = plt.subplots(gridspec_kw=gridspec_kw)
ax.plot(t, v)
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.set_minor_locator(MultipleLocator(10))
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.grid(which='major')

ax.set_xlabel('$t\\,\\left[\\mathrm{min}\\right]$')
ax.set_ylabel('$v\\,\\left[\\mathrm{km}\\cdot\\mathrm{h}^{-1}\\right]$')

fig.savefig('tomas.pdf')

