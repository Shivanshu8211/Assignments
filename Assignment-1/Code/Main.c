#include<stdio.h>
int main(){
    int acctual_h;  // acctual height
    int model_h;    // Model height
    int acctual_v;  // Volume of the tank at the top of the acctual building
    int model_v;    // Volume of the tank at the top of the model building
    printf("1. Enter height of model : ");
    scanf("%d",&model_h);
    acctual_h=model_h*30;   // as (1/30) = model height/acctual height  ==>  acctual height= model height x 30
    printf("Heieght of the acctual building is %d centimeter\n",acctual_h);

