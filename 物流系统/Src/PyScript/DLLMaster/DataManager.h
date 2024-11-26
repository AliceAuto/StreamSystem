#ifndef DATAMANAGER_H
#define DATAMANAGER_H

#include "User.h"
#include "Product.h"
#include "Order.h"
#include <vector>
#include <unordered_map>

class DataManager {
public:
    void addUser(const User& user);
    void addProduct(const Product& product);
    void addOrder(const Order& order);
    std::vector<User> getUsers();
    std::vector<Product> getProducts();
    std::vector<Order> getOrders();
    
private:
    std::unordered_map<int, User> users;
    std::unordered_map<int, Product> products;
    std::unordered_map<int, Order> orders;
};

#endif // DATAMANAGER_H
#pragma once
