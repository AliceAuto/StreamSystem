#ifndef USER_H
#define USER_H

#include <string>
#include <vector>

struct User {
    int id;
    std::string name;
    std::vector<int> purchaseHistory; // ������ʷ��ƷID
};

#endif // USER_H
#pragma once
