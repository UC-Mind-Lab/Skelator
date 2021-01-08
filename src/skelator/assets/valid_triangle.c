#include <stdio.h>
  
void checkTriangle(int x1, int y1, int x2, int y2, int x3, int y3) { 
    int a = x1 * (y2 - y3) 
            + x2 * (y3 - y1) 
            + x3 * (y1 - y2); 
  
    if (a == 0)
      printf("No\n");
    else
      printf("Yes\n");
} 
  
int main(int argc, char *argv[]) {
  int x1, x2, x3, y1, y2, y3; 

  x1 = atoi(argv[1]);
  x2 = atoi(argv[2]);
  x3 = atoi(argv[3]);
  y1 = atoi(argv[4]);
  y2 = atoi(argv[5]);
  y3 = atoi(argv[6]);

  checkTriangle(x1, y1, x2, 
                y2, x3, y3); 
  return 0; 
} 
