import time

import gtts
import io
import pygame

class TTS:
    # ttsImpl: gtts.gTTS
    lang: str

    def __init__(self, lang="zh-cn"):
        self.lang = lang

    def text_to_speech(self, input_text: str):
        # todo 定时删除临时的mp3文件
        demo_file = "test.mp3"
        tts = gtts.gTTS(text=input_text, lang=self.lang)
        tts.save(demo_file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(demo_file)
        pygame.mixer.music.play()

        # wait for music play done.
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
