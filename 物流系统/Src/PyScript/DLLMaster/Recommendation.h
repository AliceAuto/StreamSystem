#pragma once
#ifndef RECOMMENDATION_H
#define RECOMMENDATION_H

#include <vector>
#include <unordered_map>
#include "DataManager.h"

class Recommendation {
public:
    Recommendation(DataManager& dataManager);
    void recommendProducts(int userId);
private:
    DataManager& dataManager;
};

#endif // RECOMMENDATION_H
