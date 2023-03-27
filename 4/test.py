import matplotlib.pyplot as plt
import numpy as np

# Create the figure and subplots
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# Set x values for all plots
x = np.linspace(-5, 5, 100)

# Plot on the first subplot
axs[0].plot(x, np.sin(x), label='sin(x)')
axs[0].set_title('Plot 1')
axs[0].legend()

# Plot on the second subplot
axs[1].plot(x, np.cos(x), label='cos(x)')
axs[1].set_title('Plot 2')
axs[1].legend()

# Plot on the third subplot
axs[2].plot(x, np.tan(x), label='tan(x)')
axs[2].set_title('Plot 3')
axs[2].legend()

# Add a title for the whole figure
fig.suptitle('Three Plots')

# Show the plot
plt.show()
