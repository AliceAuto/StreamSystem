// main.cpp
#include <iostream>
#include "example.h" // 包含头文件

int main() {
    int sum = add(5, 3);
    int diff = subtract(5, 3);
    std::cout << "Sum: " << sum << ", Difference: " << diff << std::endl;
    return 0;
}
