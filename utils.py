# utils.py

import torch
import torchaudio
import IPython
import os

class TTSUtils:
    def __init__(self, bundle):
        self.device = "cuda"
        self.bundle = bundle

        self.processor = bundle.get_text_processor()
        self.tacotron2 = bundle.get_tacotron2().to(self.device)
        self.vocoder = bundle.get_vocoder().to(self.device)

    def generate_audio(self, text):
        with torch.inference_mode():
            processed, lengths = self.processor(text)
            processed = processed.to(self.device)
            lengths = lengths.to(self.device)
            spec, spec_lengths, _ = self.tacotron2.infer(processed, lengths)
            waveforms, lengths = self.vocoder(spec, spec_lengths)

        return waveforms, spec, self.vocoder.sample_rate


import soundfile as sf

def save_audio(waveforms, sample_rate, file_path):
    waveforms = waveforms.cpu().detach().numpy()
    sf.write(file_path, waveforms[0], sample_rate)




def plot(waveforms, spec, sample_rate):
    waveforms = waveforms.cpu().detach()
    return IPython.display.Audio(waveforms[0:1], rate=sample_rate)
