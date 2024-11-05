#include <windows.h>
#include <iostream>
#include <string>
#include "dllmain.h"  // ���� DLL ��ͷ�ļ�

using namespace std;

#define DLL_FOLDER_PATH "Dlls/dllOuts"  // DLL�ļ����ڵ��ļ���·��
#define DLL_NAME "Dll1.dll"  // DLL �ļ���

typedef int (*AddFunction)(int, int);  // ���庯��ָ������

int main() {
    // �� DLL �ļ���·����ӵ�ϵͳ·��
    SetDllDirectory(TEXT(DLL_FOLDER_PATH));  // ָ��DLL����·��

    // ���� DLL����ʹ���ļ���
    HMODULE hDll = LoadLibrary(TEXT(DLL_NAME));
    if (hDll) {
        // ��ȡ������ַ
        AddFunction add = (AddFunction)GetProcAddress(hDll, "add");
        if (add) {
            // ���� DLL ����
            int result = add(5, 3);  // ����������� add ����
            std::cout << "The result of adding is: " << result << std::endl;  // ������
        }
        else {
            std::cerr << "Could not locate the function." << std::endl;
        }

        // ж�� DLL
        FreeLibrary(hDll);
    }
    else {
        std::cerr << "Could not load the DLL." << std::endl;
    }

    // ����DLL·��
    SetDllDirectory(NULL);

    return 0;
}
