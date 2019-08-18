from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

fig = Figure()
canvas = FigureCanvas(fig)

x = np.random.randn(10000)
y = np.random.random((1, 5))
print("X:", x)
print("X type:",type(x))
print("Y:", y)
print("Y type:", type(y))
ax = fig.add_subplot(111)
ax.hist(x, 1000)

ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('matplotlib_histogram.png')