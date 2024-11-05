#include <windows.h>
#include <iostream>
#include "dllmain.h"// 包含 DLL 的头文件

typedef int (*AddFunction)(int, int);  // 定义函数指针类型

int main() {
    // 加载 DLL




    HMODULE hDll = LoadLibrary(TEXT("dlllib/Dll1.dll"));  // 确保 DLL 文件路径正确//注意这里使用相对路径，所有的dll都会生成到dlllib
    if (hDll) {
        // 获取函数地址
        AddFunction add = (AddFunction)GetProcAddress(hDll, "add");
        if (add) {
            // 调用 DLL 函数
            int result = add(5, 3);  // 传入参数调用 add 函数
            std::cout << "The result of adding is: " << result << std::endl;  // 输出结果
        }
        else {
            std::cerr << "Could not locate the function." << std::endl;
        }

        // 卸载 DLL
        FreeLibrary(hDll);
    }
    else {
        std::cerr << "Could not load the DLL." << std::endl;
    }

    return 0;
}
