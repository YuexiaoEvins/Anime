import time

import gtts
import io
import pygame

class TTS:
    # ttsImpl: gtts.gTTS
    lang: str

    # todo configure me
    generated_mp3_file_path: str

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

        # todo 希望通过ipc的方式，跟live2d的进程通信，让其进行人物的动作变更
        # todo 调研：https://www.2bboy.com/archives/147.html