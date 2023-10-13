#include "Car.h"

#include <iostream>

namespace AutoRepairShop {
	Car::Car() : Vehicle() {
		name = "Toyota";
		engine_type = "4A-GE";
		type = "coupe";
		vehicle_type = "Car";
	}

	Car::Car(std::string name): Vehicle() {
		this->name = name;
		engine_type = "V6";
		vehicle_type = "Car";
		type = "coupe";
	}

	void Car::start_engine() const {
		std::cout << "vruuum vrumvrum... engine started\n";
	}
}