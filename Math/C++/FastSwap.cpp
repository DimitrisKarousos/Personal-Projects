#include<iostream>

using namespace std;

class Vector3{
	float x, y, z;
	public:
		Vector3(float xDef, float yDef, float zDef){
			x = xDef;
			y = yDef;
			z = zDef;
		}
		void descVector3(){
			cout << "This vector is represented by the following coordinates: x=" << x << " y=" << y << " z=" << z << "." << endl;

		}
		void getVector3(){
			cout << x << " " << y << " " << z << endl;
		}
		float getX(){
			return x;
		}
		float getY(){
			return y;
		}
		float getZ(){
			return z;
		}
		void setX(float xSet){
			x = xSet;
		}
		void setY(float ySet){
			y = ySet;
		}
		void setZ(float zSet){
			z = zSet;
		}
		~Vector3(){
			cout << "Vector destroyed." << endl;
		}
};

void plebSwap(float &a, float &b){ // create third variable so it is easier to follow
	float temp = a;
	a = b;
	b = temp;
}

void ChadSwap(float &a, float &b){ // faster but wrecks memory causal chains
	a = a + b;
	b = a - b;
	a = a - b;
}

void ChadSwapVec3(Vector3 &a, Vector3 &b){
	a.setX(a.getX() + b.getX());
	b.setX(a.getX() - b.getX());
	a.setX(a.getX() - b.getX());

	a.setY(a.getY() + b.getY());
	b.setY(a.getY() - b.getY());
	a.setY(a.getY() - b.getY());

	a.setZ(a.getZ() + b.getZ());
	b.setZ(a.getZ() - b.getZ());
	a.setZ(a.getZ() - b.getZ());

}

int main(){
	
	float x = 5, y = 0.4;
	Vector3 a(0, 0.2, -1), b(4, 3.1, -0.7);

	cout<<"Swaping integers "<< x << " " << y <<endl;
	plebSwap(x,y);
	cout<< x << " " << y << endl;
	ChadSwap(x,y);
	cout<< x << " " << y << endl;

	cout << "Swapping vectors " << a.getVector3() << " " << b.getVector3() << endl;
	ChadSwapVec3(a, b);
	cout << a.getVector3() << " " << b.getVector3() << endl;

	return 0;
}
