#include<iostream>

#define N 6
#define M 8

float dotProd(float A[M], float B[M]){
    float prod = 0;
    for(int i = 0; i < M; i++){
        prod += A[i] * B[i];
    }
    return prod;
}

int sumVec(float A[M]){
    float sum = 0;
    for(int i = 0; i < M; i++){
        sum += A[i];
    }
    return sum;
}

void matProd(float A[N][M], float B[M][N], float (&prod)[N][N]){
    float row[M], col[M];
    int z = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            for(int k = 0; k < M; k++){
                row[k] = A[z][k];
                col[k] = B[k][z];
            }
            prod[i][j] = dotProd(row, col);
            z++;
        }
    }
}
