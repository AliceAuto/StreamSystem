#include "DataManager.h"

void DataManager::addUser(const User& user) {
    users[user.id] = user;
}

void DataManager::addProduct(const Product& product) {
    products[product.id] = product;
}

void DataManager::addOrder(const Order& order) {
    orders[order.id] = order;
}

std::vector<User> DataManager::getUsers() {
    std::vector<User> userList;
    for (auto& pair : users) {
        userList.push_back(pair.second);
    }
    return userList;
}

std::vector<Product> DataManager::getProducts() {
    std::vector<Product> productList;
    for (auto& pair : products) {
        productList.push_back(pair.second);
    }
    return productList;
}

std::vector<Order> DataManager::getOrders() {
    std::vector<Order> orderList;
    for (auto& pair : orders) {
        orderList.push_back(pair.second);
    }
    return orderList;
}
