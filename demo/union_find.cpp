#include "union_find.hpp"
#include <iostream>
#include <vector>
#include <tuple>

int main() {

    std::vector<std::tuple<size_t, size_t>> edges;

    edges.emplace_back(std::make_tuple(0,1));
    edges.emplace_back(std::make_tuple(1,2));
    edges.emplace_back(std::make_tuple(2,3));
    edges.emplace_back(std::make_tuple(0,3));
    edges.emplace_back(std::make_tuple(3,4));

    auto dend = tda::dendrogram(5, edges);

    for (auto e : dend) {
        std::cout << std::get<0>(e) << ", "\
        << std::get<1>(e) << ", "\
        << std::get<2>(e) << std::endl;
    }

    return 0;
}
