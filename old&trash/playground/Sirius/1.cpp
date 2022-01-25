#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//unsigned int let_cnt(unsigned int x, unsigned int N){
////  if(x > N/2)x = N-x;
////  return N*x - x*x;
//}
//
//int main(){
//  char str[100001];
//  fgets(str, 100001, stdin);
  unsigned int len = strlen(str)-1;
  unsigned int x, cnt;
  for(unsigned int i=0; i<len; i++){
    if(str[i] == '\0')continue;
    cnt = let_cnt(i+1, len+1);
    for(unsigned int j=i+1; j<len; j++){
      if(str[j] == str[i]){
        cnt += let_cnt(j+1, len+1);
        str[j] = '\0';
      }
    }
    printf("%c\t%u\n", str[i], cnt);
  }
}