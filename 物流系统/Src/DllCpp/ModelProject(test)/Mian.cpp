#include <windows.h>
#include <iostream>
#include "DllModel_4/dlltest.h"
typedef void (*DllTestFunc)();  // ���庯��ָ������

int main() {
    // ���� DLL
    HMODULE hDll = LoadLibrary(TEXT("DllCpp.dll"));
    if (hDll) {
        // ��ȡ������ַ
        DllTestFunc dllTest = (DllTestFunc)GetProcAddress(hDll, "DllTest_1");
        if (dllTest) {
            // ���� DLL ����
            dllTest();  // ���� DllTest_1 ����
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
