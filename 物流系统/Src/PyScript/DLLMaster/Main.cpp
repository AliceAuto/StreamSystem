#include <iostream>
#include "DataManager.h"
#include "Recommendation.h"
#include "Analysis.h"
#include "PathOptimization.h"

int main() {
    DataManager dm;

    // ʾ���������
    User user1 = {1, "Alice", {101, 102}};
    User user2 = {2, "Bob", {101, 103}};
    User user3 = {3, "Carol", {102}};

    dm.addUser(user1);
    dm.addUser(user2);
    dm.addUser(user3);

    Product product1 = {101, "ƻ��", "���ʵĺ�ƻ��", 3.0, 50};
    Product product2 = {102, "�㽶", "��ɫ�㽶", 2.0, 30};
    Product product3 = {103, "����", "��ζ����", 4.0, 20};

    dm.addProduct(product1);
    dm.addProduct(product2);
    dm.addProduct(product3);

    Order order1 = {1, 1, {101, 102}, 5.0};
    Order order2 = {2, 2, {101, 103}, 7.0};
    Order order3 = {3, 3, {102}, 2.0};

    dm.addOrder(order1);
    dm.addOrder(order2);
    dm.addOrder(order3);

    Recommendation recommender(dm);
    recommender.recommendProducts(1); // ���û�1�����Ƽ�

    Analysis analysis;
    std::vector<Product> products = dm.getProducts();
    analysis.sortPopularProducts(products); // �������ܻ�ӭ��Ʒ

    PathOptimization pathOpt;
    // �������ڽӾ�����ͼ
    std::vector<std::vector<int>> graph = {
        {0, 10, 15},
        {10, 0, 35},
        {15, 35, 0}
    };
    pathOpt.optimizePath(graph, 0); // �Ż�·��

    return 0;
}
