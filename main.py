from app import *

if __name__ == '__main__':
    try:
        app.run('127.0.0.1', port=80)
    except Exception as e:
        print(e.__str__())
