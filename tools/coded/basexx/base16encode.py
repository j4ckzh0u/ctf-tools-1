#version 1.0
import base64
while True:
    data=input('base16encode>')
    if data=='exit()':
        exit()
    elif data=='':
        continue
    codestr = base64.b16encode(data.encode('utf-8'))
    print(str(codestr,'utf-8'))