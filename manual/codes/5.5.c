#include <stdio.h>
#include <stdlib.h>
int main(){
	FILE* fp_1;
	FILE* fp_2;
	char s1[100],s2[100];
	double p = 0,x;
	double q = 0,y;
	fp_1 = fopen("X.dat","r");
	fp_2 = fopen("Y.dat","r");
	for(int i = 0; i<1000000; i++){
		x = atof(fgets(s1,sizeof(s1),fp_1));
		y = atof(fgets(s1,sizeof(s1),fp_2));
		
		if(x == 1 && y<0){
			p+=1;
			}
		if(x == -1 && y>0){
			q+=1;
			}
		}
	p = p/1000000;	// Calculating probabilty of x = -1 given that y > 0
	q = q/1000000;	// Calculating probabilty of x = 1 given that y < 0
	
	printf("probabilty of x = -1 given that y > 0 is %lf\n",p);
	printf("probabilty of x = 1 given that y < 0 is %lf\n",q);
	}
