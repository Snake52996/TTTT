# Translate Till The Terminal

一个自动化某小破站上常见的“把某些台词反复翻译xx遍”操作的脚本. 使用[谷歌翻译(Google translate)](https://translate.google.cn)提供的翻译服务, [Googletrans](https://github.com/ssut/py-googletrans)提供的api, 相关开源许可证请参见[https://github.com/ssut/py-googletrans/blob/master/LICENSE](https://github.com/ssut/py-googletrans/blob/master/LICENSE).

## 依赖

- [Python3](https://www.python.org/downloads/)

- [Googletrans](https://github.com/ssut/py-googletrans#installation)

## 安装

- 完成各项依赖的安装(参见[依赖列表](#依赖)中的链接)

- 下载源代码: `git clone`或者直接下载, 随你喜欢
- 完成了

## 使用

直接运行`TTTT.py`. 跟着提示走.

## 关于设置(settings.json)

**建议不要修改名为default的设置: 程序的容错性并不高, 不当的修改可能造成诡异的错误.**

- `default`: 表示默认的设置是哪一项
- `settings`: 具体的设置内容
  - `name`: 设置的名称, 用于供使用者辨识
  - `translator`: 关于翻译器的设置
    - `url`: 翻译器的url. 在国内一般建议保持默认
    - `delay_milliseconds`: 由于该api并非官方的api, 不能保证随时可用且过于高频的请求可能导致请求被拒绝, 出于保护目的设置的每次请求间延时(单位为毫秒)
  - `IO`: 关于输入与输出
    - `input_file`: 关于输入文件
      - `path`: 默认的文件路径. 设为`null`则会在运行时要求提供文件路径
      - `encode`: 文件编码. 默认为`utf-8`. **注意: 此设置并没有经过测试, 并不保证正确运行**
      - `language`: 默认的输入语言. `auto`表示由翻译器自动决定语言
    - `output_file`: 关于输出文件
      - `path`: 默认的文件路径. 设为`null`则自动在输入文件路径后添加`.out`后缀作为输出文件路径
      - `encode`: 同输入文件的说明
  - `translation`: 关于翻译过程的设置
    - `steps`: 每一轮翻译的路径. 如若设定为`ja, fr, zh-cn`则在每一轮中将翻译为日语的结果翻译为法语, 再将此结果翻译为中文. 通常更长的路径将带来更无法名状的结果. 处在路径最后一位的(上例中的中文)将作为输出语言. 具体语言的简称参见[Googletrans相关文档](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages)
    - `rounds`: 总的翻译轮数. 最多不会翻译超过此数目轮. 若检测到循环, 即某次的结果之前已经出现过, 则会提前终止.

## 关于这个名字

确实, TTTT是强行拼凑出来的名字. 管它呢.