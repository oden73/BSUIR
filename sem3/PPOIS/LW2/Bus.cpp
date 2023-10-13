#include "Bus.h"

#include <iostream>

namespace AutoRepairShop {
	Bus::Bus(): Vehicle() {
		name = "MAZ";
		engine_type = "V6";
		vehicle_type = "Bus";
		seats_amount = 50;
		owning_company = "BSUIR";
	}

	Bus::Bus(std::string name): Vehicle() {
		this->name = name;
		engine_type = "V8";
		vehicle_type = "Bus";
		seats_amount = 60;
		owning_company = "MTZ";
	}

	void Bus::start_engine() const{
		std::cout << "Brrr turturtur... engine started\n";
	}
}