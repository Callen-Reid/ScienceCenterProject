#some code
import matplotlib.pyplot as plt
import numpy as np
import math

# Parameters
m0 = 3*(10**6)# initial mass of rocket (kg) ### Will have to change
m_rock = 0.51*(10**6) # kg mass of rocket without fuel ### Will have to change
r_init = 99*(10**6) # m distance away from planet during landing/docking stage ### Will have to change
v0 = -7*10**3 # initial velocity (m/s) ### Will have to change
m_mars = 6.39*(10**23) # mass of Mars (kg)
r = 3.3895*(10**6) # radius of Mars (m)
G = 6.67408*(10**-11)# gravitational constant
# g = 9.81 # m/s^2 #earth
# g_mars = 3.711 # m/s^2
F_thrust = 4*10**7 # kg*m/s^2 Reverse thrust of rocket ### Will Have to change constant
v_ex = -4*10**(3) # m/s velocity of ejecting fuel ### Will have to change constant


# Equations
def accel_grav(r):
    g = (G * m_mars) / r**2
    return g

# Time for Simulation
dt = 1 # day
tmax = 500 # days for 5 years
timestep = int(tmax/dt)

# Array for data allocation
time = np.zeros(timestep) # duration of landing/docking
m = np.zeros(timestep) # mass of rocket
x = np.zeros(timestep) # distance from Mars
v = np.zeros(timestep) # velocity (in m/s) of rocket
a = np.zeros(timestep) # acceleration (in m/s^2) of rocket

m[0] = m0

x[0] = r_init
v[0] = v0
a[0] = -accel_grav(r_init)

ifinal = -1
for i in range(1, timestep):
    dm = F_thrust/v_ex
    if m[i-1] >= m_rock:
        m[i] = m[i-1] + dm * dt
    else:
        m[i] = m[i-1]
        F_thrust = 0
    a[i] = a[i-1] - accel_grav(x[i-1]) - F_thrust / m[i-1]
    v[i] = v[i-1] + a[i-1] * dt
    x[i] = x[i-1] + v[i-1] * dt
    time[i] = time[i-1] + dt
    if x[i] <= 0:
        ifinal = i
        break

print(ifinal)
plt.plot(m, label='Mass', color='green')
plt.plot(v, label='Velocity', color='blue')
plt.legend()
plt.show()

plt.plot(a, label='Acceleration')
plt.legend()
plt.show()

plt.plot(x, label='Position', color='black')
plt.legend()
plt.show()
