import sounddevice as sd
import numpy as np

duration = 2  # seconds
frequency = 440  # Hz (A4 tone)

sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# sd.default.device = None
sd.play(wave, samplerate=sample_rate)
sd.wait()
