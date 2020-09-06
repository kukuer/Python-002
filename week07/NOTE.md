# 面向对象编程

## 继承

1. 新式类和经典类的区别

   当前类或者父类继承了object类，那么该类就是新式类，否则便是经典类

   python3.x中不管有没有显式的继承object类，所有的父类都是继承自object。

2. object和type的关系
   - object和type都属于type类（class 'type'）
   - type类由type元类自身创建。object类是由元类type创建的
   - object父类为空，没有继承任何类
   - type父类为object类（class 'object'）

3. 类的继承

   - 单一继承
   - 多重继承
   - 菱形继承（钻石继承）
   - 继承机制MRO
   - MRO的C3算法

   经典类继承方式：深度优先， 类名.mro()方法显示继承顺序

   继承顺序：C3算法（类似有向无环路图）

## 设计模式

指导原则：solid设计原则

solid设计原则：

- 单一责任原则（The Single Responsibility Principle）
- 开放封闭原则（The Open Closed Principle）
- 里式替换原则（The Liskov Substitution Principle）
- 依赖倒置原则（The Dependency Inversion Principle）
- 接口分离原则（The Interface Segregation Principle）