import numpy as np
import matplotlib.pyplot as plt
from task2 import fft
from task3 import ifft

# 1. Wygeneruj próbki sygnału na podstawie zadanych współczynników Ai, ai, Bj, bj
samples_number = 1288
sample_rate = 1 / samples_number
t = np.arange(0, (samples_number - 1) * sample_rate, sample_rate)

Ai = 1
ai = 35
Bj = 2
bj = 25

signal = Ai * np.sin(ai * t) + Bj * np.cos(bj * t)

# 2. Wykonaj szybką transformację Fouriera na próbkach sygnału,
X = np.array(np.fft.fft(signal))

# 3. Wyświetl sygnał i wykres częstotliwości,
Y = np.abs(X)/(samples_number//2) #signal
freq = np.arange(0, (samples_number//2), 1)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, signal)
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.set_title('Signal before filtering')
ax2.plot(freq, Y[:samples_number//2])
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Amplitude')
ax2.set_title('Signal spectrum before filtering')
plt.tight_layout()
plt.show()

# 4. Pobierz od użytkownika informację, które częstotliwości należy usunąć,
to_remove = int(input('Insert frequencies you want to remove(smaller then): '))

# 5. usuń wybrane częstotliwości,
for i in range(to_remove):
    Y[i]=0

# for i in range(600, 800):
#     Y[i]=0
# for i in range(300, 400):
#     Y[i]=0


# Odwrotna szybka transformacja Fouriera
signal = np.array(np.fft.ifft(Y)).real


fig, (ax1, ax2) = plt.subplots(2, 1)
Y = np.abs(Y)/(samples_number//2) #signal
ax1.plot(t, signal)
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax1.set_title('Signal after filtering')
ax2.plot(freq, Y[:samples_number//2])
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Amplitude')
ax2.set_ylim(0, 2)
ax2.set_title('Signal spectrum after filtering')
plt.tight_layout()
plt.show()