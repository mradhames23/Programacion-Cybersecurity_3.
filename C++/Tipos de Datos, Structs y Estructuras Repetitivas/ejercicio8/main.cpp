#include <iostream>

using namespace std;

int main()
{
    int numero;
    int suma = 0;

    cout << "Ingrese un numero (0 para terminar): ";
    cin >> numero;

    while (numero != 0)
    {
        suma += numero;

        cout << "Ingrese otro numero (0 para terminar): ";
        cin >> numero;
    }

    cout << "\nLa suma total es: " << suma << endl;

    system("pause");   // Evita que la consola se cierre
    return 0;
}
