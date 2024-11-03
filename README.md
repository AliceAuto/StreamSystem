# 物流系统
 物流系统
# 项目入口
![alt text](image-2.png)
**后端开发项目文件**
- 物流系统\Src\CppDll\CppDll.sln
**前端开发项目文件**
- 物流系统\Src\PyScript\PyScript.sln
# 推荐开发插件 Fitten Code
![alt text](image-1.png)
# 创建新项目
- **快捷方式进入的是这个项目**
![alt text](image.png)
- **其他几个都是我提前配置好的，直接点击里面的sin就可以使用**
- ***如果还不够用，可以复制DllTest_1文件夹到当前目录进行开发***![alt text](image-3.png)
# 创建项目启动的快捷方式
![alt text](image-4.png)
- **创建的快捷方式统一放置到“后端开发入口”**
![alt text](image-5.png)
- **点击就可快速进入项目**
- ![alt text](image-6.png)
  
# DLL调试与生成
- 使用main调用dll的函数，可以进行调试
- 项目默认生成的exe,如果要生成dll要修改以下
  ![alt text](image-7.png)
   - 右键项目->属性->配置->常规->配置类型->动态链接库(.dll)![alt text](image-8.png)
   - 调用生成的dll，需要将配置改回exe
 - 调用调试
   - 需要一个头文件
   - ![alt text](image-11.png)
   - 一个cpp
   - ![alt text](image-10.png)
   - 一个main.cpp
   - ![alt text](image-9.png)
   - 然后记得改回生成exe的配置,编译运行后就可以运行
![alt text](image-12.png)