#include <stdio.h>
#include <sys/time.h>

int main(int argc, char *argv[]) {
  double a,b;
  a = atoi(argv[1]);
  b = atoi(argv[2]);

  if (a == 0) {
    printf("%g\n", b);
    return 0;
  }
  {
    while (b != 0) {
      if (a > b) {
        a = a - b;
      } else {
        b = b - a;
      }
    }
    printf("%g\n", a);
  }

  return 0;
}
