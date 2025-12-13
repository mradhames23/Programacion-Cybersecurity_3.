#include <iostream>

using namespace std;

int main()
{
    float celsius, fahrenheit;

    cout << "Ingrese la temperatura en grados Celsius: ";
    cin >> celsius;

    fahrenheit = (celsius * 9 / 5) + 32;

    cout << "\nTemperatura en Fahrenheit: " << fahrenheit << " °F" << endl;

    system("pause");   // Evita que la ventana se cierre
    return 0;
}
