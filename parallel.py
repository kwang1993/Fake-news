from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(processes=4) 
    res = p.map(f, [1, 2, 3, 4]) 
    print res
