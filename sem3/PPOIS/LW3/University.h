#pragma once
#include "StudentGroup.h"
#include "Teacher.h"

#include <string>
#include <vector>

namespace StudentInformationSystemLib {
	class University {
	public:
		University(std::string, std::string, std::string, std::vector<StudentGroup>, std::vector<Subject>);
		
		std::vector<Subject> get_total_subjects_list() const;
		std::vector<StudentGroup> get_total_student_group_list() const;
	private:
		std::string name;
		std::string adress;
		std::string phone_number;
	protected:
		std::vector<Subject> total_subjects_list;
		std::vector<StudentGroup> total_student_groups;

	};
}