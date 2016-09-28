import scipy.io.wavfile
import matplotlib.pyplot as plt 


def get_amplitudes(path):
    result = scipy.io.wavfile.read(path)
    amplitudes = result[1]
    norm_amplitudes = []
    for a in amplitudes:
        norm_amplitudes.append(a[0])
    return norm_amplitudes
    
amplitudes = get_amplitudes("./sqwaks/dool_shmaw/myRecording01.wav")

plt.plot(amplitudes)
plt.ylabel('some numbers')
plt.show()