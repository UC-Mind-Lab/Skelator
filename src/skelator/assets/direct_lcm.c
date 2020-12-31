#include<stdio.h>

int main(int argc, char *argv[]) {
   int a, b, max, step, lcm;

   a = atoi(argv[1]);
   b = atoi(argv[2]);
   lcm = 0;

   if(a == 0) {
     printf("%d\n", a);
     return 0;
   }

   if(b == 0) {
     printf("%d\n", b);
     return 0;
   }

   if(a > b)
      max = step = a;
   else
      max = step = b;

   while(1) {
      if(max%a == 0 && max%b == 0) {
         lcm = max;
         break;    
      }

      max += step;

      if(max < 0) {
        printf("Error: An overflow has occurred.\n", lcm);
        return 0;
      }
   }

   printf("%d\n", lcm);
   return 0;
}
