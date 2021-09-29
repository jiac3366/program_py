# 用在哪里

# 注册
@route('index', methods=['GET', 'POST'])
def static_html():
    return render_templete('index.html')


# 等效于
static_html = route('index', methods=['GET', 'POST'])(static_html)


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f

    return decorator

# def funA(fn):
#     # 定义一个嵌套函数
#     def say(arc):
#         print("Python教程:", arc)
#
#     return say
#
#
# @funA
# def funB(arc):
#     print("funB():", arc)
#
#
# funB("http://c.biancheng.net/python")


# def funA(fn):
#     # 定义一个嵌套函数
#     def say(arc):
#         print("Python教程:", arc)
#     return say
#
#
# def funB(arc):
#     print("funB():", arc)

#
# funB = funA(funB)
# funB("http://c.biancheng.net/python")