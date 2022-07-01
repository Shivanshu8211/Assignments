#include <stdio.h>
#include<math.h>

int main(){
    int p = 0;
    double num,sum = 0;
    double var = 0,sq_sum = 0;
    FILE*fp=fopen("gau.dat","r");
    while(fscanf(fp, "%lf", &num)!=-1){
        sum += num;
        sq_sum += (num*num);
        p+=1;
    }
    var = (sq_sum/(p)) - ((sum/p)*(sum/p));
    printf("Mean is %lf \n",sum/p);
    printf("Variance is %lf \n",var);
    fclose(fp);
    return 0;
}
// Mean is 0.500007 
// Variance is 0.083301 
