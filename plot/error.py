import matplotlib.pyplot as plt
import numpy as np

Yt0=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,1.889049711,1.052140611,1.643018713,0.468465787,0.277922342,0.490796718,0.332939269,0.229648609,0.18579093,0.161791224,0.138632852,0.129079079,0.140150007,0.108474819,0.115033978,0.14393673,0.108890985,0.121783909,0.112677493,0.132680393,0.127010282,0.12095591,0.134710242,0.109590012,0.111072665,0.107049278,]

Yt40=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,28.1332979,19.82132142,0.627303649,0.347726298,0.307558874,0.318667829,0.184449125,0.25889655,0.333899649,0.185456209,0.332322669,0.30296607,0.303753243,0.273750346,0.266641504,0.423873527,0.330429613,0.489201609,0.312527146]

Yr0=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,8.752384131,7.746338143,7.871530109,4.131603333,4.794495223,5.41160008,1.708752814,1.508233884,1.641141507,1.096565107,0.678711262,0.384775842,0.334293822,0.264067208,0.25934925,0.274657728,0.214831601,0.320364416,0.29531822,0.264543888,0.344398755,0.315147768,0.318973335,0.270412444,0.233431971,0.246535968]

Yr40=[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,17.35977827,14.72483706,0.669712734,0.43941003,0.233530898,0.262419726,0.178350001,0.171514655,0.23126684,0.192377948,0.200591519,0.238922553,0.229498455,0.305773737,0.714753782,0.359623887,0.395631774,0.460948579,0.365019753]

x=[0.000768,0.001728,0.003072,0.0048,0.0075,0.0108,0.0147,0.017328,0.0192,0.0243,0.03,0.0363,0.047628,0.0588,0.0675,0.0768,0.0972,0.12,0.1452,0.1728,0.1875,0.2187,0.2523,0.27,0.3072,0.3468,0.3888,0.4332,0.48,0.5808,0.6075,0.6912,0.8748,1.2288,1.5552,1.92,2.43,2.7648,3,3.63,4.6128,5.07,5.5488,5.88,6.75,7.8732,8.8752,9.9372,11.244288,12]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x,Yt0,'g.',label="Trans. Err. (0˚ VA)", markersize = 20)
ax1.plot(x,Yt40,'r1', label = "Trans. Err. (48˚ VA)", markersize = 20)
ax2.plot(x,Yr0, 'bx', label = "Rot. Err. (0˚ VA)", markersize = 20)
ax2.plot(x,Yr40, 'k+', label = "Rot. Err. (48˚ VA)", markersize = 20)
ax1.set_xlabel('Number of megapixels captured per frame', fontsize = 48)
ax1.set_ylabel('L2-norm translation error (cm)', fontsize = 48)
ax2.set_ylabel('L2-norm rotation error (degree)', fontsize = 48)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc = 'upper right', fontsize=48)
ax1.tick_params(axis = 'both', labelsize = 34)
ax2.tick_params(axis = 'both', labelsize = 34)
plt.show()

