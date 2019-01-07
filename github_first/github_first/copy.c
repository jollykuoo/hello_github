//
//  copy.c
//  github_first
//
//  Created by Jolly on 2019/1/7.
//  Copyright © 2019年 Jolly. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

void copy(){
    FILE * file;
    char* FILENAME=(char*)malloc(sizeof(char));
    char* str=(char*)malloc(sizeof(char));
    int i=0;
    printf("请输入文件名：\n");
    scanf("%s",FILENAME);
    if((file = fopen(FILENAME,"r"))==NULL){
        printf("文件不存在\n");
               exit(0);
               }
               else{
                   while(!feof(file)){
                       str[i]=fgetc(file);
                       i++;
                   }
               }
    str[i]='\0';
    printf("%s\n",str);
    free(FILENAME);
    free(str);
    fclose(file);
}
