#include "Subject.h"

#include <iostream>

namespace StudentInformationSystemLib {
	Subject::Subject() {
		name = "OKG";
		is_exam = rand() % 2;
	}

	Subject::Subject(std::string name) {
		this->name = name;
		is_exam = rand() % 2;
	}

	bool Subject::operator==(Subject other) {
		return name == other.get_name();
	}

	void Subject::show() const {
		std::cout << name << ": " << (is_exam ? "exam" : "set-off") << '\n';
	}

	std::string Subject::get_name() const { return name; }
	bool Subject::get_is_exam() const { return is_exam; }
}