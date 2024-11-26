#include "Recommendation.h"
#include <queue>
#include <set>
#include <iostream>

Recommendation::Recommendation(DataManager& dm) : dataManager(dm) {}

void Recommendation::recommendProducts(int userId) {
    std::vector<User> users = dataManager.getUsers();
    std::unordered_map<int, std::set<int>> userProductMap; // �û��������Ʒ

    for (const auto& user : users) {
        for (const auto& productId : user.purchaseHistory) {
            userProductMap[user.id].insert(productId);
        }
    }

    std::queue<int> queue;
    std::set<int> recommended;

    queue.push(userId);
    while (!queue.empty()) {
        int currentUser = queue.front();
        queue.pop();

        for (const auto& productId : userProductMap[currentUser]) {
            recommended.insert(productId);
        }
    }

    std::cout << "�Ƽ���Ʒ��";
    for (const auto& productId : recommended) {
        std::cout << productId << " ";
    }
    std::cout << std::endl;
}
