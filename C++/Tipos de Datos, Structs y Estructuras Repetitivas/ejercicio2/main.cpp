#include <iostream>
#include <string>

using namespace std;

int main()
{
    string nombre;
    int edad;
    float estatura;

    cout << "Ingrese su nombre: ";
    getline(cin, nombre);   // Lee texto con espacios

    cout << "Ingrese su edad: ";
    cin >> edad;

    cout << "Ingrese su estatura (en metros): ";
    cin >> estatura;

    cout << "\n----- FICHA PERSONAL -----\n";
    cout << "Nombre   : " << nombre << endl;
    cout << "Edad     : " << edad << " años" << endl;
    cout << "Estatura : " << estatura << " m" << endl;
    cout << "---------------------------\n";
system("pause");


    return 0;
}
