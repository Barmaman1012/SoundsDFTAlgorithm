import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 10  # seconds
sampling_rate = 44100  # standard sampling rate

# Step 1: Record audio
print("Recording...")
recording = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1)
sd.wait()  # wait until the recording is finished
print("Recording complete.")

# Flatten and extract the first 600 samples
recording = recording.flatten()
samples = recording[:600] if len(recording) >= 600 else recording

# Step 2: Perform FFT on the samples
fft_result = np.fft.fft(samples)
frequencies = np.fft.fftfreq(len(samples), 5 / sampling_rate)

# Calculate the magnitude of the FFT result
magnitude = np.abs(fft_result)

# Step 3: Plot the result
plt.plot(frequencies[:100], magnitude[:100])  # We plot only positive frequencies
plt.title("Frequency Spectrum of Audio Sample")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
