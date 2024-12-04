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

# 三角波を生成
amplitude = 32767  # 16ビットPCMの最大値
wave_data = amplitude * (2 * np.abs(2 * ((t * frequency) % 1) - 1) - 1)  # 三角波

# 16ビット整数に変換
wave_data = wave_data.astype(np.int16)

# WAVファイルに書き出し
write("output/triangle_wave_440Hz.wav", sample_rate, wave_data)

print("WAVファイル 'triangle_wave_440Hz.wav' が生成されました。")
