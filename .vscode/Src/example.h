// example.h
#ifndef EXAMPLE_H
#define EXAMPLE_H

extern "C" {
    __declspec(dllexport) int add(int a, int b);
    __declspec(dllexport) int subtract(int a, int b);
}

#endif // EXAMPLE_H
