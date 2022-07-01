#include<stdio.h>
#include<math.h>
int main(){
	FILE *fp_1;
	FILE*fp_2;
	int i = 0;
	double u;
        double v;
	fp_1 = fopen("uni.dat","r");
	fp_2 = fopen("N_uni.dat","w");
	while(fscanf(fp_1,"%lf",&u)!= EOF){
	i++;
	v = (-2*log(1-u))/0.4343;
	fprintf(fp_2,"%lf\n",v);
	fclose(fp_1);
	fclose(fp_2);
	}}
