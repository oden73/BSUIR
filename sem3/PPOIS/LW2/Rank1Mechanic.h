#pragma once
#include "Mechanic.h"
#include <vector>

namespace AutoRepairShop {
	class Rank1Mechanic : public Mechanic {
	public:
		Rank1Mechanic();
		Rank1Mechanic(std::string name);

		void set_new_chief(Mechanic);
		void ask_chief_for_advise() const;
		void repair_vehicle() override;

		std::string get_chief_name() const;
	private:
		std::string chief_name;
	};
}