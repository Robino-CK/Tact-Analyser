
#analyse audio data
#https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
plt.figure(figsize=(14, 5))
audio_data = 'res/test.wav'
ipd.Audio(audio_data)
x , sr = librosa.load(audio_data)
librosa.display.waveshow(x, sr=sr)