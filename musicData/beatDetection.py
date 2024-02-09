import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load the audio file
audio_path = 'C:\\Users\\miguel.marques\\Documents\\NeoPixel-Emulator\\musicData\\helloalien.mp3'  # Replace 'your_audio_file.mp3' with the path to your audio file
y, sr = librosa.load(audio_path)

# Calculate the duration of the audio track
duration = librosa.get_duration(y=y, sr=sr)

# Calculate the number of half-second intervals
num_intervals = int(duration * 2)

# Calculate the amplitude envelope using a rolling window maximum
amplitude_envelope = np.abs(librosa.effects.preemphasis(y))
amplitude_envelope = librosa.util.normalize(amplitude_envelope)

# Calculate brightness values for each half-second interval
brightness_values = []
for i in range(num_intervals):
    start_time = i * 0.5  # Start time of the interval
    end_time = (i + 1) * 0.5  # End time of the interval
    start_frame = librosa.time_to_frames(start_time, sr=sr)
    end_frame = librosa.time_to_frames(end_time, sr=sr)
    max_amplitude = np.max(amplitude_envelope[start_frame:end_frame])
    brightness_values.append(max_amplitude)

# Convert brightness values from range 0-1 to range 0-100
#brightness_values_scaled = [int(b * 10000) for b in brightness_values]

# Plot LED brightness levels
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(brightness_values)), brightness_values, marker='o')
plt.title('LED Brightness Over Time')
plt.xlabel('Half-Second Intervals')
plt.ylabel('LED Brightness')
#plt.show()
