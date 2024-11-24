#pragma once
#include "Object.h"


template<typename T> 
void print(const std::vector<T> &vec) {
	cout << "======================================" << endl;
	for (auto e : vec)cout << e << endl;
	cout << "======================================" << endl;
}