import numpy as np
import wave

def read_wave_file(file_path):
    """
    从.wav文件中读取音频数据和采样率。

    Args:
        file_path (str): .wav文件的路径。

    Returns:
        fs (int): 音频的采样率。
        wave_data (numpy.ndarray): 音频数据。
    """
    try:
        with wave.open(file_path, 'rb') as wf:
            fs = wf.getframerate()
            wave_data = wf.readframes(-1)
            wave_data = np.frombuffer(wave_data, dtype=np.int16)
        return fs, wave_data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None
