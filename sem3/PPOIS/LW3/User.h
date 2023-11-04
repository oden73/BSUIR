#pragma once
#include <string>

namespace StudentInformationSystemLib {
	class User {
	public:
		User();
		User(std::string);

		bool operator==(User);

		std::string get_password() const;
		std::string get_user_name() const;
		std::string get_user_email() const;
		std::string get_name() const;

		void set_password(std::string);
	private:
	protected:
		std::string name;
		std::string user_name;
		std::string user_email;
		std::string user_password;
	};
}