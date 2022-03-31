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

printf("2. Enter the accual volume of tank at the top of the building : ");
    scanf("%d",&acctual_v);
    /*  as (1/30) = model height/acctual height
        as (1/30) = model weidth/acctual weidth
        as (1/30) = model length/acctual length
        ==> model volume = l*w*h
        so acctual volume =(l*30)*(w*30)*(h*30)
        ==> Model volume = acctual volume /27000
        and also we know that on converting a volume from meter square to centimeter square
        we multiplty it by 100*100*100
    */
    model_v=(acctual_v*1000000)/27000;                                                        
    printf("Volume of the model tank at the top of the building is %d centimeter square",model_v);
}
