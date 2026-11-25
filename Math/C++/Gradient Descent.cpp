#include <iostream>

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

float GradientDescent(polynomial p[N], float estimatedMin, float tol, float lr){
    float min = estimatedMin, nextMin = 0, currentValue;
    while(abs(min - nextMin) > tol){
        min = nextMin;
        nextMin = p->polyValue(min) - lr * p->polyDerivative(min);
    }
    
return nextMin;
}