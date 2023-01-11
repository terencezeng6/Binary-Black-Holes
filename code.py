# Binary Black Holes, Computational Physics

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

m1 = 7.20018E+31 #kg
m2 = 5.78799E+31 #kg

G = 6.67408E-11 #m3 kg-1 s-2, Gravitational Constant

m1_pos = np.array([-8.0E+5, 0, 0]) #meters, initial position of object 1
m1_vel = np.array([0, -3.90E+7, 0]) #m/s, initial velocity of object 1

m2_pos = np.array([8.0E+5, 0, 0]) #meters, initial position of object 2
m2_vel = -m1/m2*m1_vel #m/s, initial velocity of object 2

com = (m1*m1_pos+m2*m2_pos)/(m1+m2) #position of the center of mass in meters

com_v = (m1*m1_vel+m2*m2_vel)/(m1+m2) #position of the center of mass velocity in meters

ke = (1/2*m1*m1_vel**2)+(1/2*m2*m2_vel**2) #total kinetic energy in joules

t = 0 #starting time
dt = 0.0001 #time step in seconds
c = 299792458 #speed of light in m/s

#lists
time = []
m1_x = []
m1_y = []
m1_z = []
m2_x = []
m2_y = []
m2_z = []
omega_list = [sqrt((G*(m1+m2))/((np.linalg.norm(m1_pos-m2_pos))**3))]
t_e = []
radius = []

def omega(r): #function for calculating angular frequency based on distance from the center
    return sqrt((G*(m1+m2)) / (r**3))

def total_energy(omega,r): #function for calculating the total energy based on the angular frequency and distance
    return -G*m1*m2/r + ke

#iteration using Euler's method:

#exit conditions for loop:
#condition 1: a certain amount of time has elapsed
#condition 2: the two black holes have collided, based on the schwarzschild equation
while t < (3600*24*365*.000001) and np.linalg.norm(m1_pos-m2_pos) > (2*G/c**2)*(m1+m2):

    #updating positions
    m1_x.append(m1_pos[0])
    m1_y.append(m1_pos[1])
    m1_z.append(m1_pos[2])
    m2_x.append(m2_pos[0])
    m2_y.append(m2_pos[1])
    m2_z.append(m2_pos[2])
    
    time.append(t) #updating time
    r = m1_pos - m2_pos #the vector of the distances between the two objects
    dist=np.linalg.norm(r) #the magnitude of the distance vector between the two objects
    ke = (0.5*m1*np.linalg.norm(m1_vel)**2) + (0.5*m2*np.linalg.norm(m2_vel)**2) #calculation of kinetic energy
    omega_list.append(omega(dist)) #adding angular frequency to the list of angular frequencies
    radius.append(dist) #adding distance to the list of distances

    delta_omega = (omega_list[-1] - omega_list[-2]) / dt #calculating the change in angular frequency over time
    
    #Energy Calculations - energy loss over time and adding to the total energy list
    e_loss = ((1/3*(G**(2/3)))*(m1*m2/((m1+m2)**(1/3)))*(1/(omega(dist)**(1/3)))*delta_omega)
    t_e.append(total_energy(omega,dist))

    F_m2_on_m1 = (G*m1*m2/dist**2 * -r/dist)
    F_m1_on_m2 = F_m2_on_m1*-1 #Newton's third law: equal and opposite forces
    #Newton's second law
    a_m1 = F_m2_on_m1/m1
    a_m2 = F_m1_on_m2/m2
    
    #value to multiply velocity by - it cannot be greater than 1, because the velocity should not increase over time
    q = min(sqrt(1+(e_loss*dt/ke)),1)
    
    #updating velocity based on acceleration
    m1_vel += dt*a_m1 
    m1_vel *= q
    m2_vel += dt*a_m2
    m2_vel *= q
    #updating position based on velocity
    m1_pos += dt*m1_vel
    m2_pos += dt*m2_vel
    t += dt #updating the time
    
#convert distance and radii into km
m1_x = [i/1000 for i in m1_x]
m1_y = [i/1000 for i in m1_y]
m2_x = [i/1000 for i in m2_x]
m2_y = [i/1000 for i in m2_y]
com /= 1000
radius = [i/1000 for i in radius]

#plotting figures - position of object 1, position of object 2, and position of center of mass, respectively
plt.figure()
plt.plot(m1_x,m1_y, 'r')
plt.plot(m2_x,m2_y, 'g')
plt.plot(com[0],com[1],'o')
plt.gca().set_aspect('equal')
plt.xlabel("position, in km")
plt.ylabel("position, in km")
plt.show()
    
#plotting figures - total energy over time and radius over time
plt.figure()
plt.plot(time, t_e)
plt.xlabel("Time, in seconds")
plt.ylabel("Total energy, in 10^47 * Joules")
plt.show()
plt.figure()
plt.axhline(y = min(radius), color = 'r', linestyle = '--')
plt.plot(time, radius)
plt.xlabel("Time, in seconds")
plt.ylabel("Radius, in km")
plt.show()
print("Schwarzschild radius:", min(radius), "km") #distance between the two black holes where they turn into one black hole
