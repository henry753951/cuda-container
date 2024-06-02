# 切換 Python 環境
```bash
$ sudo update-alternatives --config python
$ sudo update-alternatives --config python3
```

# 編輯 Python 環境 (初始化)
```bash
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 2

$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2
```
