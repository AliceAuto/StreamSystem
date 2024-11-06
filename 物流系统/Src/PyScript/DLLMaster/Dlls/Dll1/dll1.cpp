// Dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"  // 如果你的项目中使用了预编译头，否则可以删除这一行。
#include "dll1.h" // 包含头文件
#include <cstdio> // 用于 printf

// DLL 中的函数实现
extern "C" __declspec(dllexport) int sub(int a, int b) {
    // 返回两个整数的和
    return a - b;
}
