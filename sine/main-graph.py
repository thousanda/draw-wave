import numpy as np
import matplotlib.pyplot as plt

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
wave_data = amplitude * np.sin(2 * np.pi * frequency * t)

# グラフのプロット
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], wave_data[:1000])  # 最初の1000サンプルだけ描画
plt.title("440Hz Sine Wave (A4 Note)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()

# PNG画像として保存
output_path = "output/440Hz_sine_wave.png"
plt.savefig(output_path)
plt.close()

print(f"Waveform saved as: {output_path}")
