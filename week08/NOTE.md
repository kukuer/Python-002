# Python高阶语法

[TOC]

## 1. 变量赋值

- 可变数据类型：**传递内存初始地址，对象的引用**
  - 列表 list
  - 字典 dict

  ```python
  # 问题3: x、y的值分别是什么
  x = [1,2,3]
  y = x
  x.append(4)
  print(x)
  print(y)
  >>> print(x)
  [1, 2, 3, 4]
  >>> print(y)
  [1, 2, 3, 4]
  
  
  # 问题4: a、b的值分别是多少
  a = [1, 2, 3]
  b = a
  a = [4, 5, 6]
  >>> a
  [4, 5, 6]
  >>> b
  [1, 2, 3]
  
  
  # 问题5: a、b的值分别是多少
  a = [1, 2, 3]
  b = a
  a[0],a[1],a[2] = 4, 5, 6
  >>> a
  [4, 5, 6]
  >>> b
  [4, 5, 6]
  ```
  
  
  
- 不可变数据类型：**传递对象本身**
  - 整型 int
  - 浮点型 float 
  - 字符串 string
  - 元组 tuple
  
  ```python
  # 问题1: a、b、c三个id是否相同
  a = 123
  b = 123
  c = a
  print(id(a))
  print(id(b))
  print(id(c))
  >>> print(id(a))
  140712956563536
  >>> print(id(b))
  140712956563536
  >>> print(id(c))
  140712956563536
  
  # 问题2: a、b、c的值分别是多少
  a = 456
  print(id(a))
  >>> print(id(a))
  2137341477808
  
  c = 789
  >>> print(id(c))
  2137341477968
  
  c = b = a
  >>> print(id(c))
  2137341477808
  >>> print(id(a))
  2137341477808
  >>> print(id(b)) 
  2137341477808
  ```
  
  

## 2. 容器序列的深浅拷贝

序列：str、list、tuple、bytes、bytesarray、memoryview(内存视图)、array.array、collections.deque

- 容器序列：list、tuple、memoryview等，可以存放不同类型的数据
- 扁平序列：str、bytes、bytearrary、array.array、memoryview等只能存放相同类型的数据。

容器序列存在深拷贝、浅拷贝问题。

- 注意：非容器序列不存在拷贝问题（int、str、tuple）

```python
import copy
copy.copy(object)   #浅拷贝只传递内存地址
copy.deepcopy(object) #深拷贝在内存中重新创建对象
```



```python
# 容器序列的拷贝问题
old_list = [ i for i in range(1, 11)]

new_list1 = old_list #对象应用
>>> new_list1 is old_list
True
new_list2 = list(old_list)  #传递对象本身
>>> new_list2 is new_list1    
False

# 切片操作
new_list3 = old_list[:]    #传递对象本身
>>> new_list3 is new_list1  
False

# 嵌套对象
old_list.append([11, 12])
>>> new_list1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
>>> new_list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> new_list3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



import copy
new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)
>>> new_list4 == new_list5  #拷贝后值相等
True
>>> new_list4 is new_list5  #不是同一对象
False
>>> old_list[10][0] = 13
>>> new_list4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
>>> new_list5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
```

## 3. 字典与扩展内置数据类型

1. **collections 官方文档：**
   https://docs.python.org/zh-cn/3.7/library/collections.html 

2. 字典与哈希  

   字典的key只能使用不可变类型。

   hash不支持可变类型

3. collections:

   常用功能：

   - 带命名的元组：

     ```python
     import collections
     
     Point = collections.nametuple('Point', ['x', 'y'])
     # 赋值
     p = Point(11, 12)
     p = Point(x=11, y=12)
     
     print(p[0], p[1])
     # 将p的值赋给x，y
     x, y = p
     print(p.x + p.y)`
     print(p)
     ```

     nametuple举例：

     计算欧氏距离

     ```python
     from collections import namedtuple
     from math import sqrt
     Point = namedtuple('Ponit', ['x','y','z'])
     
     class Vector(Point):
         def __init__(self, p1, p2, p3):
             super(Vector).__init__()
             self.p1 = p1
             self.p2 = p2
             self.p3 = p3
         
         # __sub__魔术方法，支持减法
         def __sub__(self, other):
             tmp = (self.p1 - other.p1)**2+(self.p2 - other.p2)**2+ \
             (self.p3 - other.p3)**2
             return sqrt(tmp)
     
     p1 = Vector(1, 2, 3)
     p2 = Vector(4, 5, 6)
     
     p1-p2
     ```

     

   - 计数器：

     ```python
     from collections import Counter
     
     mystring = ['a','b','c','d','d','d','d','c','c','e']
     # 取得mystring中频率最高的3个值
     cnt = Counter(mystring)
     cnt.most_common(3)
     # b在mystring中出现次数
     cnt['b']
     ```

   - 双向队列

     ```python
     from collections import deque
     
     d = deque('que')  # 实例化
     d.append('abc')  # 右侧添加数据
     d.appendleft('ccc')  # 左侧添加数据
     ```

     

## 4. 函数

- 可调用的对象
- 函数名后不携带（），传递函数对象
- 函数名后携带（），执行函数，传递返回值

```python
def func1():
    pass

>>> type(a) 
<class 'function'>
>>> type(b) 
<class 'NoneType'>
```

函数类：

```python
class func2(object):
	def __call__(self):  #魔术方法
		pass
```

### 参数：

**参数分类：**

- 必选参数
- 默认参数
- 可变参数
- 关键字参数
- 命名关键字参数

**参数是函数-高阶函数**

**lambda表达式**

可变参数：

*args：一个\*号，args传入值数据类型为序列

**kwargs:  2个*\*号，kargs传入参数为hash函数或者字典，key-value结构的数据类型。

**注**：args、kwargs非python关键字，使用args/kwargs为预定俗称，便于大家理解，也可以修改。

- 函数中使用可变长参数顺序：
  1. 序列数据在前，按照序列中数据先后顺序赋值。
  2. 字典类型在后
  3. \**kwargs会优先获取key-value赋值，赋值完成后，剩余数据传递给\*args

```python
def function(*args, **kwargs):
    print(f'args: {args}')
    print(f'kargs: {kwargs}')
    
function(123, 'abc', nanme='value')
```

### lambda表达式：

- lambda指示表达式，不是所有的函数逻辑都能封装成lambda
- lambda表达式，后面只能跟1个表达式
  - 实现简单函数一般可以使用lambda表达式替代
  - 高阶函数也可以使用lambda表达式

```python
# 简单函数
def test(x): return x + 1
# 用lambda替代
lambda: x:x + 1
```

### 高阶函数：

高阶： 参数函数、返回值是函数

常见的高阶函数：map、reduce、filter、apply

- apply在python2.3版本移除
- reduce放在functools包中
- 推导式和生成器表达式可以替代map和filter

map函数：

```python
# 平方
def square(x): return x**2

# map映射，将第2个参数值，依次传递给第一个方法对象处理
m = map(square, range(10))
next(m) # 取m的下一个值
list(m) # 取出所有值
# 用列表推导式替代
[square(x) for x in range(10)]
```

reduce函数：

```python
from functools import reduce

def add(x, y):
    return x + y

#将第2个参数中值两两相加
reduce(add, [1, 3, 5, 7, 9])
# 返回结果: 25
```

filter函数：

```python
def is_odd(n):
    return n % 2 == 1
# 根据is_odd函数，过滤参数2中返回结果为false
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

>>> list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
[1, 5, 9, 15]
```

### 偏函数：

偏函数是把方法的某个值固定下来，调用。

functools.partial：返回一个可调用的partial对象

使用方法：partial(function, *args, **kwargs)

**注意：**

- function是必选参数
- args和kwargs至少有1个

```python
# 例1
def add(x, y):
    return x + y

import functools
# 固定x取值为1
add_1 = functools.partial(add, 1)
# 给y赋值10，返回11
add_1(10)

# 例2
>>> import itertools
>>> g = itertools.count()
>>> next(g)
0
>>> next(g)
1
>>> auto_add_1 = functools.partial(next, g)
>> auto_add_1()
2
```

## 5. 变量作用域

- 变量作用域也叫命名空间

- python和其他语言有很大区别，只有在模块、类和函数中定义，才有作用域的概念。

- python动态语言赋值是一个对象，具体类型不用去关心。

- python只有当需要用到数据类型独有的特殊功能才需要初始化，比如：dict list添加元素时

  用到的方法。

python新版本中引入的Type Hint，类型提示的功能

其他高级语言对变量使用:

- 变量声明
- 定义类型（申请内存空间大小）
- 初始化（赋值，填充内存）
- 引用（通过对象名称调用对象内存数据）

### 变量作用域规则

Python作用域遵循LEGB规则：

LEGB规则：

- L-Local(function); 函数内的命名空间
- E-Enclosing function locals; 外部嵌套函数的命名空间（如：closure）
- G-Global(module); 函数定义所在模块（文件）的命名空间
- B-Builtin(Python); Python内置模块的命名空间

## 6. 闭包

### 函数返回值

返回关键字：

- return
- yield  #一个一个返回值

返回对象：

- 可调用的对象——闭包（装饰器）

### 闭包

特性：

- 函数里面定义函数
- 外部函数和内部函数不相关，尽量不耦合
- 外部函数定义模式规则，对函数进行装饰，内部函数定义运行
- 定义态，而不能呈现一种运行态。在定义的时候设置规则，而不在运行时在设置规则

```python
# 例1
# 函数是一个对象，所以可以作为某个函数的返回结果
def line_conf():
    def line(x):
        return 2*x+1
    return line       # return a function object

my_line = line_conf()
print(my_line(5))

# 例2
# 如果line()的定义中引用了外部的变量
def line_conf():
    # enclosure变量
    b = 10
    def line(x):
        '''如果line()的定义中引用了外部的变量'''
        return 2*x+b
    return line       
# 顺序问题，引用不到b=-1
b = -1
my_line = line_conf()
print(my_line(5))

# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)


# 例3
# 外部函数定义规则
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))

# 例4
# 与line绑定的是line_conf()传入的a,b

# Global变量
a=100
b=200
def line_conf(a, b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
```

**内部函数对外部函数作用域里变量的引用（非全局变量）则称内部函数为闭包**

```python
# 实现每次函数执行递增1
def counter(start=0):
   count=[start]
   def incr():
       count[0]+=1
       return count[0]
   return incr

c1=counter(10)

print(c1())
# 结果：11
print(c1())
# 结果：12
```

**nonlocal访问外部函数的局部变量**

```python
# 注意start的位置，return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        # start变量local作用域，访问外部函数变量，incr函数执行
        # 完成 start不释放
        nonlocal start
        start+=1
        return start
    return incr

# c1 c2互不影响
c1=counter2(5)
print(c1())
print(c1())

c2=counter2(50)
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())
```

**函数和对象比较有哪些不同的属性**

```python
# 函数和对象比较有哪些不同的属性
# 函数还有哪些属性
def func(): 
    pass
func_magic = dir(func)

# 常规对象有哪些属性
class ClassA():
    pass
obj = ClassA()
obj_magic = dir(obj)

# 比较函数和对象的默认属性
set(func_magic) - set(obj_magic)
```

## 7.装饰器

- 增强而不改变原有函数
- 装饰器强调函数的定义态而不是运行态
- 装饰器在模块导入的时会自动运行

装饰器语法糖展开：

```python
#装饰器的两种使用方式
@decorate
def target():
    print('do something')
    
def target():
    print('do something')
target = decorate(target)
```

target 表示函数

target() 表示函数执行

```python
# Flask 的装饰器是怎么用的？
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>hello world </h1>'

# app.add_url_rule('/', 'index')

if __name__ == '__main__':
   app.run(debug=True)

# 注册
@route('index',methods=['GET','POST'])
def static_html():
    return  render_template('index.html')

# 等效于
static_html = route('index',methods=['GET','POST'])(static_html)()


def route(rule, **options):
    def decorator(f):
        endpoint = options.pop("endpoint", None)
        # 使用类似字典的结构以'index'为key 以 method static_html  其他参数为value存储绑定关系
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator
```

```python
# 包装
def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'
```

### 被装饰函数

1. **被修饰函数带参数**

   ```python
   # 被修饰函数带参数
   def outer(func):
       def inner(a,b):
           print(f'inner: {func.__name__}')
           print(a,b)
           func(a,b)
       return inner
   
   @outer
   def foo(a,b):
       print(a+b)
       print(f'foo: {foo.__name__}')
       
       
   foo(1,2)
   foo.__name__
   ```

2. **被修饰函数带不定长参数**

   ```python
   # 被修饰函数带不定长参数
   def outer2(func):
       def inner2(*args,**kwargs):
           func(*args,**kwargs)
       return inner2
   
   @outer2
   def foo2(a,b,c):
       print(a+b+c)
       
   foo2(1,3,5)
   ```

3. **被修饰函数带返回值**

   ```python
   # 被修饰函数带返回值
   def outer3(func):
       def inner3(*args,**kwargs):
           ret = func(*args,**kwargs)
           return ret
       return inner3
   
   @outer3
   def foo3(a,b,c):
       return (a+b+c)
       
   print(foo3(1,3,5))
   ```

   ### 内置装饰器

   内置装饰器主要的标准库：functools

   **wraps**装饰器：

   ```python
   # 内置的装饰方法函数
   
   # functools.wraps
   # @wraps接受一个函数来进行装饰
   # 并加入了复制函数名称、注释文档、参数列表等等的功能
   # 在装饰器里面可以访问在装饰之前的函数的属性
   # @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
   # 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。 
   # 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。
   
   # 例1
   from time import ctime,sleep
   from functools import wraps
   def outer_arg(bar):
       def outer(func):
           # 结构不变增加wraps, 
           @wraps(func)
           def inner(*args,**kwargs):
               print("%s called at %s"%(func.__name__,ctime()))
               ret = func(*args,**kwargs)
               print(bar)
               return ret
           return inner
       return outer
   
   @outer_arg('foo_arg')
   def foo(a,b,c):
       """  __doc__  """
       return (a+b+c)
       
   print(foo.__name__)
   
   # flask 使用@wraps()的案例
   from functools import wraps
    
   def requires_auth(func):
       @wraps(func)
       def auth_method(*args, **kwargs):
           if not auth:
               authenticate()
           return func(*args, **kwargs)
       return auth_method
   
   @requires_auth
   def func_demo():
       pass
   
   # 例2
   from functools import wraps
    
   def logit(logfile='out.log'):
       def logging_decorator(func):
           @wraps(func)
           def wrapped_function(*args, **kwargs):
               log_string = func.__name__ + " was called"
               print(log_string)
               with open(logfile, 'a') as opened_file:
                   opened_file.write(log_string + '\n')
               return func(*args, **kwargs)
           return wrapped_function
       return logging_decorator
    
   @logit()
   def myfunc1():
       pass
    
   myfunc1()
   # Output: myfunc1 was called
    
   @logit(logfile='func2.log')
   def myfunc2():
       pass
    
   myfunc2()
   
   # Output: myfunc2 was called
   
   # 例3 老版本wrapt装饰器
   ##########################
   # 可以使用wrapt包替代@wraps
   # # wrapt包 https://wrapt.readthedocs.io/en/latest/quick-start.html
   #  @wrapt.decorator
   #  def wrapper(func, instance, args, kwargs):
   
   import wrapt
   
   def with_arguments(myarg1, myarg2):
       @wrapt.decorator
       def wrapper(wrapped, instance, args, kwargs):
           return wrapped(*args, **kwargs)
       return wrapper
   
   @with_arguments(1, 2)
   def function():
       pass
   ```

   **lru_cache**装饰器

   ```python
   # functools.lru_cache
   # 《fluent python》的例子
   # functools.lru_cache(maxsize=128, typed=False)有两个可选参数
   # maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
   # typed若为True，则会把不同的参数类型得到的结果分开保存
   import functools
   @functools.lru_cache()
   def fibonacci(n):
       if n < 2:
           return n
       return fibonacci(n-2) + fibonacci(n-1)
   
   if __name__=='__main__':
       import timeit
       print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))
   ```

## 8. 类装饰器

### 类装饰器：

- Python 2.6 开始添加类装饰器
- 常用内置类装饰器：classmethod、staticmethod、property
- 使用\_\_call\_\_将类模拟成可调用对象

```python
from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)
    
    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

def myfunc():
    pass

MyClass(100)(myfunc)()
# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


# 另一个示例
class Count(object):
    def __init__(self,func):
        self._func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kargs)

@Count
def example():
    print('hello')

example()
print(type(example))


# 其他常用的排序和计数相关用法
a = (1, 2, 3, 4)
a.sort()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'sort'
sorted(a)
# [1, 2, 3, 4]
# sorted 支持更多场景  多维list 字典混合list list混合字典


# 计数有没有更优雅、更Pythonic的解决方法呢？
# 答案是使用collections.Counter。
from collections import  Counter
Counter(some_data)
# 利用most_common()方法可以找出前N个出现频率最高的元素以及它们对应的次数
Counter(some_data).most_common(2)
```

### 装饰器装饰类

```python
# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()
```

## 9. 对象协议和鸭子类型

