#include "Motorcycle.h"

#include <iostream>

namespace AutoRepairShop {
	Motorcycle::Motorcycle(): Vehicle() {
		name = "Bajaj";
		engine_type = "V1";
		vehicle_type = "Motorcycle";
		weight = 200;
		type = "Sport";
		frame_material = "Carbon";
	}

	Motorcycle::Motorcycle(std::string name) {
		this-> name = name;
		engine_type = "V2";
		vehicle_type = "Motorcycle";
		weight = 150;
		type = "Off-road";
		frame_material = "Titanuim";
	}

	void Motorcycle::start_engine() const {
		std::cout << "vruuum vumvum... engine started";
	}
}