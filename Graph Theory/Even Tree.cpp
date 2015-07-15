#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
using namespace std;

struct Node
{
    Node() : pinx(0), nodeCnt(0){};
    int pinx;
    unordered_set<int> c;
    int nodeCnt;
};

void countNode(vector<Node> &in, int rinx)
{
    if (in[rinx].c.empty())
    {
        in[rinx].nodeCnt = 1;
        return;
    }

    for (auto &i : in[rinx].c)
    {
        countNode(in, i);
        in[rinx].nodeCnt += in[i].nodeCnt;
    }
    in[rinx].nodeCnt += 1;
}

int cut(vector<Node> &in, int rinx, int rr)
{
    int cnt = 0;
    vector<int> removed;
    for (auto i : in[rinx].c)
    {
        if (in[i].nodeCnt % 2 == 0) 
        {
            cnt++;
            in[rinx].nodeCnt -= in[i].nodeCnt;
            removed.push_back(i);
            cnt += cut(in, i, rr);
        }
        else
            cnt += cut(in, i, rr);
    }
    for (auto i : removed)
    {
        in[rinx].c.erase(i);
    }

    if (cnt > 0)
    {
        cnt += cut(in, rinx, rr);
    }
    return cnt;
}

int main() {
    int n, m; cin >> n >> m;
    vector<Node> nodes(n);
    
    //    Build tree
    unordered_set<int> hs;
    for (int i = 1; i <= n; i++)
        hs.insert(i);

    while (m--)
    {
        int a, b; cin >> a >> b;
        if (hs.find(a) != hs.end())
            hs.erase(a);
        nodes[b - 1].c.insert(a - 1);
        nodes[a - 1].pinx = b - 1;
    }
    int rinx = *hs.begin() - 1;

    //    Count
    countNode(nodes, rinx);
    int ret = cut(nodes, rinx, rinx);
    cout << ret << endl;
    return 0;
}