#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>

#define N_INF 50
#define N_SUP 100
#define TIMEOUT 20
#define LG 80
#define M_MAX 10

unsigned int mystere;
// #define mystere 75

void compteArebours(unsigned int t){
  sleep(t);
  puts("temps écoulé ! Désolé ! C'est perdu !");
  kill(getppid(), SIGKILL); //on arréte le prog principal
}

void modifierNbreMystere(unsigned int t){
 // modifie le nombre mystere 2 fois à chaque tiers du chrono
 // en ajoutant ou en supprimant un nombre aléatoire borné
 unsigned int duree=t/3;
 for (unsigned int i=1; i <3 ; i++)
 {
        sleep(duree);
        kill(getppid(),SIGUSR1);

 }
}

void signal_handler(int signal){
        int n= rand()%M_MAX +1;
        if (rand()%2){
                printf("\nOwo : le nombre mystère a été augmenté de %u\n",n);
                mystere=mystere+n;
        }
        else {
                printf("\nle nombre mystère a été diminué de %u\n",n);
                mystere=mystere-n;
        }
}


int main(int argc, char* argv[]){

 unsigned int proposition=0;
 unsigned int temps=TIMEOUT;
 char ligne[LG];
 int r;
 pid_t timeFils;
 pid_t randFils;
 if (argc == 2) {
     if (sscanf(argv[1],"%u",&temps)!=1)
             temps=TIMEOUT; //temps par défaut car paramètre incorrect

 }

 //on initialise le générateur pseudo aléatoire sur le PID du process
 // qui change forcément à chaque exécution
 srand(getpid());
 // puis on choisit un nombre aléatoire dans les bornes
 mystere= rand()%(N_SUP-N_INF+1) + N_INF;


 printf("Trouvez un entier positif entre %u et %u\n",N_INF,N_SUP);
 printf("Vous avez %u secondes ! Bonne chance\n", temps);

 switch(timeFils=fork()) {

               case -1 : // Oups !!! fork n'a pas marché !
                         perror("fork"); exit(errno);

               case  0 : // Code du fils qui va s'occuper de la tempo
                         compteArebours(temps);
                         exit(0);
 }

 switch(randFils=fork()){
        case -1 : // Oups !!! fork n'a pas marché !
                         perror("fork"); exit(errno);

               case  0 : // Code du fils qui va s'occuper de la tempo
                         modifierNbreMystere(temps);
                         exit(0);
 }

signal(SIGUSR1, signal_handler);
do {    
         printf("%d",mystere);
         printf ("Quelle est votre proposition ? : ");
         fgets (ligne, LG, stdin); 
         r=sscanf(ligne,"%u",&proposition);
         if (r==1 ){
                 // on a un nouvel entier à comparer
            if (proposition > mystere)
                    puts("trop grand !");
            else {
                    if (proposition < mystere)
                            puts("trop petit !");
                    else
                            break;

                 }

           }
    } while (proposition != mystere);

 puts("Bravo ! C'est gagné !");
 kill(timeFils,SIGKILL); // On arrete le fils qui gère le chrono
 kill(randFils,SIGKILL);
 // le wait est donc inutile et inapproprié
 return 0;
}
 