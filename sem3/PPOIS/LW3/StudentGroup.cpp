#include "StudentGroup.h"

#include <algorithm>
#include <iostream>

namespace StudentInformationSystemLib {
	StudentGroup::StudentGroup() {
		group_number = "000000";
		course = rand() % 4 + 1;
		week_schedule = { Schedule({Subject(), Subject("MOIS")}) ,
							Schedule({Subject("ChM"), Subject("PPOIS")}),
							Schedule({Subject("MSiSvIT"), Subject("BGCh")}),
							Schedule({Subject("MOIS"), Subject("OTIS")}),
							Schedule({Subject("IBG"), Subject("FizK")}) };
		students_list = { Student(), Student("bbbb"), Student("rrrr"), Student("oooo"), Student("ttttt") };
		for (int i = 0; i < students_list.size(); i++)
			students_list[i].set_group_number(group_number);
	}

	StudentGroup::StudentGroup(std::string group_number, std::vector<Student> students, std::vector<Subject> subjects){
		this->group_number = group_number;
		course = rand() % 4 + 1;
		fillint_schedule(subjects);
		for (int i = 0; i < students.size(); i++)
			students_list.push_back(students[i]);
		for (int i = 0; i < students_list.size(); i++)
			students_list[i].set_group_number(group_number);
	}

	bool StudentGroup::operator==(StudentGroup other) const {
		return group_number == other.get_group_number();
	}

	bool StudentGroup::operator==(std::string group_number) const {
		return this->group_number == group_number;
	}

	void StudentGroup::set_missing_hours(Student student) {
		for(int i = 0; i < students_list.size(); i ++)
			if (students_list[i] == student) {
				students_list[i].get_missing_hours();
				break;
			}
	}

	void StudentGroup::add_student(Student student) {
		for(int i = 0; i < students_list.size(); i ++)
			if (students_list[i] == student) {
				throw std::runtime_error("such student already exists in this group");
			}
		students_list.push_back(student);
	}

	void StudentGroup::remove_student(Student student) {
		int index = -1; 
		for(int i = 0; i < students_list.size(); i ++)
			if (students_list[i] == student) {
				index = i;
				break;
			}
		if (index == -1) {
			throw std::runtime_error("such student does not exist");
		}

		students_list.erase(students_list.begin() + index);
	}

	void StudentGroup::curator_hour() {
		std::cout << "how many students are there on curator hour? 2...\n then let's begin...";
	}

	std::vector<Student> StudentGroup::get_students_list() const { return students_list; }
	std::string StudentGroup::get_group_number() const { return group_number; }
	Teacher StudentGroup::get_curator() const { return curator; }
	int StudentGroup::get_course() const { return course; }
	std::vector<Subject> StudentGroup::get_subjects() const {
		std::vector<Subject> subjects;
		for (int i = 0; i < week_schedule.size(); i++) {
			std::vector<Subject> schedule_subjects = week_schedule[i].get_subjects();
			for (int j = 0; j < schedule_subjects.size(); j++)
				subjects.push_back(schedule_subjects[j]);
		}
		return subjects;
	}

	void StudentGroup::set_course(int course) { this->course = course; }
	void StudentGroup::set_curator(Teacher curator) { this->curator = curator; }
	void StudentGroup::set_subjects(std::vector<Subject> subjects){
		week_schedule.clear();
		fillint_schedule(subjects);
	}

	void StudentGroup::fillint_schedule(std::vector<Subject> subjects) {
		std::random_shuffle(subjects.begin(), subjects.end());
		for (int i = 0; i < 5; i++)
			week_schedule.push_back(Schedule({ subjects[i] }));
	}
}