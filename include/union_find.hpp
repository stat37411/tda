#pragma once

#include <tuple>
#include <vector>
#include <numeric> // iota

namespace tda {

// find subroutine with path compression
size_t find(
    size_t x,
    std::vector<size_t> &parent
) {
    size_t root = x;

    // first find cluster representative
    while (parent[root] != root) {
        root = parent[root];
    }

    // now do path compression
    while (parent[x] != root) {
        auto p = parent[x];
        parent[x] = root;
        x = p;
    }

    return root;
}

// merge/union by size
// return true if clusters are merged
// return false if clusters were already the same
bool merge(
    size_t x,
    size_t y,
    std::vector<size_t> &parent,
    std::vector<size_t> &size
) {
    x = find(x, parent);
    y = find(y, parent);

    if (x == y) return false;

    // swap if necessary so size[y] <= size[x]
    if (size[x] < size[y]) {
        auto tmp = y;
        y = x;
        x = tmp;
    }

    // now merge two clusters
    parent[y] = x;
    size[x] += size[y];
    return true;
}

/*
create dendrogram on n points
edges consist of tuple (source, target)
we'll assume edges are sorted in some order

output is dendrogram: data is
(source cluster, target cluster, edge index)
*/
std::vector<std::tuple<size_t, size_t, size_t>> dendrogram(
    size_t n, // number of points
    std::vector<std::tuple<size_t, size_t>> &edges
) {
    // initialize dendrogram
    std::vector<std::tuple<size_t, size_t, size_t>> d; // dendrogram
    d.reserve(n);

    std::vector<size_t> parent(n);
    std::iota(parent.begin(), parent.end(), 0);

    std::vector<size_t> size(n, 1); // all clusters start with 1 point

    size_t ei = 0;
    for (auto e : edges) {
        auto i = std::get<0>(e);
        auto j = std::get<1>(e);
        auto ip = find(i, parent);
        auto jp = find(j, parent);
        if (merge(i, j, parent, size)) {
            // merge smaller cluster to larger cluster
            if (size[ip] < size[jp]) {
                d.emplace_back(
                    std::make_tuple(ip, jp, ei)
                );
            } else {
                d.emplace_back(
                    std::make_tuple(jp, ip, ei)
                );
            }

        }
        ei++; // increment edge counter
    }

    return d;
}

} // namespace tda
