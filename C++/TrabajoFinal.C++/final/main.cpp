#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Estructura que simula una fila de una matriz de intentos
struct IntentoAcceso
{
    string usuario;
    string servidor;
    string ip;
    string tipo;   // Exitoso o Fallido
    string hora;
};

// Prototipos de funciones
void RegistrarIntento(vector<IntentoAcceso>& intentos);
void MostrarReporte(const vector<IntentoAcceso>& intentos);
void GenerarAlertas(const vector<IntentoAcceso>& intentos);

int main()
{
    vector<IntentoAcceso> intentos;
    int opcion;

    do
    {
        cout << "\n===== SISTEMA DE MONITOREO DE ACCESOS =====\n";
        cout << "1. Registrar intento de acceso\n";
        cout << "2. Mostrar reporte\n";
        cout << "3. Generar alertas\n";
        cout << "4. Salir\n";
        cout << "Seleccione una opcion: ";
        cin >> opcion;

        switch (opcion)
        {
            case 1:
                RegistrarIntento(intentos);
                break;
            case 2:
                MostrarReporte(intentos);
                break;
            case 3:
                GenerarAlertas(intentos);
                break;
            case 4:
                cout << "Saliendo del sistema...\n";
                break;
            default:
                cout << "Opcion invalida.\n";
        }

    } while (opcion != 4);

    system("pause");
    return 0;
}

// 🔹 Registrar un intento de acceso
void RegistrarIntento(vector<IntentoAcceso>& intentos)
{
    IntentoAcceso nuevo;

    cin.ignore();
    cout << "Usuario: ";
    getline(cin, nuevo.usuario);

    cout << "Servidor: ";
    getline(cin, nuevo.servidor);

    cout << "IP: ";
    getline(cin, nuevo.ip);

    cout << "Tipo (Exitoso/Fallido): ";
    getline(cin, nuevo.tipo);

    cout << "Hora (HH:MM): ";
    getline(cin, nuevo.hora);

    intentos.push_back(nuevo);
    cout << "Intento registrado correctamente.\n";
}

// 🔹 Mostrar todos los intentos
void MostrarReporte(const vector<IntentoAcceso>& intentos)
{
    if (intentos.empty())
    {
        cout << "No hay intentos registrados.\n";
        return;
    }

    cout << "\n----- REPORTE DE ACCESOS -----\n";
    for (int i = 0; i < intentos.size(); i++)
    {
        cout << "\nIntento " << i + 1 << endl;
        cout << "Usuario  : " << intentos[i].usuario << endl;
        cout << "Servidor : " << intentos[i].servidor << endl;
        cout << "IP       : " << intentos[i].ip << endl;
        cout << "Tipo     : " << intentos[i].tipo << endl;
        cout << "Hora     : " << intentos[i].hora << endl;
    }
}

// 🔹 Generar alertas por intentos fallidos
void GenerarAlertas(const vector<IntentoAcceso>& intentos)
{
    int fallidos = 0;

    for (int i = 0; i < intentos.size(); i++)
    {
        if (intentos[i].tipo == "Fallido" || intentos[i].tipo == "fallido")
        {
            fallidos++;
        }
    }

    cout << "\n----- ALERTAS DE SEGURIDAD -----\n";
    cout << "Intentos fallidos detectados: " << fallidos << endl;

    if (fallidos >= 3)
    {
        cout << "⚠️ ALERTA: Posible intento de intrusión.\n";
    }
    else
    {
        cout << "Sistema estable.\n";
    }
}
