#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int estPremier(unsigned long int nb){
// nb >=5 par construction
 unsigned long int i=5;
 if (nb % 2 == 0) return(0);
 if (nb % 3 == 0) return(0);
 for (i=5 ; i*i<nb ; i+=2)
	 if (nb % i == 0) return(0);
 return(1);
}

void * parcoursNbre (void * data){
unsigned long int i;
unsigned long int * tab = (unsigned long int *) data;
for (i= tab[0]; i<=tab[1] ; i+=2){ 
        //on avance que sur les nombres impairs 
    if (estPremier(i)==1) printf("%lu\n",i); 
  } 
return ((void*)0);
}

int main (int argc, char* argv[])
{
unsigned long int n;	
pthread_t t1,t2,t3 ;
unsigned long int borne1[2], borne2[2],borne3[2];

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

borne1[0]=5; borne1[1]=n/2;

if(pthread_create(&t1,NULL,parcoursNbre,borne1)){
		fprintf(stderr,"pb création threads\n");
		exit(3);
		}

borne2[0]=(n/2)+1 ; borne2[1]=(n/4)*3;		
if(pthread_create(&t2,NULL,parcoursNbre,borne2)){
                fprintf(stderr,"pb création threads\n");
                exit(3);
                }

borne3[0]=((n/4)*3)+1; borne3[1]=n;
if ( borne3[0] % 2 == 0) borne3[0]=borne3[0] + 1;

if(pthread_create(&t3,NULL,parcoursNbre,borne3)){
                fprintf(stderr,"pb création threads\n");
                exit(3);
                }



if(pthread_join(t1,NULL)){
	        fprintf(stderr,"pb attente threads\n");
                exit(3);
                }

if(pthread_join(t2,NULL)){
                fprintf(stderr,"pb attente threads\n");
                exit(3);
                }
if(pthread_join(t3,NULL)){
                fprintf(stderr,"pb attente threads\n");
                exit(3);
                }



exit(0);
}
