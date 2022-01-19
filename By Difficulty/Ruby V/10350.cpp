#include<iostream>
#include <cmath>
using namespace std;

int main(){
  int N;
  cin >> N;
  long long nums[20010];
  for (int n=0;n<N;n++){
    cin>>nums[n];
    nums[n+N]=nums[n];
  }
  long long dp[20010];
  dp[0]=0;
  for (int n=0;n<2*N;n++){
    dp[n+1]=dp[n]+nums[n];
  }
  long long ans=0;
  long long su = dp[N];
  for (int i=0;i<N;i++){
    for (int j=0;j<N;j++){
      if (dp[i+j+1]-dp[i]<0){
        ans += ceil((double)(dp[i]-dp[i+j+1])/su);
      }
    }
  }
  cout << ans << endl;
}
