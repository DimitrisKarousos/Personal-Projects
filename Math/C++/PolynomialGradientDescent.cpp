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

void GradientDescent(polynomial p, float lr, float tol, float &EstimatedMin){
    float prevMin = 2 * EstimatedMin;
    while(abs(prevMin - EstimatedMin) > tol){
        prevMin = EstimatedMin;
        EstimatedMin = prevMin - lr * p.polyDerivative(prevMin);
    }
}

void GradientAscent(polynomial p, float lr, float tol, float &EstimatedMax){
    float prevMax = 2 * EstimatedMax;
    while(abs(prevMax - EstimatedMax) > tol){
        prevMax = EstimatedMax;
        EstimatedMax = prevMax + lr * p.polyDerivative(prevMax);
    }
}