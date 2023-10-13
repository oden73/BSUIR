#pragma once
#include "Equipment.h"
#include "Vehicle.h"

#include <string>
#include <vector>

using namespace std;

namespace AutoRepairShop {
	class Mechanic {
	public:
		Mechanic();
		Mechanic(string name);

		bool operator==(Mechanic other);

		virtual void repair_vehicle(); // cout << fixing.... pause cout << fixing... и тд, если автобус или грузовое, то подольше, а еще с некоторым шансом сделать поломку некоторого оборудования
		
		void get_new_vehicle(Vehicle);
		void check_equipment_for_breakdown() const; // вызывать внутри repair
		void go_on_lunch_break() const;

		bool get_is_busy() const;
		vector<string> get_allowed_vehicle_types() const;
		Vehicle get_vehicle() const;
		string get_name() const;

		void set_is_not_busy();
		void set_equipment(vector<Equipment>);
	private:
		int age;
		std::string working_since;
		std::string name;
		// AutoRepairShopClass repair_shop;
		bool is_busy;
	protected:
		std::vector<std::string> allowed_vehicle_types;
		std::vector<Equipment> neccessary_equipment;
		Vehicle vehicle;
	};
}