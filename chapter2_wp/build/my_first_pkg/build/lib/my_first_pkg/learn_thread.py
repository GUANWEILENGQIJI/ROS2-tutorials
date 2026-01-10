import threading
import requests
"""
requests库使用示例
多线程示例
"""

class DownLoad():
    def download_f(self,url,call_back_wordcount):
        # pass
        print(f'{threading.get_ident()}开始下载{url}')
        response = requests.get(url)#reponse对象包含了url网页的所有信息
        response.encoding = 'utf-8'
        call_back_wordcount(url,response.text)#reponse.text为url网页的html源代码

    def down_load_start(self,url,call_back_wordcount):
        thread = threading.Thread(target=self.download_f,args=(url,call_back_wordcount))
        thread.start()

def wordcount(url,result):
    # pass
    print(f'{url}:{len(result)}->{result[:5]}')

def main():
    download = DownLoad()
    download.down_load_start('http://0.0.0.0:8000/novel1.txt',wordcount)
    download.down_load_start('http://0.0.0.0:8000/novel2.txt',wordcount)
    download.down_load_start('http://0.0.0.0:8000/novel3.txt',wordcount)