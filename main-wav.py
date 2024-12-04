import numpy as np
from scipy.io.wavfile import write

# サンプリングレート
sample_rate = 48000  # 48kHz

# 周波数（440Hz = A音）
frequency = 440  

# 音の長さ（秒）
duration = 1  # 1秒

# 時間軸データ
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# 正弦波を生成
amplitude = 32767  # 16ビットPCMの最大値
wave_data = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.int16)

# WAVファイルに書き出し
write("output/440Hz_A.wav", sample_rate, wave_data)

print("WAVファイルが生成されました！")
