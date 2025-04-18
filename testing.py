import sounddevice as sd

print("default Host API", sd.query_hostapis())
print("available Devices:", sd.query_devices())