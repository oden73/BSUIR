#pragma once
#include "Vehicle.h"

namespace AutoRepairShop {
	class Truck : public Vehicle {
	public:
		Truck();
		Truck(std::string);

		void start_engine() const override;
	private:
		bool has_trailer;
		std::string owning_company;
	};
}