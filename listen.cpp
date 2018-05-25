
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unistd.h>
#include "RF24-master/RF24.h"
// #include <sqlite3.h>

typedef uint8_t byte;

using namespace std;

RF24 radio(15,8); // radio(CE,CS)
byte addresses[][6] = {"0XXXX"};

int luminosity = 99;
stringstream radio_stream;
string value;

sqlite3 *db;
sqlite3_stmt *stmt;
string query;

void setup() {
    radio.begin();
    radio.setPALevel(RF24_PA_LOW);
    radio.openReadingPipe(1, addresses[0]);
    radio.printDetails();
    radio.startListening();
}

void loop() {
    if(radio.available()) {
        radio.read(&luminosity, sizeof(luminosity));
    }

    radio_stream << luminosity;
    string str_lum = radio_stream.str();
    radio_stream.str(string());

    query = "INSERT INTO luminosity VALUES (" + str_lum + ");";
    //cout << sqlstatement;

    if(sqlite3_open("/home/pi/peri.db", &db) == SQLITE_OK) {
        sqlite3_prepare(db, query.c_str(), -1, &stmt, NULL);
        sqlite3_step(stmt);
    }
    else
        cout << "Failure opening database \n";

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    sleep(1);
}

int main(int argc, char **argv)
{
    setup();
    while (1)
        loop();
    return 0;
}