from fileinput import filename
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
freq = askopenfilename()
x = freq.split('/')
x = x[-1]
x = x.split('.')
filename = x[0]

df = pd.read_table(freq, sep=",")

x=df.iloc[:,0]
y=df.iloc[:,1]

plt.figure(figsize=(15, 10), dpi=80)

plt.plot(x, y)

plt.title('Frequency Response')
plt.xlabel('Hz')
plt.ylabel('dB')
plt.xscale('log')


plt.tight_layout()

plt.xlim(x.min(), x.max())
plt.ylim(y.min(), y.max()+1)


plt.savefig(filename+'.png')
#plt.show()
