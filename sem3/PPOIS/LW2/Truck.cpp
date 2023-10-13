#include "Truck.h"

#include <iostream>

namespace AutoRepairShop {
	Truck::Truck(): Vehicle() {
		name = "KamAZ";
		engine_type = "V6";
		vehicle_type = "Truck";
		has_trailer = false;
		owning_company = "Coal mine Inc.";
	}

	Truck::Truck(std::string name): Vehicle() {
		this->name = name;
		engine_type = "V8";
		vehicle_type = "Truck";
		has_trailer = true;
		owning_company = "BSUIR";
	}

	void Truck::start_engine() const {
		std::cout << "Brrr brbrbrbr... engine started\n";
	}
}