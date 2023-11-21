import time
import unittest
import tts
import aiounittest


class TestAsyncTTS(unittest.IsolatedAsyncioTestCase):
    async def test_genshin_api(self):
        test_text = "测试一下看看什么效果"
        tts_impl = tts.TTS()
        voice_tmp_path = await tts_impl.genshin_voice_top_api(test_text)
        print(f"generated file: {voice_tmp_path}")

class TestTTS(unittest.TestCase):
    def setUp(self):
        self.tts_impl = tts.TTS()


    # def test_text_to_speech(self, ):
    #     tts_impl = tts.TTS()
    #     test_text = "测试一下看看什么效果"
    #     tts_impl.text_to_speech(test_text)

    async def test_genshin_api(self):
        test_text = "测试一下看看什么效果"
        tts_impl = tts.TTS()
        voice_tmp_path = await tts_impl.genshin_voice_top_api(test_text)
        print(f"generated file: {voice_tmp_path}")

if __name__ == '__main__':
    unittest.main()