class VetAudioScribe:
    def __init__(self, model_size="base"):
        self.model_size = model_size
        self.model = None

    def load_local_whisper(self):
        try:
            from faster_whisper import WhisperModel
            self.model = WhisperModel(self.model_size, device="cpu", compute_type="int8")
            print(f"[INFO] Local Whisper Model ({self.model_size}) loaded.")
        except ImportError:
            print("[WARNING] faster-whisper not installed.")

    def transcribe_clinical_note(self, audio_path):
        if not self.model:
            return "Simulated note: Cow shows clinical signs of subclinical ketosis."
        segments, info = self.model.transcribe(audio_path, beam_size=5)
        text = " ".join([segment.text for segment in segments])
        return text
      
