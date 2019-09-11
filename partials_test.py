from functools import partial


def foo(a, b, c, d):
    print("a: %s" % a)
    print("b: %s" % b)
    print("c: %s" % c)
    print("d: %s" % d)


def foo1(msg,print_msg=True, **kwargs):
    # print("args: %s" % args)
    print("msg: %s " % msg)
    print("print_msg: %s" % print_msg)
    print("kwargs: %s" % kwargs)
    print(str(kwargs.get("log_name")))

# dict = {"name": 1, "last name": 2}
print(dict)
p_foo = partial(foo, 2, 3, 4)
p_foo1 = partial(foo1, log_name="nameee")
p_foo(6)
p_foo1("bla1", print=True)
p_foo1("bla2", False,  print=False, log_name="Elad")

