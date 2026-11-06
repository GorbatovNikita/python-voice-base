from java import jclass

class Transcription:
    def __init__(self, audio_path: str, content: str):
        self.audio_path = audio_path
        self.content = content

    def get_obj(self):
        obj = jclass(
            "ru.hck.voice.data.Transcription"
        )()

        obj.setAudioPath(self.audio_path)
        obj.setContent(self.content)

        return obj

class TranscriptionRepository:
    def __init__(self):
        self.bridge = jclass(
            "ru.hck.voice.bridge.database.TranscriptionBridge"
        )

    def insert(self, obj: Transcription) -> int:
        return self.bridge.insert(obj.get_obj())

    def update(self, obj: Transcription) -> None:
        self.bridge.update(obj.get_obj())

    def delete(self, id: int) -> None:
        self.bridge.deleteById(id)


