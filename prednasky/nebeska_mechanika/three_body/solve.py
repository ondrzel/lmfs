import numpy as np

G = 1
m1 = 1e-5
m2 = 1e-7
M = m1 + m2
mu = G*M
pi1 = m1/M
pi2 = m2/M

r12 = 1e20
x1 = -pi2*r12
x2 = pi1*r12

omega = np.sqrt(mu/r12**3)

'''
x = X[0]
y = X[1]
z = X[2]
v_x = X[3]
v_y = X[4]
v_z = X[5]
'''

def rhs(X):
    r1 = np.sqrt((X[0] - x1)**2 + X[1]**2 + X[2]**2)
    r2 = np.sqrt((X[0] - x2)**2 + X[1]**2 + X[2]**2)
    return [X[3], X[4], X[5], \
            2*omega*X[4] + (omega*X[0])**2 - (X[0] - x1)*mu1/r1**3 - (X[0] - x2)*mu2/r2**3, \
            2*omega*X[3] + (omega*X[1])**2 - X[1]*(mu1/r1**3 + mu2/r2**3), \
            -X[2]*(mu1/r1**3 + mu2/r2**3)]



