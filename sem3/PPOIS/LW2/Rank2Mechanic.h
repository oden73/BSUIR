#pragma once
#include "Rank1Mechanic.h"

namespace AutoRepairShop {
	class Rank2Mechanic : public Mechanic {
	public:
		Rank2Mechanic();
		Rank2Mechanic(std::string);

		void take_lecture() const;
		void repair_vehicle() override;
		void get_new_subordinate(Rank1Mechanic);
		void remove_subordinate(std::string);

		std::vector<std::string> get_subordinates() const;

	private:
		std::vector<std::string> subordinates_names;
	};
}