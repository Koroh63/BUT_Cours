#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

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

switch(fork()) {
               case -1 : // Oups !!! fork n'a pas marché !
                         perror("fork"); exit(errno);

               case  0 : // Code du fils 1
                       for(i=5; i<=n/2 ; i+=2){
			 if (estPremier(i)==1) printf("%lu\n",i);
		       }

                         exit(0);
}

switch(fork()) {

               case -1 : // Oups !!! fork n'a pas marché !
                         perror("fork"); exit(errno);

               case  0 : // Code du fils 2
                       for(i=n/2+1; i<=(n/4)*3 ; i+=2){
                         if (estPremier(i)==1) printf("%lu\n",i);
                       }

                         exit(0);
}

switch(fork()) {

               case -1 : // Oups !!! fork n'a pas marché !
                         perror("fork"); exit(errno);

               case  0 : // Code du fils 3
			i=(n/4)*3+1;
                        if ( i%2 == 0) i++ ;
                        for (; i<=n ; i+=2){       
                         if (estPremier(i)==1) printf("%lu\n",i);
                         }

                         exit(0);
}


//code du pere
// attente fils
wait(NULL);
wait(NULL);
wait(NULL);
exit(0);
}
