#include <windows.h>
#include <iostream>
#include "DllTest_1.h"  // 包含 DLL 的头文件

typedef void (*DllTestFunc)();  // 定义函数指针类型

int main() {
    // 加载 DLL
    HMODULE hDll = LoadLibrary(TEXT("DllTest.dll"));
    if (hDll) {
        // 获取函数地址
        DllTestFunc dllTest = (DllTestFunc)GetProcAddress(hDll, "DllTest_1");
        if (dllTest) {
            // 调用 DLL 函数
            dllTest();  // 调用 DllTest_1 函数
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
