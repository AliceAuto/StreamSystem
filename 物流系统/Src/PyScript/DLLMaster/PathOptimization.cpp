#include "PathOptimization.h"
#include <limits>
#include <iostream>
#include <vector>
#include <vector>
#include <limits>

int minDistance(const std::vector<int>& dist, const std::vector<bool>& sptSet) {
    int min = std::numeric_limits<int>::max(); // 初始化最小距离为最大值
    int min_index = -1; // 初始化最小索引

    for (int v = 0; v < dist.size(); v++) {
        // 如果当前距离更小并且没有被处理过
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v]; // 更新最小距离
            min_index = v; // 更新最小索引
        }
    }
    return min_index; // 返回最小距离的索引
}

void PathOptimization::optimizePath(const std::vector<std::vector<int>>& graph, int source) {
    int V = graph.size();
    std::vector<int> dist(V, std::numeric_limits<int>::max());
    std::vector<bool> sptSet(V, false);

    dist[source] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet); // 假设有实现该函数的逻辑
        sptSet[u] = true;

        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != std::numeric_limits<int>::max() && 
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // 输出结果
    for (int i = 0; i < V; i++) {
        std::cout << "距离源点 " << source << " 到节点 " << i << " 的最短路径长度为: " << dist[i] << std::endl;
    }
}
