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

void NewtonRaphsonApprox(polynomial p, float initialGuess, float tol, float &EstimatedRoot){
    float lastRoot = 2 * initialGuess, currentRoot = initialGuess;
    int iterations = 0;
    while(abs(lastRoot - currentRoot) > tol || iterations <= 1000000){
        currentRoot = lastRoot - (p.polyValue(lastRoot) / p.polyDerivative(lastRoot));
        lastRoot = currentRoot;
        iterations++;
    }
    EstimatedRoot = currentRoot;
    if(iterations <= 1000000){
        cout << "Converged after " << iterations << " iterations." << endl;
    }
    else {
        cout << "Could not converge to an acceptable solution." << endl;
    }
}