// DllTest.cpp : ���� DLL Ӧ�ó������ڵ㡣

#include "DllTest_1.h"
#include <cstdio>

extern "C" __declspec(dllexport) void DllTest_1()
{
    printf("DllTest_1::Test()\n");
}
