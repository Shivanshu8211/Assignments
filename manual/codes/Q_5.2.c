#include<stdio.h>
#include <stdlib.h>
int main(){
	int A = 5;
	char s1[100],s2[100];
	double X,Y,N;
	FILE* fp_1;
	FILE* fp_2;
	FILE* fp_3;
	fp_1 = fopen("X.dat","r");
	fp_2 = fopen("gau.dat","r");
	fp_3 = fopen("Y.dat","w");
	for(int i = 0; i<1000000; i++){
		X = atof(fgets(s1,sizeof(s1),fp_1));
		N = atof(fgets(s1,sizeof(s1),fp_2));
		Y = A*X + N;
		fprintf(fp_3,"%lf\n",Y);
	}
	return 0;	
	}

