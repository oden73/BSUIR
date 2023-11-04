#pragma once
#include "User.h"
#include "PersonalAccount.h"

#include <vector>


namespace StudentInformationSystemLib {
	class Student : public User {
	public:
		Student();
		Student(std::string);
		
		void forgot_personal_account_password();
		void pass_exams() const;
		void recieve_message(std::string);
		void get_missing_hours();
		void show_message(std::string) const;
		void punishment() const;
		void pass_a_certificate();
		void show_all_mail() const;

		std::string get_group_number() const;
		int show_missing_hours() const;

		void set_group_number(std::string);
	private:
		std::string group_number;
		PersonalAccount personal_account;
	};
}