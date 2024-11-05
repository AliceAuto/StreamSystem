#include <windows.h>
#include <iostream>
#include <string>
#include "dllmain.h"  // 包含 DLL 的头文件

using namespace std;

#define DLL_FOLDER_PATH "Dlls/dllOuts"  // DLL文件所在的文件夹路径
#define DLL_NAME "Dll1.dll"  // DLL 文件名

typedef int (*AddFunction)(int, int);  // 定义函数指针类型

int main() {
    // 将 DLL 文件夹路径添加到系统路径
    SetDllDirectory(TEXT(DLL_FOLDER_PATH));  // 指定DLL搜索路径

    // 加载 DLL，仅使用文件名
    HMODULE hDll = LoadLibrary(TEXT(DLL_NAME));
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

    // 重置DLL路径
    SetDllDirectory(NULL);

    return 0;
}
