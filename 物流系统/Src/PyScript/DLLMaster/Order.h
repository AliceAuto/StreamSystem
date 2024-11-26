#ifndef ORDER_H
#define ORDER_H

#include <vector>

struct Order {
    int id;
    int userId; // 用户ID
    std::vector<int> productIds; // 商品ID列表
    float totalAmount; // 总金额
};

#endif // ORDER_H
#pragma once
