#include "PersonalAccount.h"

#include <iostream>

namespace StudentInformationSystemLib {
	PersonalAccount::PersonalAccount() {
		missed_hours = rand() % 10 + 1;
	}
	
	void PersonalAccount::punishment() const {
		if (missed_hours > 10) {
			std::cout << "NO MONEY HONEY!!!!! for 1 month\n";
		}
		if (72 - missed_hours < 10) {
			std::cout << "you may be removed from university soon\n";
		}
	}

	void PersonalAccount::pass_a_certificate() {
		missed_hours = std::max(0, missed_hours - rand() % 20 + 2);
	}

	void PersonalAccount::forgot_password(User* user) const {
		std::cout << "enter email to confirm personality: ";
		std::string email;
		std::cin >> email;
		if (email != user->get_user_email())
			throw std::runtime_error("you can't change your password");
		std::string password;
		std::cout << "enter new password: ";
		std::cin >> password;
		user->set_password(password);
	}

	void PersonalAccount::recieve_message(std::string message) { mail.push_back(message); }

	void PersonalAccount::show_message(std::string message) const {
		message_presence_check(message);
		std::cout << "your recieved message:\n" << message << '\n';
	}

	void PersonalAccount::show_all_mail() const {
		if (mail.size() == 0) {
			std::cout << "inbox is empty\n";
			return;
		}
		for (int i = mail.size() - 1; i >= 0; i--)
			std::cout << "message #" << mail.size() - i + 1 << " " << mail[i] << '\n';
	}

	void PersonalAccount::get_missing_hours() { missed_hours += 2; }

	void PersonalAccount::message_presence_check(std::string message) const {
		bool found = false;
		for (int i = 0; i < mail.size(); i++)
			if (mail[i] == message) {
				found = true;
				break;
			}
		if (!found) {
			throw std::runtime_error("there is no such message");
		}	
	}

	int PersonalAccount::show_missing_hours() const { return missed_hours; }
}

