import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('TYPES OF DAMPING')
st.header('',divider='rainbow')


A=int(st.number_input('Enter the Amplitude'))
m=int(st.number_input('Enter the mass',min_value=1))
k=int(st.number_input('Enter the spring constant value'))
b=int(st.number_input('Enter damping constant value'))
#dt = 0.01

tmax = 40
dt = 0.001

print(b**2-4*m*k)

def funcv(v):
    return ((1/m)*(-k*(x[i])-(b*v)))
def funcx():
    return v[i]


t = [0]
v = [0]
x = [A]
i = 0

while t[-1] <= tmax:
    k1x = funcx()
    k2x = funcx()
    k3x = funcx()
    k4x = funcx()

    x.append(x[i] + ((1 / 6) * (k1x + 2 * k2x + 2 * k3x + k4x) * dt))

    k1 = funcv(v[i])
    k2 = funcv(v[i] + 0.5 * k1 * dt)
    k3 = funcv(v[i] + 0.5 * k2 * dt)
    k4 = funcv(v[i] + k3 * dt)

    v.append(v[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * dt)

    t.append(t[-1] + dt)
    i += 1

if (b**2-4*m*k)>0:
    plt.subplot(1,2,1)
    plt.plot(t,x,color='red')
    plt.ylim(-A-1, A+1)
    plt.grid()
    plt.title('Overdamped')
    plt.subplot(1,2,2)
    plt.plot(t,v,color='red')
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

if (b**2-4*m*k)==0:
    plt.subplot(1,2,1)
    plt.plot(t,x,color='red')
    plt.ylim(-A-1, A+1)
    plt.grid()
    plt.title('Critical Damping')
    plt.subplot(1,2,2)
    plt.plot(t,v,color='red')
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')

if (b**2-4*m*k)<0:
    plt.subplot(1,2,1)
    plt.plot(t,x,color='red')
    plt.ylim(-A-1, A+1)
    plt.grid()
    plt.title('Underdamped')
    plt.subplot(1,2,2)
    plt.plot(t,v,color='red')
    plt.grid()
    plt.savefig('graph.jpg')
    st.image('graph.jpg')