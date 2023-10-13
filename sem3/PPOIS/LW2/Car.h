#pragma once
#include "Vehicle.h"

namespace AutoRepairShop {
	class Car: public Vehicle {
	public:
		Car();
		Car(std::string);

		void start_engine() const override;
	private:
		std::string type;
	};
}