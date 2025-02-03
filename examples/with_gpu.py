"""
Note:
    On Linux you need to run this as well: apt-get install portaudio19-dev
    gpu version is sufficient only for Linux and Windows. macOS works with GPU by default.
    You can see the used execution provider by enable debug log. see with_log.py

Setup:
    pip install kokoro-onnx[gpu] sounddevice
    wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
    wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

Run:
python examples/play.py
"""

import sounddevice as sd
from kokoro_onnx import Kokoro

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
samples, sample_rate = kokoro.create(
    "Hello. This audio generated by kokoro!", voice="af_sarah", speed=1.0, lang="en-us"
)
print("Playing audio...")
sd.play(samples, sample_rate)
sd.wait()
