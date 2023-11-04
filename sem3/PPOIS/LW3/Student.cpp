#include "Student.h"

#include <iostream>

namespace StudentInformationSystemLib {
	Student::Student() : User() { personal_account = PersonalAccount(); };
	Student::Student(std::string name) : User(name) { personal_account = PersonalAccount(); };
	
	void Student::recieve_message(std::string message) { personal_account.recieve_message(message); }
	void Student::show_message(std::string message) const { personal_account.show_message(message); }
	void Student::pass_exams() const {
		std::cout << "you successfully have passed your exams, congratulations!\nyour marks you can see in your personal account\n";
	}

	void Student::get_missing_hours() { personal_account.get_missing_hours(); }
	void Student::forgot_personal_account_password() { personal_account.forgot_password(this); }

	void Student::punishment() const { personal_account.punishment(); }
	void Student::pass_a_certificate() { personal_account.pass_a_certificate(); }
	void Student::show_all_mail() const { personal_account.show_all_mail(); }

	std::string Student::get_group_number() const { return group_number; }
	int Student::show_missing_hours() const { return personal_account.show_missing_hours(); }
	
	void Student::set_group_number(std::string group_number) { this->group_number = group_number; }

}