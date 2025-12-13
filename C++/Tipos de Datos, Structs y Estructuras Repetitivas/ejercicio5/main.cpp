#include <iostream>
#include <string>

using namespace std;

struct Estudiante
{
    string nombre;
    int edad;
    float promedio;
};

int main()
{
    Estudiante estudiantes[3];
    int mejor = 0;  // índice del mejor promedio

    for (int i = 0; i < 3; i++)
    {
        cout << "\nIngrese los datos del estudiante " << i + 1 << endl;

        cout << "Nombre: ";
        cin.ignore();                // limpia el buffer
        getline(cin, estudiantes[i].nombre);

        cout << "Edad: ";
        cin >> estudiantes[i].edad;

        cout << "Promedio: ";
        cin >> estudiantes[i].promedio;

        // Comparar promedios
        if (estudiantes[i].promedio > estudiantes[mejor].promedio)
        {
            mejor = i;
        }
    }

    cout << "\n----- ESTUDIANTE CON MEJOR PROMEDIO -----\n";
    cout << "Nombre   : " << estudiantes[mejor].nombre << endl;
    cout << "Edad     : " << estudiantes[mejor].edad << endl;
    cout << "Promedio : " << estudiantes[mejor].promedio << endl;
    cout << "----------------------------------------\n";

    system("pause");   // Evita que la consola se cierre
    return 0;
}
