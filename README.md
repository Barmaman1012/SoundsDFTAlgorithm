# Audio Analyzer - Piano Tuner

## Authors
- Yaniv Arbel
- Bar Maman
- Gilad Bregman

## Overview
This project demonstrates the application of Fourier Transform techniques to analyze and process audio recordings, specifically for identifying and tuning musical notes. By utilizing the Discrete Fourier Transform (DFT) and its efficient implementation, the Fast Fourier Transform (FFT), we have created an algorithm capable of analyzing piano recordings and assisting in precise tuning.

## Features
- **Frequency Analysis:** Decomposes audio signals into frequency components using FFT.
- **Dominant Frequency Detection:** Extracts the most dominant frequency for any audio note.
- **Piano Tuning:** Identifies deviations in recorded notes and provides recommendations for tuning.
- **Example Application:** Includes an analysis of the "Jingle Bells" song as a practical example.

## Methodology
The Fourier Transform is used to convert time-domain audio signals into their frequency-domain representation. The key steps include:
1. Applying the FFT to an audio signal.
2. Identifying dominant frequencies corresponding to musical notes.
3. Comparing recorded notes with standard piano frequencies to suggest tuning adjustments.

## Technologies Used
- Python
- NumPy
- SciPy
- Matplotlib
