// DllTest.cpp : ���� DLL Ӧ�ó������ڵ㡣

#include "dlltest.h"
#include <cstdio>

extern "C" __declspec(dllexport) void DllTest_1()
{
    printf("DllTest_1::Test()\n");
}
