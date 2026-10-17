import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin

# Simulate PM2.5 data: trend + daily cycle + noise
fs = 1  # 1 sample per minute
t = np.arange(0, 1440) # 1440 mins = 1 day
trend = 50 + 0.02*t
daily_cycle = 20*np.sin(2*np.pi*0.0007*t)
noise = 10*np.random.randn(len(t))
pm25_raw = trend + daily_cycle + noise

# 1. Moving Average Filter
def moving_avg(x, N=5):
    return np.convolve(x, np.ones(N)/N, mode='same')

pm25_ma = moving_avg(pm25_raw, 10)

# 2. FIR Low-pass Filter
fir_coeff = firwin(numtaps=21, cutoff=0.1, window='hamming')
pm25_fir = lfilter(fir_coeff, 1.0, pm25_raw)

# 3. IIR Butterworth Filter
def butter_lowpass(cutoff, fs, order=4):
    nyq = 0.5*fs
    normal_cutoff = cutoff/nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

b, a = butter_lowpass(0.05, fs, order=4)
pm25_butter = lfilter(b, a, pm25_raw)

# 4. FFT Analysis
N = len(pm25_butter)
X = np.fft.fft(pm25_butter)
freqs = np.fft.fftfreq(N, d=1/fs)
magnitude = np.abs(X)

# Plots
plt.figure(figsize=(10,4))
plt.plot(t, pm25_raw, alpha=0.5, label='Raw PM2.5')
plt.plot(t, pm25_butter, linewidth=2, label='Filtered (Butterworth)')
plt.xlabel('Time (minutes)'); plt.ylabel('PM2.5 (ug/m3)')
plt.title('Raw vs Filtered Air Pollution Signal'); plt.legend(); plt.grid()
plt.savefig('images/filtered_result.png', dpi=150)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(freqs[:N//2], magnitude[:N//2])
plt.title('FFT Spectrum - Dominant Pollution Frequencies')
plt.xlabel('Frequency (Hz)'); plt.ylabel('Magnitude'); plt.grid()
plt.savefig('images/fft_spectrum.png', dpi=150)
plt.show()

print("Filtering done. SNR improved. FFT peak at:", freqs[np.argmax(magnitude[1:N//2])+1])
