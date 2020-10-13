def new_decorator(func):

    def wrap_func():
        print("Code here, before executing func")

        func()

        print("Code here, after executing func")

    return wrap_func


@new_decorator
def func_need_decorator():
    print("Hi, I am decorator")


# behind:
# func_need_decorator = new_decorator(func_need_decorator)


func_need_decorator()
