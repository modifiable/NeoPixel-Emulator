import librosa
import numpy as np
import matplotlib.pyplot as plt


def amplitude_envelope(signal, frame_size, hop_length, sr):
    """Calculate the amplitude envelope of a signal

    Returns the envelope values and timestamps
    """
    amplitude_envelope = []
    
    # calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length): 
        amplitude_envelope_current_frame = max(signal[i:i+frame_size]) 
        amplitude_envelope.append(amplitude_envelope_current_frame)
    
    values = np.array(amplitude_envelope)
    times = librosa.frames_to_time(np.arange(1, len(values)+1), hop_length=hop_length, sr=sr)
    return  values, times

# Load the audio file
audio_path = 'C:\\Users\\miguel.marques\\Documents\\NeoPixel-Emulator\\musicData\\beat.mp3'  # Replace 'your_audio_file.mp3' with the path to your audio file
audio, sr = librosa.load(audio_path)

# Extract tempo and beat frames
brightness_values, timestamps = amplitude_envelope(audio, frame_size=1024, hop_length=512, sr=sr)

# Convert brightness values from range 0-1 to range 0-100
#brightness_values_scaled = [int(b * 10000) for b in brightness_values]

# Plot LED brightness levels
plt.figure(figsize=(10, 4))
plt.plot(timestamps, brightness_values, marker='o')
plt.title('LED Brightness Over Time')
plt.xlabel('Half-Second Intervals')
plt.ylabel('LED Brightness')
plt.show()
