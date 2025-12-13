#include <iostream>
#include <string>

using namespace std;

struct Producto
{
    string nombre;
    float precio;
    int cantidad;
};

int main()
{
    Producto productos[5];
    float totalInventario = 0;

    for (int i = 0; i < 5; i++)
    {
        cout << "\nIngrese los datos del producto " << i + 1 << endl;

        cout << "Nombre: ";
        cin.ignore();
        getline(cin, productos[i].nombre);

        cout << "Precio: ";
        cin >> productos[i].precio;

        cout << "Cantidad: ";
        cin >> productos[i].cantidad;

        totalInventario += productos[i].precio * productos[i].cantidad;
    }

    cout << "\n----- VALOR TOTAL DEL INVENTARIO -----\n";
    cout << "Total: $" << totalInventario << endl;
    cout << "-------------------------------------\n";

    system("pause");   // Evita que se cierre la consola
    return 0;
}

