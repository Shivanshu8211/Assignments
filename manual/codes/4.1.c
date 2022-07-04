#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
//uniform("uni_1.dat", 1000000);
//uniform("uni_2.dat", 1000000);
char s1[100],s2[100];
//char *s_1,*s_2;
FILE *fp_1;
FILE *fp_2;
FILE *fp_3; 
//double u_1;
//double u_2;
//double t;
fp_1 = fopen("uni_1.dat","r");
fp_2 = fopen("uni_2.dat","r");
fp_3 = fopen("Tri.dat","w");
for(int i = 0; i<1000000; i++){
	//s_1 = fgets(s1,sizeof(s1),fp_1);
	//s_2 = fgets(s2,sizeof(s2),fp_2);
	//printf("%s",s_1);
	//u_1 = atof(s_1);
	//u_2 = atof(s_2);
	//printf("%lf",u_1);
	//t = u_1 + u_2;
	fprintf(fp_3,"%lf\n",atof(fgets(s1,sizeof(s1),fp_1))+atof(fgets(s2,sizeof(s2),fp_2)));
	}
	fclose(fp_1);
	fclose(fp_2);
	fclose(fp_3);
}
 
