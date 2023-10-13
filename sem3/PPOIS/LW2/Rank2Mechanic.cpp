#include "Rank2Mechanic.h"

#include <iostream>
#include <Windows.h>

namespace AutoRepairShop {
	Rank2Mechanic::Rank2Mechanic() : Mechanic() {
		allowed_vehicle_types = { "Car", "Motorcycle", "Bus", "Truck" };
	}

	Rank2Mechanic::Rank2Mechanic(std::string name) : Mechanic(name) {
		allowed_vehicle_types = { "Car", "Motorcycle", "Bus", "Truck" };
	}

	void Rank2Mechanic::take_lecture() const {
		std::cout << "learning subordinates new things... job done!\n";
	}

	void Rank2Mechanic::repair_vehicle() {
		string type = vehicle.get_vehicle_type();
		if (type == "Motorcycle") {
			cout << "fixing...\n";
			Sleep(1000);
		}
		if (type == "Car") {
			for (int i = 0; i < 2; i++) {
				cout << "fixing...\n";
				Sleep(1000);
			}
		}
		if (type == "Truck") {
			for (int i = 0; i < 3; i++) {
				cout << "fixing...\n";
				Sleep(1000);
			}
		}
		if (type == "Bus") {
			for (int i = 0; i < 4; i++) {
				cout << "fixing...\n";
				Sleep(1000);
			}
		}
		cout << "job done, vehicle is fixed!\n";
		vehicle.set_being_fixed(false);
	}

	void Rank2Mechanic::get_new_subordinate(Rank1Mechanic new_mechanic){
		subordinates_names.push_back(new_mechanic.get_name());
	}

	void Rank2Mechanic::remove_subordinate(std::string removable_mechanic_name) {
		int index = 0;
		for(int i = 0; i < subordinates_names.size(); i ++)
			if (subordinates_names[i] == removable_mechanic_name) {
				index = i;
				break;
			}
		subordinates_names.erase(subordinates_names.begin() + index);
	}

	std::vector<std::string> Rank2Mechanic::get_subordinates() const { return subordinates_names; }
}