import time

def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('|' * int(done * 50), done * 100),end='')
n = 0
def test():
    global n
    if(n == 100):
        n = 0
    progress_bar(n/100)
    time.sleep(0.05)
    n += 1


while 1:
    test()  