#include <iostream>

using namespace std;

int main()
{
    int opcion;
    float num1, num2;

    do
    {
        cout << "\n----- MENU -----\n";
        cout << "1. Sumar\n";
        cout << "2. Restar\n";
        cout << "3. Multiplicar\n";
        cout << "4. Salir\n";
        cout << "Seleccione una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
            case 1:
                cout << "Ingrese el primer numero: ";
                cin >> num1;
                cout << "Ingrese el segundo numero: ";
                cin >> num2;
                cout << "Resultado: " << num1 + num2 << endl;
                break;

            case 2:
                cout << "Ingrese el primer numero: ";
                cin >> num1;
                cout << "Ingrese el segundo numero: ";
                cin >> num2;
                cout << "Resultado: " << num1 - num2 << endl;
                break;

            case 3:
                cout << "Ingrese el primer numero: ";
                cin >> num1;
                cout << "Ingrese el segundo numero: ";
                cin >> num2;
                cout << "Resultado: " << num1 * num2 << endl;
                break;

            case 4:
                cout << "Saliendo del programa...\n";
                break;

            default:
                cout << "Opcion invalida. Intente nuevamente.\n";
        }

    } while (opcion != 4);

    system("pause");   // Evita que se cierre la consola
    return 0;
}
