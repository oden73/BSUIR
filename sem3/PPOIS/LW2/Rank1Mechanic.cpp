#include "Rank1Mechanic.h"

#include <iostream>
#include <Windows.h>

namespace AutoRepairShop {
	Rank1Mechanic::Rank1Mechanic() : Mechanic() {
		allowed_vehicle_types = { "Car", "Motorcycle" };
	}

	Rank1Mechanic::Rank1Mechanic(std::string name) : Mechanic(name) {
		allowed_vehicle_types = { "Car", "Motorcycle" };
	}

	void Rank1Mechanic::ask_chief_for_advise() const {
		std::cout << "asking for advise... now this mechanic is more smarter!\n";
	}
	
	void Rank1Mechanic::repair_vehicle() {
		cout << "fixing...\n";
		Sleep(1000);
		if (vehicle.get_vehicle_type() == "Car") {
			cout << "fixing...\n";
			Sleep(1000);
		}
		cout << "job done, vehicle is fixed!\n";
		vehicle.set_being_fixed(false);
	}

	void Rank1Mechanic::set_new_chief(Mechanic new_chief) { chief_name = new_chief.get_name(); }

	std::string Rank1Mechanic::get_chief_name() const { return chief_name; }
}