#pragma once
#include "Vehicle.h"

namespace AutoRepairShop {
	class Bus : public Vehicle {
	public:
		Bus();
		Bus(std::string);
		void start_engine() const override;
	private:
		int seats_amount;
		std::string owning_company;
	};
}