# Django学习笔记

**官方文档**

 [https://docs.djangoproject.com/zh-hans/3.0/](https://docs.djangoproject.com/zh-hans/3.0/) 

1. 创建django项目：django-admin startproject  <project_name>

2. 目录结构：

   ```python
   MyDjango:
       manage.py   #命令行工具，管理django项目
       MyDjango
       	__init__.py
           setting.py 		#项目配置文件
           urls.py			
           wsgi.py
   ```

3. 创建Django应用程序

   - python manage.py help	#查看工具具体功能

   - python manage.py startapp index 	#创建应用程序

   ```python
   index
   	migrations	#数据库迁移文件夹
       models.py	#模型
       apps.py		#当前app配置文件
       admin.py	#管理后台
       tests.py	#自动化测试
       views.py	#视图
   ```

4. 启动Django项目

    python manage.py runnserver	#默认8000端口，修改IP：port

5. seetting.py配置文件

6. URLconf： url调度器
   1. Django处理请求流程：
      1. Django接收到请求，每个请求对应一个HttpRequest对象，HttpRequest对象拥有urlconf属性

         它的值将被setting.py中的ROOT_URLCONF设代替

      2. Django加载URLconf模块，并寻找可用的urlpatterns，Django依次匹配每个URL配置，匹配到

         第一个模式停止。

      3. 一旦匹配成功，Django导入匹配到的视图，视图获取到如下参数：

         - 1个HttpRequest实例
         - 一个或者多个参数

      4. 如果URL没有匹配到，或者匹配过程中触发异常，Django将调用错误处理视图和自定义的处理。

   2. URL支持变量

      URL变量类型：

      - str   #字符串
      - int   #整型
      - slug  #备注
      - uuid   #唯一ID
      - path   #路径，可以可以

      ```python
      # 如果是整型，赋值给param这个变量，将变量传递到views.param。
      # 如果类型不匹配，django返回404
      path('<int:year>', views.year)
      path('<int:year>/<str:name>', views.name)
      
      # views.py
      def year(request, param)
      def name(request, **kwargs)  #接收不定长参数
      	return HttpResponse(kwargs['name'])
      ```

   3. URL支持正则表达式

      ```python
      from django.urls import re_path
      # ?P 正则标识是关键字
      # <>内是变量名
      # 变量后跟正则表达式
      re_path('(?P<year>[0-9]{4}).html', views.re_year, name='urlyear')
      
      # views.py
      def re_year(request, year):
      	return render(request, 'yeartemplate.html')
      	
      # Templates文件夹中yeartemplate.html
      <a href="{% url'urlyear' 2020 %}">2020 booklist</a>
      ```

   4. 自定义规则

      ```python
      from django.urls import path, register_converter
      from . import converters
      
      # converters是自定义模块, Intconverter是自定义类
      register_converter(converters.IntConverter, 'myrule')
      
      path('<myrule:year>', views.year)
      
      # converters.py
      # regex, to_python, to_url属性是必须实现的
      class IntConverter：
      	regex = '[0-9]+'
      	
      	# 接收到url转换成python类型
      	def to_python(self, value):
      		return Int(value)
      		
      	# 将python类型转换为url
      	def to_url(self, value):
      		return str(value) 
      ```

7. 使用ORM创建数据库表

   - 每个model都是一个python类， 这些类都继承父类django.db.models.Model
   - model类的每个属性都相当与数据库表的字段
   - Django提供了自动生成访问数据库的API

   ```python
   from django.db import models
   
   class Person(models.Model):
       id = models.integerField(primary_key=True)  #primary_key主键
       name = models.CharField(max_length=30)
   ```

   ```sql
   CREAT TABLE index_person(
   	"id" serial NOT PRIMARY KEY,
       "name" varchar(30) NOT NULL
   );
   ```

   自动生成表结构命令：

   python manage.py makemigrations	#在migration文件夹下生产过程文件

   python manage.py migrate	#在数据库中生成表

   

  