#include "Analysis.h"
#include <algorithm>

static bool compare(const Product& a, const Product& b) {
    return a.stock < b.stock; // ����ʹ�ÿ������ܻ�ӭ�̶�
}

void Analysis::sortPopularProducts(std::vector<Product>& products) {
    std::sort(products.begin(), products.end(), compare);
}
