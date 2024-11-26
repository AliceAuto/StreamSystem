#include "PathOptimization.h"
#include <limits>
#include <iostream>
#include <vector>
#include <vector>
#include <limits>

int minDistance(const std::vector<int>& dist, const std::vector<bool>& sptSet) {
    int min = std::numeric_limits<int>::max(); // ��ʼ����С����Ϊ���ֵ
    int min_index = -1; // ��ʼ����С����

    for (int v = 0; v < dist.size(); v++) {
        // �����ǰ�����С����û�б������
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v]; // ������С����
            min_index = v; // ������С����
        }
    }
    return min_index; // ������С���������
}

void PathOptimization::optimizePath(const std::vector<std::vector<int>>& graph, int source) {
    int V = graph.size();
    std::vector<int> dist(V, std::numeric_limits<int>::max());
    std::vector<bool> sptSet(V, false);

    dist[source] = 0;

    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet); // ������ʵ�ָú������߼�
        sptSet[u] = true;

        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != std::numeric_limits<int>::max() && 
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // ������
    for (int i = 0; i < V; i++) {
        std::cout << "����Դ�� " << source << " ���ڵ� " << i << " �����·������Ϊ: " << dist[i] << std::endl;
    }
}
