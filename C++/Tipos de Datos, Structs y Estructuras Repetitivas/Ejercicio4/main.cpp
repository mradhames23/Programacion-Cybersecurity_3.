#include <iostream>

using namespace std;

int main()
{
    float base, altura, area;

    cout << "Ingrese la base del rectangulo: ";
    cin >> base;

    cout << "Ingrese la altura del rectangulo: ";
    cin >> altura;

    area = base * altura;

    cout << "\nEl area del rectangulo es: " << area << endl;

    system("pause");   // Evita que la ventana se cierre

    return 0;
}
