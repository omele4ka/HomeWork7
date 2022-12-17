from datetime import datetime as dt
path = 'log.txt'

def str_logger(sm_str, res):
    log = f'{dt.now()} | {sm_str} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)



