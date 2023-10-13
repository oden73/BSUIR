#include "Equipment.h"

namespace AutoRepairShop {
	Equipment::Equipment() {
		name = "Tool for vehicles";
		for_what_vehicle_types = { "Car", "Motorcycle", "Truck", "Bus" };
		total_amount = 10;
	}

	Equipment::Equipment(string name, vector<string> vehicle_types) {
		this->name = name;
		for_what_vehicle_types = vehicle_types;
		total_amount = 15;
	}

	void Equipment::operator +=(Equipment add_equipment) {
		total_amount += add_equipment.get_total_amount();
	}

	bool Equipment::operator==(Equipment other) {
		return name == other.get_name();
	}

	int Equipment::get_total_amount() const { return total_amount; }
	string Equipment::get_name() const { return name; }
	vector<string> Equipment::get_vehicle_types() const { return for_what_vehicle_types; }
}