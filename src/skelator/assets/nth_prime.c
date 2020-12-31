#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {
  int rangenumber, c = 0, num = 2, i, letest = 0;
  rangenumber = atoi(argv[1]);

  while (c != rangenumber) {
    int count = 0;
    for (i = 2; i <= sqrt (num); i++) {
      if (num % i == 0) {
        count++;
        break;
      }
    }
    if (count == 0) {
      c++;
      letest = num;
    }
    num = num + 1;
  }
  printf ("%d\n",rangenumber,letest);
  return 0;
}
