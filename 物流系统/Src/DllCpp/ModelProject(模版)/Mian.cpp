#include <windows.h>
#include <iostream>
#include "dllmain.h"// ���� DLL ��ͷ�ļ�

typedef int (*AddFunction)(int, int);  // ���庯��ָ������

int main() {
    // ���� DLL




    HMODULE hDll = LoadLibrary(TEXT("dlllib/Dll1.dll"));  // ȷ�� DLL �ļ�·����ȷ//ע������ʹ�����·�������е�dll�������ɵ�dlllib
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

    return 0;
}
