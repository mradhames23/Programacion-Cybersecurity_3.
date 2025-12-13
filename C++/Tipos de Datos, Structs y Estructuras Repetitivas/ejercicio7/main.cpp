#include <iostream>

using namespace std;

int main()
{
    int numero;

    cout << "Ingrese un numero: ";
    cin >> numero;

    cout << "\nTabla de multiplicar del " << numero << ":\n";

    for (int i = 1; i <= 12; i++)
    {
        cout << numero << " x " << i << " = " << numero * i << endl;
    }

    system("pause");   // Evita que la consola se cierre
    return 0;
}
