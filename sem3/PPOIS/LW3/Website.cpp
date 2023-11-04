#include "Website.h"

#include <iostream>

namespace StudentInformationSystemLib {
	Website::Website() {
		adress = "abcd.com";
		administrators = { User("admin")};
	}

	Website::Website(std::string adress) {
		this->adress = adress;
		administrators = { User("admin")};
	}

	void Website::change_adress(User admin, std::string new_adress) {
		get_permission(admin);
		adress = new_adress;
	}

	void Website::website_update(User admin, std::string code) {
		get_permission(admin);
		std::cout << "updates are successfully applied\n";
	}

	void Website::get_permission(User admin) {
		bool permission = false;
		for (int i = 0; i < administrators.size(); i++)
			if (admin == administrators[i]){
				permission = true;
				break;
			}
		if (!permission) {
			throw std::runtime_error("throw non-admin can't change website");
		}
	}
}