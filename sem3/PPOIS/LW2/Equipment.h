#pragma once
#include <vector>
#include <string>

using namespace std;

namespace AutoRepairShop {
	class Equipment {
	public:
		Equipment();
		Equipment(string, vector<string>);
		void operator +=(Equipment);
		bool operator==(Equipment);
		
		string get_name() const;
		int get_total_amount() const;
		vector<string> get_vehicle_types() const;
	private:
		int total_amount;
		string name;
		std::vector<string> for_what_vehicle_types;
	};
}