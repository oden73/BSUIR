#include "Vehicle.h"

namespace AutoRepairShop {
	Vehicle::Vehicle(){
		serial_number = make_serial_number();
		is_being_fixed = false;
	}

	bool Vehicle::operator==(Vehicle other) {
		return (name == other.get_name() && vehicle_type == other.get_vehicle_type()
			&& engine_type == other.get_engine_type());
	}

	std::string Vehicle::make_serial_number() const {
		std::string phone_number;
		for (int i = 0; i < 11; i++)
			phone_number += (rand() % 10 + '0');
		return phone_number;
	}

	void Vehicle::start_engine() const {}

	bool Vehicle::get_being_fixed() const { return is_being_fixed; }
	std::string Vehicle::get_serial_number() const { return serial_number; }
	std::string Vehicle::get_vehicle_type() const { return vehicle_type; }
	std::string Vehicle::get_name() const { return name; }
	std::string Vehicle::get_engine_type() const { return engine_type; }

	void Vehicle::set_being_fixed(bool being_fixed) { is_being_fixed = being_fixed; }
}