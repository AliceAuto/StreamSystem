// DllTest.cpp : 定义 DLL 应用程序的入口点。

#include "DllTest_1.h"
#include <cstdio>

extern "C" __declspec(dllexport) void DllTest_1()
{
    printf("DllTest_1::Test()\n");
}
