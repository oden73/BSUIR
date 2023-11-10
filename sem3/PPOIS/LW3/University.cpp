#include "University.h"

namespace StudentInformationSystemLib {
	University::University(std::string name, std::string adress, std::string phone_number, std::vector<StudentGroup> groups, std::vector<Subject> subjects_list) : name(name), adress(adress), phone_number(phone_number), total_student_groups(groups), total_subjects_list(subjects_list) {};

	std::vector<StudentGroup> University::get_total_student_group_list() const {
		return total_student_groups;
	}
	
	std::vector<Subject> University::get_total_subjects_list() const {
		return total_subjects_list;
	}
}
