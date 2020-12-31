// Fibonacci Series using Recursion 
#include <stdio.h> 
int fib(int n) { 
    if (n <= 1) 
        return n; 
    return fib(n - 1) + fib(n - 2); 
} 
  
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    printf("%d\n", fib(n)); 
    return 0; 
} 
