import numpy as np
import matplotlib.pyplot as plt

# Define the butterfly curve equation
def butterfly_curve(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
    return x, y

# Generate values for t
t = np.linspace(0, 24*np.pi, 1000)

# Calculate x and y coordinates using the butterfly curve equation
x, y = butterfly_curve(t)

# Plot the butterfly curve
plt.plot(x, y, color='blue')
plt.axis('equal')
plt.title('Butterfly Curve @Kreggscode')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
