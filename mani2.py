#include <stdio.h>
 
int main()
{
   int mani;
   
   printf("\mani");
   scanf("%d", &mani);
 
   mani%2 == 0 ? printf("Even\mani") : printf("Odd\mani");
     
   return 0;
}
