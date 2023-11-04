#pragma once
#include <string>

namespace StudentInformationSystemLib {
	class Subject {
	public:
		Subject();
		Subject(std::string);

		bool operator==(Subject);

		void show() const;

		std::string get_name() const;
		bool get_is_exam() const;
	private:
		std::string name;
		bool is_exam;
	};
}