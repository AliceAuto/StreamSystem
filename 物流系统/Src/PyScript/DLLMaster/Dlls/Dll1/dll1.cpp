// Dllmain.cpp : ���� DLL Ӧ�ó������ڵ㡣
#include "pch.h"  // ��������Ŀ��ʹ����Ԥ����ͷ���������ɾ����һ�С�
#include "dll1.h" // ����ͷ�ļ�
#include <cstdio> // ���� printf

// DLL �еĺ���ʵ��
extern "C" __declspec(dllexport) int sub(int a, int b) {
    // �������������ĺ�
    return a - b;
}
