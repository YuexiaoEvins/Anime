import openai

class ChatGPT:
    def generate(self,text:str):
        pass

    def chat_with_gpt(self, messages):
        """
        使用 ChatGPT 接口生成回复消息
        :param messages: 上下文消息列表
        :return: ChatGPT 返回的回复消息
        """
        max_length = len(self.data_openai['api_key']) - 1

        try:
            openai.api_base = self.data_openai['api']

            if not self.data_openai['api_key']:
                return "请设置Api Key"
            else:
                # 判断是否所有 API key 均已达到速率限制
                if self.current_key_index > max_length:
                    self.current_key_index = 0
                    return "全部Key均已达到速率限制,请等待一分钟后再尝试"
                openai.api_key = self.data_openai['api_key'][self.current_key_index]

            # 调用 ChatGPT 接口生成回复消息
            resp = openai.ChatCompletion.create(
                model=self.data_chatgpt['model'],
                messages=messages
            )
            resp = resp['choices'][0]['message']['content']

        # 处理 OpenAIError 异常
        except openai.OpenAIError as e:
            if str(e).__contains__("Rate limit reached for default-gpt-3.5-turbo") and self.current_key_index <= max_length:
                self.current_key_index = self.current_key_index + 1
                logging.info("速率限制，尝试切换key")
                return self.chat_with_gpt(messages)
            elif str(e).__contains__(
                    "Your access was terminated due to violation of our policies") and self.current_key_index <= max_length:
                logging.info("请及时确认该Key: " + str(openai.api_key) + " 是否正常，若异常，请移除")

                # 判断是否所有 API key 均已尝试
                if self.current_key_index + 1 > max_length:
                    return str(e)
                else:
                    logging.info("访问被阻止，尝试切换Key")
                    self.current_key_index = self.current_key_index + 1
                    return self.chat_with_gpt(messages)
            else:
                logging.info('openai 接口报错: ' + str(e))
                resp = "openai 接口报错: " + str(e)

        return resp