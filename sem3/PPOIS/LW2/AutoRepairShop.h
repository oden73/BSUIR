#pragma once
#include "Mechanic.h"
#include "Rank2Mechanic.h"
#include "Rank1Mechanic.h"
#include "Vehicle.h"
#include "Equipment.h"
#include <vector>

namespace AutoRepairShop {
	class AutoRepairShopClass {
	public:
		AutoRepairShopClass();
		
		void add_new_vehicle(Vehicle);
		void add_new_rank1mechanic(Rank1Mechanic);
		void add_new_rank2mechanic(Rank2Mechanic);
		void add_new_equipment(Equipment);
		void send_vehicle(Mechanic);
		void assign_free_mechanic();
	

		void remove_rank1_mechanic(Rank1Mechanic);
		void remove_rank2_mechanic(Rank2Mechanic);
		void remove_equipment(Equipment);
		void remove_vehicle(Vehicle);
		
		std::string get_name() const;
		std::string get_adress() const;
		std::vector <Vehicle> get_vehicles_list() const;
		std::vector<Equipment> get_equipment_list() const;
		std::vector<Mechanic> get_total_mechanics_list() const;
		std::vector<Rank1Mechanic> get_rank1mechanic_list() const;
		std::vector<Rank2Mechanic> get_rank2mechanic_list() const;
	private:
		std::string name;
		std::string adress;
		std::vector<Vehicle> vehicles_list;
		std::vector<Equipment> equipment_list;
		std::vector<Rank2Mechanic> chiefs_list;
		std::vector<Rank1Mechanic> rank1mechanics_list;

		vector<pair<Vehicle, int>> finding_free_vehicles() const;
		void get_chief_for_rank1mechanic(Rank1Mechanic*);
	};
}