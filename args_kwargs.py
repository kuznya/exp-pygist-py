l = (1,2,3,4,)

def boo(*args, **kwargs):
    print(args)
    print(kwargs)
    print('-'*30)

boo(1,2,3,4)
boo(1,2,3,4, link_last=True)

boo(*l, link_last=True)

print('-' * 50)


def boo1(*args, link_last=False):
    print(args)
    print('link_last:', link_last)
    print('-'*30)

boo1(1,2,3,4)
boo1(1,2,3,4, link_last=True)
boo1(*l, link_last=True)
