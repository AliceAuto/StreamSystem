#ifndef ORDER_H
#define ORDER_H

#include <vector>

struct Order {
    int id;
    int userId; // �û�ID
    std::vector<int> productIds; // ��ƷID�б�
    float totalAmount; // �ܽ��
};

#endif // ORDER_H
#pragma once
