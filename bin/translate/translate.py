#!/bin/python3

import requests
import pyperclip
import subprocess
import asyncio
import time
from urllib.parse import quote_plus
from lxml import etree


class trans:
    def __init__(self, text) -> None:
        self.request = requests.Session()
        self.text = text
        self.url = {
            "google": "https://translate.google.com.hk/translate_a/single?client=gtx&sl=auto&tl={}&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&q={}",
            "haici": "https://apii.dict.cn/mini.php?q=",
            "youdao": "https://dict.youdao.com/jsonapi_s?doctype=json&jsonversion=4",
            "baidu": "https://fanyi.baidu.com/sug",
        }
        self.headers = {
            "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

    async def google(self):
        t = ""
        num = 0
        text = quote_plus(self.text)
        for t in self.text:
            if ord(t) > 255:
                num += 1
            else:
                num -= 1

        tl = num <= 0 and "zh-CN" or "en"
        try:
            response = self.request.get(
                self.url["google"].format(tl, text),
                headers=self.headers,
                timeout=5,
            )
            if not response or response.status_code != 200:
                return

            fanyi = response.json()

            t = fanyi[0][0] and f"google:\n{fanyi[0][0][0]}\n" or ""
        except Exception:
            pass

        return t

    async def haici(self):
        t = ""
        text = quote_plus(self.text)
        try:
            response = self.request.get(
                self.url["haici"] + text, headers=self.headers, timeout=5
            )
            if not response or response.status_code != 200:
                return

            html = etree.HTML(response.text)
            haici = html.xpath("/html/body/div[1]/text()")
            t = haici and "海词:\n" + "\n".join(haici) + "\n" or ""
        except Exception:
            pass

        return t

    async def youdao(self):
        t = ""
        youdao = []
        body = {"q": self.text, "client": "web", "keyfrom": "webdict"}
        try:
            response = self.request.post(
                self.url["youdao"],
                headers=self.headers,
                timeout=5,
                data=body,
            )
            if not response or response.status_code != 200:
                return

            fanyi = response.json()

            if "fanyi" in fanyi:
                t = "有道:\n" + fanyi["fanyi"]["tran"]
            else:
                for value in fanyi["web_trans"]["web-translation"][0]["trans"]:
                    youdao.append(self.text + " " + value["value"])
                t = youdao and "有道:\n" + "\n".join(youdao) + "\n" or ""
        except Exception:
            pass

        return t

    async def baidu(self):
        t = ""
        baidu = []
        body = {"kw": f"{self.text}"}
        try:
            response = self.request.post(
                self.url["baidu"], headers=self.headers, data=body, timeout=5
            )
            if not response or response.status_code != 200:
                return

            fanyi = response.json()
            for value in fanyi["data"]:
                baidu.append(value["k"] + " " + value["v"])
            t = baidu and "百度:\n" + "\n".join(baidu) + "\n" or ""
        except Exception:
            pass

        return t


def notify(msg, id):
    subprocess.Popen(["/bin/bash", "-c", f'notify-send -r {id} "翻译" "{msg}"'])


async def main():
    num = 0
    history = {}
    pyperclip.copy("")
    notify("开启翻译", 9527)
    while True:
        text = pyperclip.paste()
        text = text.replace("\n", "").replace("\r", "")
        try:
            if num == 30:
                del history[text]
                num = 0
        except KeyError:
            pass

        try:
            if history[text]:
                notify(history[text], 9526)
                del history[text]
        except KeyError:
            if text != "":
                notify("开始翻译 " + text, 9526)
                t = trans(text)
                results = await asyncio.gather(
                    t.google(), t.haici(), t.youdao(), t.baidu()
                )
                tmp = ""
                for i in results:
                    tmp += isinstance(i, str) and i or ""

                history[text] = tmp
                notify(history[text], 9526)
        finally:
            pyperclip.copy("")

        time.sleep(1 / 5)
        num += 1


if __name__ == "__main__":
    asyncio.run(main())
