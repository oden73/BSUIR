#include "User.h"

#include <string>

namespace StudentInformationSystemLib {
	User::User() {
		name = "Arthur Morgan";
		user_name = "123";
		user_email = "123@gmail.com";
		user_password = "123";
	}
	
	User::User(std::string name) {
		this->name = name;
		this->user_name = name + "228";
		user_email = user_name + "@gmail.com";
		user_password = "123";
	}

	bool User::operator==(User other) {
		return name == other.get_name() && user_name == other.get_user_name();
	}

	std::string User::get_name() const { return name; }
	std::string User::get_user_name() const { return user_name; }
	std::string User::get_user_email() const { return user_email; }
	std::string User::get_password() const { return user_password; }
	
	void User::set_password(std::string password) { user_password = password; }

}
