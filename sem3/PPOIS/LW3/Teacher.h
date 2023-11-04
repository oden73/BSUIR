#pragma once
#include "User.h"
#include "Student.h"
#include "Subject.h"

#include <string.h>
#include <vector>

namespace StudentInformationSystemLib {
	class Teacher : public User {
	public:
		Teacher();
		Teacher(std::string, std::vector<Subject>);

		void make_interesting_lecture();
		
		bool get_is_curator() const;
		std::vector<Subject> get_taught_disciplines() const;

		void set_is_curator(bool);
	private:
		std::vector<Subject> taught_disciplines;
		bool is_curator;
	};
}