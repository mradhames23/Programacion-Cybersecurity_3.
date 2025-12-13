#include <iostream>

using namespace std;

int main()
{
    int num1, num2;

    cout << "Ingrese el primer numero entero: ";
    cin >> num1;

    cout << "Ingrese el segundo numero entero: ";
    cin >> num2;

    cout << "\nResultados:\n";
    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicacion: " << num1 * num2 << endl;

    if (num2 != 0)
    {
        cout << "Division: " << (float)num1 / num2 << endl;
    }
    else
    {
        cout << "Division: No se puede dividir entre cero" << endl;
    }
    system("pause");


    return 0;
}

