#include "Mechanic.h"

#include <iostream>
#include <Windows.h>

namespace AutoRepairShop {
	Mechanic::Mechanic() {
		name = "Arthur Morgan";
		age = 36;
		working_since = "02.02.2000";
		is_busy = false;
	}

	Mechanic::Mechanic(string name) {
		this->name = name;
		age = 30;
		working_since = "01.01.2023";
		is_busy = false;
	}

	bool Mechanic::operator==(Mechanic other) {
		return name == other.get_name();
	}

	void Mechanic::repair_vehicle() {}

	void Mechanic::get_new_vehicle(Vehicle new_vehicle) {
		is_busy = true;
		new_vehicle.set_being_fixed(true);
		vehicle = new_vehicle;
	}

	void Mechanic::check_equipment_for_breakdown() const {
		if (rand() % 4) {
			std::cout << "something went wrong... repairing equipment..\n";
			Sleep(1000);
			std::cout << "equipment is repaired!\n";
			return;
		}
		std::cout << "fixing went fine! equipment is OK\n";
	}

	void Mechanic::go_on_lunch_break() const {
		std::cout << "it's lunch time! vehicles will wait...\n nomnomnom...\n";
		Sleep(2000);
		std::cout << "lunch is over :( getting back to work\n";
	}

	bool Mechanic::get_is_busy() const { return is_busy; }
	std::vector<std::string> Mechanic::get_allowed_vehicle_types() const { return allowed_vehicle_types; }
	Vehicle Mechanic::get_vehicle() const { return vehicle; }
	std::string Mechanic::get_name() const { return name; }

	void Mechanic::set_is_not_busy() { is_busy = false; }
	void Mechanic::set_equipment(vector<Equipment> equipment) { neccessary_equipment = equipment; }
}