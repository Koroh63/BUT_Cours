#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <sys/shm.h>
#include <sys/stat.h>

#define N_INF 50
#define N_SUP 100
#define TIMEOUT 20
#define LG 80
#define M_MAX 10

// unsigned int mystere;
// #define mystere 75

void compteArebours(unsigned int t,int segment_id){
        sleep(t);
        puts("temps écoulé ! Désolé ! C'est perdu !");
        shmctl(segment_id,IPC_RMID,0);
        kill(getppid(), SIGKILL); //on arréte le prog principal
}

void modifierNbreMystere(unsigned int t,unsigned int* shared_memory){
        // modifie le nombre mystere 2 fois à chaque tiers du chrono
        // en ajoutant ou en supprimant un nombre aléatoire borné
        unsigned int duree=t/3,n;
        for (unsigned int i=1; i <3 ; i++)
        {
                n= rand()%M_MAX +1;
                sleep(duree);
                if (rand()%2){
                        printf("\nle nombre mystère a été augmenté de %u\n",n);
                        *shared_memory=*shared_memory+n;
                }
                else {
                        printf("\nle nombre mystère a été diminué de %u\n",n);
                        *shared_memory=*shared_memory-n;
                }
        }
}




int main(int argc, char* argv[]){

        int segment_id;
        unsigned int* shared_memory ;
        struct shmid_ds shmbuffer;
        int segment_size;
        const int shared_segment_size = sizeof(unsigned int);
        segment_id = shmget(IPC_PRIVATE, shared_segment_size, IPC_CREAT | IPC_EXCL | S_IRUSR | S_IWUSR);
        if (segment_id == -1) {
                perror("shmget");
                exit(EXIT_FAILURE);
        }
    
        // Attachement du segment de mémoire partagée
        shared_memory = (unsigned int*) shmat(segment_id, 0, 0);
        if (shared_memory == (void*) -1) {
                perror("shmat");
                exit(EXIT_FAILURE);
        }        
        shmctl (segment_id, IPC_STAT, &shmbuffer);
        segment_size = shmbuffer.shm_segsz;



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
        *shared_memory = rand() % (N_SUP - N_INF + 1) + N_INF;

        printf("Trouvez un entier positif entre %u et %u\n",N_INF,N_SUP);
        printf("Vous avez %u secondes ! Bonne chance\n", temps);

        switch(timeFils=fork()) {

                case -1 : // Oups !!! fork n'a pas marché !
                                perror("fork"); exit(errno);

                case  0 : // Code du fils qui va s'occuper de la tempo
                                compteArebours(temps,segment_id);
                                exit(0);
        }

        switch(randFils=fork()){
                case -1 : // Oups !!! fork n'a pas marché !
                                perror("fork"); exit(errno);

                case  0 : // Code du fils qui va s'occuper de la tempo
                                modifierNbreMystere(temps,shared_memory);
                                exit(0);
        }

        do {    
                printf("%d",*shared_memory);
                printf ("Quelle est votre proposition ? : ");
                fgets (ligne, LG, stdin); 
                r=sscanf(ligne,"%u",&proposition);
                if (r==1 ){
                        // on a un nouvel entier à comparer
                if (proposition > *shared_memory)
                        puts("trop grand !");
                else {
                        if (proposition < *shared_memory)
                                puts("trop petit !");
                        else
                                break;

                        }

                }
        } while (proposition != *shared_memory);

        puts("Bravo ! C'est gagné !");
        kill(timeFils,SIGKILL); // On arrete le fils qui gère le chrono
        kill(randFils,SIGKILL);
        shmctl(segment_id,IPC_RMID,0);
        
        // le wait est donc inutile et inapproprié
        return 0;
}
 