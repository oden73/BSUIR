#pragma once
#include <string>

namespace AutoRepairShop {
	class Vehicle {
	public:
		Vehicle();
		
		bool operator==(Vehicle);

		virtual void start_engine() const;

		bool get_being_fixed() const;
		std::string get_vehicle_type() const;
		std::string get_serial_number() const;
		std::string get_name() const;
		std::string get_engine_type() const;

		void set_being_fixed(bool);
	private:
		std::string serial_number;
		bool is_being_fixed;

		std::string make_serial_number() const;
	protected:
		std::string name;
		std::string engine_type;
		std::string vehicle_type;
	};
}