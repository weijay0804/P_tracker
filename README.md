## P記帳

> 一個簡單的記帳軟體

### Usage
* Clone 到本地端
* 安裝相關套件
  > 如果是使用 `pipenv` 可以直接 `pipenv install`
* 設定環境變數
  > CMD
  ```cmd
  > set FLASK_APP=main.py
  ```

  > Bash 
  ```bash
  $ export FLASK_APP=main.py
  ```

* 初始化資料庫
    ``` bash
    $ flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```
* 執行程式
    ```bash
    $ flask run
    ```
* 再來就去 `127.0.0.1:5000` 就有了
