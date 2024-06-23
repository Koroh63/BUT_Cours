#include <stdio.h>
#include <stdlib.h>

int estPremier(unsigned long int nb){
// nb >=5 par construction
 unsigned long int i=5;
 if (nb % 2 == 0) return(0);
 if (nb % 3 == 0) return(0);
 for (i=5 ; i*i<nb ; i+=2)
	 if (nb % i == 0) return(0);
 return(1);
}

int main (int argc, char* argv[])
{
unsigned long int  n, i;

if (argc !=2 ) {
       fprintf(stderr, "usage %s N où N est un entier\n", argv[0]);
       exit(1);
      } 

if (sscanf(argv[1],"%lu",&n)!=1){
    fprintf(stderr, "L'argument doit être entier\n");
    exit(2);
    }

printf("C'est parti pour trouver les nombres premiers inférieurs à %lu\n",n);

if (n==0){
	exit(0);
}
puts("1");
if (n>=2) puts("2");
if (n>=3) puts("3");

for (i=5; i<=n ; i+=2){
	//on avance que sur les nombres impairs
    if (estPremier(i)==1) printf("%lu\n",i);
  }
exit(0);
}
