#pragma once
#include "Website.h"
#include "University.h"
#include "Subject.h"

#include <map>

namespace StudentInformationSystemLib {
	class StudentInformationSystem: public Website, public University {
	public:
		StudentInformationSystem(std::string, std::string, std::string, std::vector<StudentGroup>, std::vector<Subject>);

		void add_teacher(Teacher);
		void add_student_group(StudentGroup);
		void assign_curator_to_group(StudentGroup*);
		void add_student(Student);
		void setting_missed_hours(Teacher);
		void remove_student(Student);
		void remove_teacher(Teacher);
		void new_academic_year(std::vector<StudentGroup>);
		void send_message_to_all_students(std::string);

		void withdraw_student_list() const;

		std::vector<Student> get_student_userlist() const;
		std::vector<Teacher> get_teacher_userlist() const;
	private:
		std::vector<Student> students_userlist;
		std::vector<Teacher> teachers_userlist;
		std::map<std::string, std::string> users_database;

		void add_user_to_database(User);
		void remove_4course();
		void add_1course(std::vector<StudentGroup>);
		void filling_students_userlist();
	};
}