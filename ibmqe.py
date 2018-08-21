import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg.lapack as lapak
from mpl_toolkits.mplot3d import Axes3D


def bdsCorr():
    from math import acos, sqrt
    c1 = -0.9
    c2 = -0.8
    c3 = -0.8
    from states import rho_bds
    rho = np.zeros((4, 4), dtype=complex)
    rho = rho_bds(c1, c2, c3)
    eig = lapak.zheevd(rho)
    print('eigens:', eig[0][0], eig[0][1], eig[0][2], eig[0][3])
    import discord
    dp = 0.05
    d = 20*(1-0)
    di = np.zeros(d)
    cc = np.zeros(d)
    mi = np.zeros(d)
#    diE = np.zeros(d)
#    ccE = np.zeros(d)
#    miE = np.zeros(d)
#    rhopE = np.zeros((4, 4), dtype=complex)
    pv = np.zeros(d)
    rhop = np.zeros((4, 4), dtype=complex)
#    import kraus
#    import tomography as tomo
    p = -dp
    for j in range(0, d):
        p = p + dp
#        rhop = kraus.rho_pd(p, rho) # ; print(rhop) # teste para ver rhop
        c1p = c1*(1.0-p)**2
        c2p = c2*(1.0-p)**2
        c3p = c3
        print("p = ", p, ", c1p=", c1p, ", c2p=", c2p, ", c3p=", c3p)
        p00 = (1.0 + c1p - c2p + c3p)/4.0
        p01 = (1.0 + c1p + c2p - c3p)/4.0
        p10 = (1.0 - c1p + c2p + c3p)/4.0
        p11 = (1.0 - c1p - c2p - c3p)/4.0
        print("p00 = ", p00, ", p01=", p01, ", p10=", p10, ", p11=", p11)
        theta = 2.0*acos(sqrt(p00 + p01))
        alpha = 2.0*acos(sqrt(p00 + p10))
        print("theta = ", theta, ", alpha", alpha)
        print("")
        rhop = rho_bds(c1p, c2p, c3p)
        pv[j] = p
        di[j] = discord.discord_oz_bds(rhop)
        cc[j] = discord.ccorr_hv_bds(rhop)
        mi[j] = discord.mi_bds(rhop)
        '''sj = str(j)
        path1 = '/home/jonasmaziero/Dropbox/Research/IBM_QC/'
        path2 = 'tomography/BDS/bell_diagonal/'
        path = path1 + path2 + sj + '/'
        rhopE = tomo.tomo_2qb(path)
        diE[j] = discord.discord_oz_bds(rhopE)
        ccE[j] = discord.ccorr_hv_bds(rhopE)
        miE[j] = discord.mi_bds(rhopE)
        eigE = lapak.zheevd(rhopE)
        print('eigensE:', eigE[0][0], eigE[0][1], eigE[0][2], eigE[0][3])
        print('di =', di[j], '  diE = ', diE[j])'''
    plt.plot(pv, di, label='di')
    plt.plot(pv, cc, label='cc')
    plt.plot(pv, mi, label='im')
    plt.xlabel('p')
    plt.legend()
    plt.show()


def werner():
    import tomography as tomo
    rhoE = np.zeros((4, 4), dtype=complex)
    import entanglement as ent
    Ne = 15
    we = np.array([0, 0.1, 0.2, 0.3, 0.32,
                   0.34, 0.36, 0.38, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    Ee = np.zeros(Ne)
    for j in range(0, Ne):
        sj = str(j)
        path1 = '/home/jonasmaziero/Dropbox/Research/ibm/bds/'
        path2 = 'werner_qx2/dados_plot/'
        path = path1 + path2 + sj + '/'
        rhoe = tomo.tomo_2qb(path)
        Ee[j] = ent.concurrence(rhoe)
    Nt = 100
    Et = np.zeros(Nt)
    wt = np.zeros(Nt)
    from states import Werner
    dw = 1.01/Nt
    w = -dw
    for j in range(0, Nt):
        w = w + dw
        if w > 1.0:
            break
        rho = Werner(w)
        Et[j] = ent.concurrence(rho)
        wt[j] = w

    plt.plot(we, Ee, label='Ee')
    plt.plot(wt, Et, label='Et')
    plt.xlabel('w')
    plt.legend()
    plt.show()


# werner()
