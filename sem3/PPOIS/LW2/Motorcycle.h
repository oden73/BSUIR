#pragma once
#include "Vehicle.h"

namespace AutoRepairShop {
	class Motorcycle : public Vehicle {
	public:
		Motorcycle();
		Motorcycle(std::string);

		void start_engine() const override;
	private:
		std::string type;
		std::string frame_material;
		int weight;
	};
}