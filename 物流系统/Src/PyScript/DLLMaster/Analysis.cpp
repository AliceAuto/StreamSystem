#include "Analysis.h"
#include <algorithm>

static bool compare(const Product& a, const Product& b) {
    return a.stock < b.stock; // 假设使用库存代替受欢迎程度
}

void Analysis::sortPopularProducts(std::vector<Product>& products) {
    std::sort(products.begin(), products.end(), compare);
}
