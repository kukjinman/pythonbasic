import numpy
import matplotlib.pyplot as plt

from pythonbasic.my_package import greet, multiply_numbers
from pythonbasic.my_package import farewell as fw

greet("국진맨")

fw("국진맨2")

multiply_numbers(2,4)

x = numpy.linspace(0, 10, 100);

plt.plot(x, numpy.sin(x), label='Sine', color='blue')
plt.show()
