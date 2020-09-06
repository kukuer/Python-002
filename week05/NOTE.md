# Django学习笔记

**官方文档**

 [ttps://docs.djangoproject.com/zh-hans/3.0/](https://docs.djangoproject.com/zh-hans/3.0/) 

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

   python manage.py help	#查看工具具体功能

   python manage.py startapp index 	#创建应用程序

   ```python
   index
   	migrations	#数据库迁移文件夹
       models.py	#模型
       apps.py		#当前app配置文件
       admin.py	#管理后台
       tests.py	#自动化测试
       views.py	#视图
   ```

   