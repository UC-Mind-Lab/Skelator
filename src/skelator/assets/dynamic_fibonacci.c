#include <stdio.h> 
  
int fib(int n) {
    int f[n + 1]; 
    int i; 
  
    f[0] = 0; 
    f[1] = 1; 
  
    for (i = 2; i <= n; i++) { 
        f[i] = f[i - 1] + f[i - 2]; 
    } 
  
    return f[n]; 
} 
  
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    printf("%d\n", fib(n)); 
    return 0; 
} 
