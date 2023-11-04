#pragma once
#include "Student.h"
#include "Schedule.h"
#include "Teacher.h"

#include <vector>
#include <string>

namespace StudentInformationSystemLib {
	class StudentGroup {
	public:
		StudentGroup();
		StudentGroup(std::string, std::vector<Student>, std::vector<Subject>);

		bool operator==(StudentGroup) const;
		bool operator==(std::string) const;

		void add_student(Student);
		void remove_student(Student);
		void set_missing_hours(Student);

		void curator_hour();

		std::vector<Student> get_students_list() const;
		Teacher get_curator() const;
		std::vector<Subject> get_subjects() const;
		std::string get_group_number() const;
		int get_course() const;

		void set_curator(Teacher);
		void set_subjects(std::vector<Subject>);
		void set_course(int);
	private:
		std::string group_number;
		std::vector<Student> students_list;
		Teacher curator;

		void fillint_schedule(std::vector<Subject>);
	protected:
		int course;
		std::vector<Schedule> week_schedule;
	};
}