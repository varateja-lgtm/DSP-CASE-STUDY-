Air Pollution Monitoring using Digital Filters and Fast Fourier Transform

DSP Case Study - B.Tech ECE

System

Abstract

Air pollution is a critical environmental issue. Raw sensor data (PM2.5, PM10, NO2, CO) is highly noisy due to sensor drift, environmental interference, and quantization noise. This case study demonstrates how Digital Signal Processing techniques - specifically Digital Filters (Moving Average, FIR Low-pass, IIR Butterworth) and Fast Fourier Transform (FFT) - can be used to clean, analyze, and extract meaningful patterns from air pollution data for real-time AQI monitoring and alert systems.

1. Introduction & Problem Statement

  Traditional air quality monitoring systems directly display raw sensor values, leading to false alarms and inaccurate readings. DSP provides a robust solution.

2. Objectives

  Acquire and digitize air pollution signals
  
  Design and apply digital filters for noise removal
  
  Apply FFT for spectral analysis
  
  Calculate AQI and develop threshold-based alerts

4. System Architecture

  

         Sensors -> ADC -> Pre-processing -> Digital Filters -> FFT -> Feature Extraction & AQI -> Visualization & Alert
  
  See images/block_diagram.png


6. Theory

  A) Digital Filters
  
    Moving Average: y[n] = (1/N) * sum(x[n-k])
    
    FIR Low-pass: H(z) = sum(h[n]z^-n), cutoff 0.1*fs, Hamming window
    
    IIR Butterworth: |H(jΩ)|² = 1 / (1 + (Ω/Ωc)^(2N)), Order 4
  
  B) FFT
  
    X[k] = sum(x[n] * exp(-j*2πkn/N))


8. Methodology

  Data Acquisition: PMS5003, MQ135, fs=1 sample/min
  
  Pre-processing: Normalization, interpolation
  
  Filtering: MA(N=10) -> FIR -> Butterworth cascade, SNR 8.2dB to 18.7dB
  
  FFT Analysis: 1024-point FFT, dominant peak at ~1.15e-5 Hz (24hr cycle)
  
  AQI & Alert: CPCB standards

10. Results
  
  Filtering reduces spikes by 70%
  
  FFT reveals daily traffic and weekly industrial patterns
  
  12% more stable AQI, reduced false alerts

11. How to Run
  


        pip install numpy scipy matplotlib
  
        python code/main.py

13. Future Scope
  
  ML integration, Wavelet transform, ESP32 edge implementation


References
  
  Proakis & Manolakis, Oppenheim, CPCB AQI Guidelines, WHO 2024

