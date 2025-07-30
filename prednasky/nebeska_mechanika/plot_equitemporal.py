import numpy as np
import matplotlib.pyplot as plt

dpi = 100
plt.rcParams.update({'figure.figsize': (1600/dpi, 1180/dpi),
                     'figure.dpi': dpi})

gridspec_kw = dict(left=0.04, right=0.98, top=0.96, bottom=0.04)

fig, axes = plt.subplots(nrows=3, ncols=4, gridspec_kw=gridspec_kw)
axes = [ax for sub_axes in axes for ax in sub_axes]
phi = np.linspace(0., 2*np.pi, 1001)

#for e, ax in zip([0., .1, .2, .3, .4, .5, .6, .7, .8, .9, .99, .999], axes):
for e, ax in zip([0., .1, .2, .3, .4, .5, .7, .9, .99, .999, .9999, .99999], axes):
    mean_anomalies = np.linspace(0., 2*np.pi, 17)[:-1]
    eccentric_anomalies = np.copy(mean_anomalies)
    for i in range(100):
        eccentric_anomalies = mean_anomalies + e*np.sin(eccentric_anomalies)
    cos_true_anomalies = (np.cos(eccentric_anomalies) - e)/(1 - e*np.cos(eccentric_anomalies))
    sin_true_anomalies = np.sqrt(1 - cos_true_anomalies**2)*np.sign(np.sin(mean_anomalies))

    p = 1. - e**2
    cosphi = np.cos(phi)
    r = p/(1 + e*cosphi)
    ax.plot(r*cosphi, r*np.sin(phi), c='black')

    r = p/(1 + e*cos_true_anomalies)
    ax.scatter(r*cos_true_anomalies, r*sin_true_anomalies, c='black')
    ax.set_title('e = %f' % e)
    ax.set_aspect(1)
    ax.set_ylim((-1.1, 1.1))

fig.savefig('kepler_equitemporal.pdf')
