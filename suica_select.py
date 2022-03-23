import socket
import time
import binascii
import nfc

gakuban_list = []

def connected(tag):
  # タグのIDなどを出力する
  idm, pmm = tag.polling(0xFE00)
  tag.idm, tag.pmm, tag.sys = idm, pmm, 0xFE00
  print('\n----------\n')
  if isinstance(tag, nfc.tag.tt3.Type3Tag):
    try:
      sc = nfc.tag.tt3.ServiceCode(106,11)
      bc = nfc.tag.tt3.BlockCode(0,service=0)
      data = tag.read_without_encryption([sc],[bc])
      sid = data[2:9]
      hantei = False
      for n in gakuban_list:
        if n == sid:
          hantei = True
      if hantei == False:
        """s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.99', 1235))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.send(sid)"""
        gakuban_list.append(sid)
        time.sleep(0.1)
        print('学籍番号 : ' + sid.decode())
        print('\n-----------\n')
        return 0
      else:
        print('Notice : This ID card is already readed!')
        return 1
    except Exception as e:
      print("except : " + str(e))
  else:
    print("error: tag isn't Type3Tag")

def start(clf):
  # タッチ時のハンドラを設定して待機する
    print('\nReady --- Touch ID Card!')
   
    
    if clf.connect(rdwr={'on-connect': connected})==1:
        return 1
    else:
        return 0

