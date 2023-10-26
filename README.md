Done
1. B站弹幕直播库： https://github.com/xfgryujk/blivedm


TODO 
- TTS 库调研： TODO
- live2d 的python库： todo
- live2d 直播工具： https://www.live2d.com/en/
- live2d 的制片人模型：https://www.live2d.com/en/learn/sample/
  - 看看是否有必要通过stable diffusion 或者 midjourney弄个模型，然后自己建模

Note:
项目模块说明：
  - Manager: 所有模块的聚合，实现某个handler，作为参数传入给bili_live的类里面
  - Live2d: live2d的相关的模块
  - blivedm: 直播间弹幕抓取代码，把回调函数传入内部
  - tts: 文字转音频的代码模块，要支持多个tts模型
  - llm: 使用langchain整合多个llm模型，作为tts模块的输入源

其他:
    本人习惯性使用OOP的编程思想，见谅。