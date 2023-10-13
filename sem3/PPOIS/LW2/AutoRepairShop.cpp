#include "AutoRepairShop.h"
#include "Bus.h"
#include "Car.h"
#include "Truck.h"
#include "Motorcycle.h"
#include <iostream>
#include <algorithm>

namespace AutoRepairShop {
	AutoRepairShopClass::AutoRepairShopClass() {
		name = "Repair Shop 322";
		adress = "Brown st. 32";
		vehicles_list = { Truck("Mercedes"), Car("Mazda"), Car(), Motorcycle(), Bus(), Car("BMW")};
		this->add_new_rank2mechanic(Rank2Mechanic());
		this->add_new_rank2mechanic(Rank2Mechanic("Vladislav Korolkov"));
		this->add_new_rank1mechanic(Rank1Mechanic("Egor Glyoza"));
		this->add_new_rank1mechanic(Rank1Mechanic("Maksim Karpuk"));
		this->add_new_rank1mechanic(Rank1Mechanic("Vyacheslav Ageenko"));
		equipment_list = { Equipment("Wrench", {"Car", "Truck", "Bus", "Motorcycle"}),
							Equipment("Hydraulic press", {"Car", "Truck", "Bus"}),
							Equipment("Smaller Hydraulic press", {"Motorcycle"}),
							Equipment("Machine", {"Truck", "Bus"}),
							Equipment() };
	}

	void AutoRepairShopClass::add_new_vehicle(Vehicle new_vehicle) {
		vehicles_list.push_back(new_vehicle);
	}

	void AutoRepairShopClass::add_new_rank1mechanic(Rank1Mechanic new_mechanic) {
		get_chief_for_rank1mechanic(&new_mechanic);
		vector<Equipment> mechanic_equipment;
		for (int i = 0; i < equipment_list.size(); i++) {
			vector<string> vehicle_types = equipment_list[i].get_vehicle_types();
			for (int vehicle_type = 0; vehicle_type < vehicle_types.size(); vehicle_type++)
				if (vehicle_types[vehicle_type] == "Car" || vehicle_types[vehicle_type] == "Motorcycle") {
					mechanic_equipment.push_back(equipment_list[i]);
				}
		}
		new_mechanic.set_equipment(mechanic_equipment);
		for (int i = 0; i < vehicles_list.size(); i++)
			if (!vehicles_list[i].get_being_fixed() &&
				(vehicles_list[i].get_vehicle_type() == "Car" ||
					vehicles_list[i].get_vehicle_type() == "Motorcycle")) {
				new_mechanic.get_new_vehicle(vehicles_list[i]);
				vehicles_list[i].set_being_fixed(true);
				break;
			}
		rank1mechanics_list.push_back(new_mechanic);
	}

	void AutoRepairShopClass::add_new_rank2mechanic(Rank2Mechanic new_mechanic) {
		for (int i = 0; i < vehicles_list.size(); i ++)
			if (!vehicles_list[i].get_being_fixed()) {
				new_mechanic.get_new_vehicle(vehicles_list[i]);
				vehicles_list[i].set_being_fixed(true);
				break;
			}
		new_mechanic.set_equipment(equipment_list);
		chiefs_list.push_back(new_mechanic);
	}

	void AutoRepairShopClass::add_new_equipment(Equipment new_equipment) {
		bool repair_shop_has = false;
		for(int i = 0; i < equipment_list.size(); i ++)
			if (equipment_list[i] == new_equipment) {
				repair_shop_has = true;
				equipment_list[i] += new_equipment;
				break;
			}
		if (!repair_shop_has)
			equipment_list.push_back(new_equipment);
	}

	void AutoRepairShopClass::send_vehicle(Mechanic mechanic_alligned_to_vehicle) {
		int sending_vehicle = 0;
		for (int i = 0; i < vehicles_list.size(); i++) {
			if (vehicles_list[i].get_serial_number() ==
				mechanic_alligned_to_vehicle.get_vehicle().get_serial_number()) {
				sending_vehicle = i;
				break;
			}
		}
		//mechanic_alligned_to_vehicle.set_is_not_busy();
		vehicles_list.erase(vehicles_list.begin() + sending_vehicle);
		for(int i = 0; i < rank1mechanics_list.size(); i ++)
			if (rank1mechanics_list[i].get_name() == mechanic_alligned_to_vehicle.get_name()) {
				rank1mechanics_list[i].set_is_not_busy();
				return;
			}
		for (int i = 0; i < chiefs_list.size(); i++)
			if (chiefs_list[i].get_name() == mechanic_alligned_to_vehicle.get_name()) {
				chiefs_list[i].set_is_not_busy();
				return;
			}
	}

	void AutoRepairShopClass::assign_free_mechanic() {
		vector<pair<Vehicle, int>> free_vehicles = finding_free_vehicles();
		for (int i = 0; i < rank1mechanics_list.size(); i++) {
			if (!rank1mechanics_list[i].get_is_busy()) {
				for (int j = 0; j < free_vehicles.size(); j++) {
					if (free_vehicles[j].first.get_vehicle_type() == "Car" ||
						free_vehicles[j].first.get_vehicle_type() == "Motorcycle") {
						rank1mechanics_list[i].get_new_vehicle(free_vehicles[j].first);
						vehicles_list[free_vehicles[j].second].set_being_fixed(true);
						return;
					}
				}
			}
		}
		for (int i = 0; i < chiefs_list.size(); i++) 
			if (!chiefs_list[i].get_is_busy()) {
				chiefs_list[i].get_new_vehicle(free_vehicles[0].first);
				vehicles_list[free_vehicles[0].second].set_being_fixed(true);
				return;
			}
		throw runtime_error("there are no correct vehicles for free mechanics");
	}

	void AutoRepairShopClass::remove_equipment(Equipment removable_equipment) {
		std::string find_name = removable_equipment.get_name();
		int index = -1;
		for (int i = 0; i < equipment_list.size(); i++)
			if (equipment_list[i].get_name() == find_name) {
				index = i;
				break;
			}
		if (index == -1) {
			throw runtime_error("there is no such equipment for remove");
		}
		equipment_list.erase(equipment_list.begin() + index);
	}

	void AutoRepairShopClass::remove_vehicle(Vehicle removable_vehicle) {
		std::string find_number = removable_vehicle.get_serial_number();
		int index = -1;
		for (int i = 0; i < vehicles_list.size(); i++)
			if (vehicles_list[i].get_serial_number() == find_number) {
				index = i;
				break;
			}
		if (index == -1) {
			throw runtime_error("there is no such equipment for remove");
		}
		vehicles_list.erase(vehicles_list.begin() + index);
	}

	vector<pair<Vehicle, int>> AutoRepairShopClass::finding_free_vehicles() const{
		vector<pair<Vehicle, int>> free_vehicles;
		for (int i = 0; i < vehicles_list.size(); i++) {
			if (!vehicles_list[i].get_being_fixed()) {
				free_vehicles.emplace_back(vehicles_list[i], i);
			}
		}

		if (free_vehicles.size() == 0) {
			throw runtime_error("there are no free vehicles");
		}
		return free_vehicles;
	}

	void AutoRepairShopClass::get_chief_for_rank1mechanic(Rank1Mechanic* new_mechanic) {
		std::random_shuffle(chiefs_list.begin(), chiefs_list.end());
		new_mechanic->set_new_chief(chiefs_list[0]);
		chiefs_list[0].get_new_subordinate(*new_mechanic);
	}

	void AutoRepairShopClass::remove_rank1_mechanic(Rank1Mechanic removable_mechanic) {
		std::string find_name = removable_mechanic.get_name();
		int index = -1;
		for(int i = 0; i < rank1mechanics_list.size(); i ++)
			if (rank1mechanics_list[i].get_name() == find_name) {
				index = i;
				std::string chief_name = rank1mechanics_list[i].get_chief_name();
				for(int j = 0; j < chiefs_list.size(); j ++)
					if (chiefs_list[j].get_name() == chief_name) {
						chiefs_list[j].remove_subordinate(find_name);
						break;
					}
			}
		if (index == -1) {
			throw runtime_error("there is no such rank 1 mechanic");
		}
		rank1mechanics_list.erase(rank1mechanics_list.begin() + index);
	}

	void AutoRepairShopClass::remove_rank2_mechanic(Rank2Mechanic removable_mechanic) {
		int index = -1;
		std::string find_name = removable_mechanic.get_name();
		for (int i = 0; i < chiefs_list.size(); i++)
			if (chiefs_list[i].get_name() == find_name) {
				index = i;
				break;
			}
		if (index == -1) {
			throw runtime_error("there is no such rank 2 mechanic");
		}
		vector<string> subordinates = chiefs_list[index].get_subordinates();
		chiefs_list.erase(chiefs_list.begin() + index);
		for (int i = 0; i < subordinates.size(); i++) 
			for(int j = 0; j < rank1mechanics_list.size(); j ++)
				if (rank1mechanics_list[j].get_name() == subordinates[i]) {
					get_chief_for_rank1mechanic(&rank1mechanics_list[j]);
				}
	}

	std::string AutoRepairShopClass::get_name() const { return name; }
	std::string AutoRepairShopClass::get_adress() const { return adress; }
	std::vector<Vehicle> AutoRepairShopClass::get_vehicles_list() const { return vehicles_list; }
	std::vector<Equipment> AutoRepairShopClass::get_equipment_list() const { return equipment_list; }
	std::vector<Rank1Mechanic> AutoRepairShopClass::get_rank1mechanic_list() const { return rank1mechanics_list; }
	std::vector<Rank2Mechanic> AutoRepairShopClass::get_rank2mechanic_list() const { return chiefs_list; }

	vector<Mechanic> AutoRepairShopClass::get_total_mechanics_list() const{
		vector<Mechanic> mechanics_list;
		for (int i = 0; i < chiefs_list.size(); mechanics_list.push_back(chiefs_list[i++]));
		for (int i = 0; i < rank1mechanics_list.size(); mechanics_list.push_back(rank1mechanics_list[i++]));
		return mechanics_list;
	}
}	