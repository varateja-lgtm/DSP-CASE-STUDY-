% Air Pollution Monitoring using Digital Filters and FFT - MATLAB
clc; clear; close all;

fs = 1; % 1 sample/min
t = 0:1439;
trend = 50 + 0.02*t;
daily_cycle = 20*sin(2*pi*0.0007*t);
noise = 10*randn(size(t));
pm25_raw = trend + daily_cycle + noise;

% 1. Moving Average
N = 10;
b_ma = (1/N)*ones(1,N);
pm25_ma = filter(b_ma, 1, pm25_raw);

% 2. FIR Low-pass
fir_coeff = fir1(20, 0.1);
pm25_fir = filter(fir_coeff, 1, pm25_raw);

% 3. IIR Butterworth
[b_butter, a_butter] = butter(4, 0.05/(0.5*fs), 'low');
pm25_butter = filter(b_butter, a_butter, pm25_raw);

% 4. FFT
Nfft = length(pm25_butter);
X = fft(pm25_butter);
freqs = (0:Nfft-1)*(fs/Nfft);
magnitude = abs(X);

figure;
plot(t, pm25_raw, 'r--'); hold on;
plot(t, pm25_butter, 'b', 'LineWidth', 2);
legend('Raw','Filtered'); title('Raw vs Filtered PM2.5'); grid on;

figure;
plot(freqs(1:Nfft/2), magnitude(1:Nfft/2));
title('FFT Spectrum'); xlabel('Frequency (Hz)'); ylabel('Magnitude'); grid on;
