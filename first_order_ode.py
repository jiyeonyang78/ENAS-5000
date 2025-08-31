'''
Solving the intital value problem for a first order ordinary differential equation using Newton's law of cooling.
-   An ojbect having a temperature of 90F is placed in an environment kept at 60. Ten minutes later, the temperature of the object is 88F.
    What will be the temperature of the object after 20 minutes? 
    How long will it take for the object to reach a temperature of 65F?

-   Date: August 30, 2025
'''

import math
import matplotlib.pyplot as plt
import numpy as np

T_env = 60
T0 = 90
T10 = 88
t1 = 10

k = - (1 / t1) * math.log((T10 - T_env) / (T0 - T_env))

def T(t):
    return T_env + (T0 - T_env) * np.exp(-k * t)

ts = np.linspace(0, 300, 400)
temps = T(ts)

T20 = T(20)
T_target = 65
t_target = - (1 / k) * math.log((T_target - T_env) / (T0 - T_env))

plt.figure(figsize=(8,5))
plt.plot(ts, temps, label="Temperature curve T(t)")
plt.scatter([0, 10, 20], [T0, T10, T20], color="red", label="Known points")
plt.axhline(T_env, linestyle="--", label="Ambient (60°F)")
plt.axhline(T_target, linestyle=":", color="gray")
plt.axvline(t_target, linestyle=":", color="gray",
            label=f"Time to 65°F ≈ {t_target:.1f} min")
plt.title("Newton's Law of Cooling")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°F)")
plt.legend()
plt.grid(True)
plt.show()
