#pragma once
#include "Object.h"


template<typename T> 
void print(const std::vector<T> &vec) {
	std::cout << "======================================" << std::endl;
	for (auto e : vec)std::cout << e << std::endl;
	std::cout << "======================================" << std::endl;
}