#include <iostream>

using namespace std;

int main()
{
    int numero;
    int pares = 0;
    int impares = 0;

    for (int i = 1; i <= 10; i++)
    {
        cout << "Ingrese el numero " << i << ": ";
        cin >> numero;

        if (numero % 2 == 0)
        {
            pares++;
        }
        else
        {
            impares++;
        }
    }

    cout << "\nCantidad de numeros pares: " << pares << endl;
    cout << "Cantidad de numeros impares: " << impares << endl;

    system("pause");   // Evita que la consola se cierre
    return 0;
}
