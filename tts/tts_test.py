import time
import unittest
import tts


class TestTTS(unittest.TestCase):

    def test_text_to_speech(self,):
        tts_impl = tts.TTS()
        test_text = "测试一下看看什么效果"
        tts_impl.text_to_speech(test_text)
