#include<iostream>
#include<queue>
#include<map>
using namespace std;
int main() {
  int K, N;
  cin >> K >> N;
  long long  P[100];
  priority_queue<long long, vector<long long>, greater<long long>>pq;
  for (int k = 0; k < K; k++) {
    cin >> P[k];
    pq.push(P[k]);
	}
  map<long long, bool>visited;
  long long mv = P[K-1];
	long long ans;
	for (int n = N;n>0;n--){
		ans = pq.top(); pq.pop();
		for (int k = 0; k < K; k++) {
			long long c = ans * P[k];
			if (pq.size() >= N && c >= mv)
				continue;
			if (!visited[c]) {
				visited[c] = true;
				pq.push(c);
				mv = max(mv, c);
			}
		}
	}
	cout << ans;
}
