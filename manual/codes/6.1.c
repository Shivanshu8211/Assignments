#include<stdio.h>
#include<stdlib.h>
int main(){    
    int para;
    printf("Enter value of k ");
    scanf("%d",&para); 
    int len = 1000000;

    FILE*fp=fopen("gau_V.dat","w");

    for(int i=0;i<len;i++){
        float l=0;
        for(int j=0;j<para;j++){
                float m=0;
                for(int k=0;k<12;k++){
                    m+=(double)rand()/RAND_MAX;
        }
            l+=(m-6)*(m-6);
        }
        fprintf(fp,"%lf\n",l);

    }
    fclose(fp);
    	}
