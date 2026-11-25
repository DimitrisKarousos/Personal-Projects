#include<iostream>

using namespace std;

#define N 8

class polynomial{
    int deg;
    float a[deg];
    public:
        polynomial(int A[N]){
            deg = sizeof(A) / sizeof(A[0]);
            for(int i = 0; i < deg; i++){
                a[i] = A[i];
            }
        }
        int getDeg(){
            return deg;
        }
        float polyValue(float x){
            float v = 0;
            for(int i = 0; i < deg; i++){
                v += x^(deg-i) * a[i];
            }
            return v;
        }
        float polyDerivative(float x){
            float df = 0;
            for(int i = 0; i < deg; i++){
                df += x^(deg-i-1) * (deg - i) * a[i];
            }
            return df;
        }
        ~polynomial(){
            cout << "Polynomial destroyed." << endl;
        }
};

void BisectionApprox(polynomial p, float lowerBoundary, float upperBoundary, float &EstimatedRoot, float tol){
    float a = lowerBoundary, b = upperBoundary;
    EstimatedRoot = (upperBoundary + lowerBoundary) / 2;
    float pr = tol * tol * tol + 1;
    while(pr != 0 || 2 * EstimatedRoot > tol){
        pr = p.polyValue(EstimatedRoot);
        EstimatedRoot = (b + a) / 2;
        if(pr * p.polyValue(a) < 0){
            b = EstimatedRoot;
        } 
        else if(pr * p.polyValue(b) < 0){
            a = EstimatedRoot;
        }
    }
}