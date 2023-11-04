#pragma once
#include "User.h"

#include <vector>

namespace StudentInformationSystemLib {
	class PersonalAccount{
	public:
		PersonalAccount();

		void forgot_password(User*) const;
		void punishment() const;
		void pass_a_certificate();
		void recieve_message(std::string);
		void show_message(std::string) const;
		void show_all_mail() const;
		void get_missing_hours();
	
		int show_missing_hours() const;
	private:
		void message_presence_check(std::string) const;

		int missed_hours;
		std::vector<std::string> mail;
	};
}