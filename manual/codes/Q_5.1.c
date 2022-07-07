#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

	FILE *fp;
	fp = fopen("X.dat","w");
	int num[]={-1,1};
	time_t t;
	srand((unsigned) time(&t));
	
	for (int i = 0; i<1000000; i++){
		int n = rand()%2;
		fprintf(fp,"%d\n",num[n]);
		}
		
	fclose(fp);
	return 0;
	}
