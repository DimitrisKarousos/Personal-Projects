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

void RegulaFalsi(polynomial p, float lowerBoundary, float upperBoundary, float tol, float &EstimatedRoot){
    float a = lowerBoundary, b = upperBoundary;
    if(b * a < 0){
        while(p.polyValue(EstimatedRoot) > tol){
            EstimatedRoot = a * p.polyValue(b) - b * p.polyValue(a) / (p.polyValue(b) - p.polyValue(a));
            if(p.polyValue(EstimatedRoot) * p.polyValue(b) < 0){
                a = EstimatedRoot;
            }
            else if(p.polyValue(EstimatedRoot) * p.polyValue(a) < 0){
                b = EstimatedRoot;
            }
        }
    }
    else{
        cout << "Please make sure a root is contained within the boundaries." << endl;
    }
}