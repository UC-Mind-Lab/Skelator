#include <stdio.h>
#include <sys/time.h>


int gcd(int a, int b) {
  if (a == 0) {
    return b;
  } else { 
    while (b != 0) { 
      if (a > b) {
        a = a - b;
      } else {
        b = b - a;
      }
    }
    return a;
  }
}


int abs(int a) {
  if(a < 0) {
    a *= -1;
  }
  return a;
}


int lcm(int a, int b) {
  if(a == 0) {
    return a;
  } else if(b == 0) {
    return b;
  } else {
    return abs(a*b)/gcd(a,b);
  }
}


int main(int argc, char *argv[]) {
  int a,b;
  a = atoi(argv[1]);
  b = atoi(argv[2]);

  int answer = lcm(a,b);

  printf("%d\n", answer);

  return 0;
}
