import datetime,time


def log(d_time):
    def _log(fn):
        def wrapper(*args,**kargs):
            start = datetime.datetime.now()
            ret = fn(*args,**kargs)
            duration = (datetime.datetime.now() - start).total_seconds()
            if duration > d_time:
                print('计算超时')
            return ret
        return wrapper
    return _log

@log(1)
def add(x,y):
    time.sleep(1)
    return x+y

print(add(4,5))