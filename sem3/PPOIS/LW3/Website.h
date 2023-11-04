#pragma once
#include "User.h"

#include <string>
#include <vector>

namespace StudentInformationSystemLib {
	class Website {
	public:
		Website();
		Website(std::string);

		void change_adress(User, std::string);
		void website_update(User, std::string);
	private:
	protected:
		std::string adress;
		std::vector<User> administrators;
		
		void get_permission(User);
	};
}