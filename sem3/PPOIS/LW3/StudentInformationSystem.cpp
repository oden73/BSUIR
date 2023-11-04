#include "StudentInformationSystem.h"

#include <iostream>
#include <algorithm>

namespace StudentInformationSystemLib {
	StudentInformationSystem::StudentInformationSystem(std::string name, std::string adress, std::string phone_number, std::vector<StudentGroup> groups, std::vector<Subject> subject_list) : Website("iis.bsuir.by"), University(name, adress, phone_number, groups, subject_list) {
		filling_students_userlist();
		teachers_userlist = { Teacher(), Teacher("asd", {Subject("PPOIS")}),
								Teacher("qwe", {Subject("ChM"), Subject("MA"), Subject("LAIAG")}), Teacher("zxc", {Subject("OTIS"), Subject("TMOIS")}),
								Teacher("rty", {Subject("MSiSvIT"), Subject("Logika")}),
								Teacher("fgh", {Subject("PIOIVIS")}), Teacher("vbn", {Subject("IBG"), Subject("BGCh")}),
								Teacher("uio", {Subject("LOIS"), Subject("AOIS")}) };
		for (int i = 0; i < total_student_groups.size(); i++)
			assign_curator_to_group(&total_student_groups[i]);
		for (int i = 0; i < teachers_userlist.size(); i++)
			add_user_to_database(teachers_userlist[i]);
	}

	void StudentInformationSystem::add_teacher(Teacher teacher) {
		add_user_to_database(teacher);
		teachers_userlist.push_back(teacher);
	}

	void StudentInformationSystem::assign_curator_to_group(StudentGroup* group) {
		for (int i = 0; i < teachers_userlist.size(); i++)
			if (!teachers_userlist[i].get_is_curator()) {
				teachers_userlist[i].set_is_curator(true);
				(*group).set_curator(teachers_userlist[i]);
				return;
			}
	}

	void StudentInformationSystem::add_student(Student new_student) {
		for (int i = 0; i < total_student_groups.size(); i++)
			if (total_student_groups[i] == new_student.get_group_number()) {
				total_student_groups[i].add_student(new_student);
				students_userlist.push_back(new_student);
				add_user_to_database(new_student);
				return;
			}
	}

	void StudentInformationSystem::setting_missed_hours(Teacher teacher) {
		std::vector<Subject> subjects = teacher.get_taught_disciplines();
		for (int i = 0; i < subjects.size(); i++) {
			std::vector<StudentGroup> groups;
			for (int j = 0; j < total_student_groups.size(); j++) {
				std::vector<Subject> group_subjects = total_student_groups[j].get_subjects();
				for(int subject = 0; subject < group_subjects.size(); subject++)
					if (group_subjects[subject] == subjects[i]) {
						groups.push_back(total_student_groups[j]);
						break;
					}
			}
			std::random_shuffle(groups.begin(), groups.end());
			for (int j = 0; j < total_student_groups.size(); j++) {
				if (total_student_groups[j] == groups[0]) {
					total_student_groups[j].set_missing_hours(total_student_groups[j].get_students_list()[0]);
					break;
				}
			}
		}
	}

	void StudentInformationSystem::remove_student(Student removable_student) {
		for(int i = 0; i < total_student_groups.size(); i ++)
			if (total_student_groups[i] == removable_student.get_group_number()) {
				total_student_groups[i].remove_student(removable_student);
				break;
			}
		int index = 0;
		for (int i = 0; i < students_userlist.size(); i++)
			if (removable_student == students_userlist[i]) {
				index = i;
				break;
			}
		students_userlist.erase(students_userlist.begin() + index);
	}

	void StudentInformationSystem::remove_teacher(Teacher removable_teacher) {
		int index = 0;
		for (int i = 0; i < teachers_userlist.size(); i++)
			if (removable_teacher == teachers_userlist[i]) {
				index = i;
				break;
			}
		teachers_userlist.erase(teachers_userlist.begin() + index);
		if (removable_teacher.get_is_curator()) {
			for (int i = 0; i < total_student_groups.size(); i++)
				if (total_student_groups[i].get_curator() == removable_teacher) {
					assign_curator_to_group(&total_student_groups[i]);
					break;
				}
		}
	}

	void StudentInformationSystem::new_academic_year(std::vector<StudentGroup> course1_groups) {
		remove_4course();
		for (int i = 0; i < total_student_groups.size(); i++) {
			std::vector<Subject> new_subjects;
			for (int j = 0; j < 5; j++)
				new_subjects.push_back(total_subjects_list[rand() % total_subjects_list.size()]);
			total_student_groups[i].set_course(total_student_groups[i].get_course() + 1);
			total_student_groups[i].set_subjects(new_subjects);
		}
		add_1course(course1_groups);
	}

	void StudentInformationSystem::send_message_to_all_students(std::string mail) {
		for (int i = 0; i < students_userlist.size(); i++)
			students_userlist[i].recieve_message(mail);
	}

	void StudentInformationSystem::withdraw_student_list() const {
		for (int i = 0; i < total_student_groups.size(); i++) {
			std::cout << "Group " << total_student_groups[i].get_group_number() << ":\n";
			std::vector<Student> students = total_student_groups[i].get_students_list();
			for (int j = 0; j < students.size(); j++)
				std::cout << j + 1 << ". " << students[i].get_name() << '\n';
		}
	}

	void StudentInformationSystem::add_user_to_database(User user) {
		get_permission(User("admin"));
		std::string user_name = user.get_user_name();
		std::string user_password = user.get_password();
		users_database[user_name] = user_password;
	}

	void StudentInformationSystem::remove_4course() {
		while (true) {
			bool found = false;
			int index = 0;
			for (int i = 0; i < total_student_groups.size(); i++)
				if (total_student_groups[i].get_course() == 4) {
					found = true;
					for (int j = 0; j < teachers_userlist.size(); j++)
						if (teachers_userlist[j] == total_student_groups[i].get_curator()) {
							teachers_userlist[j].set_is_curator(false);
							break;
						}
					std::vector<Student> students = total_student_groups[i].get_students_list();
					for (int j = 0; j < students.size(); j++) {
						users_database.erase(students[j].get_user_name());
					}
					index = i;
					break;
				}
			if (!found) {
				break;
			}
			total_student_groups.erase(total_student_groups.begin() + index);
		}
	}

	void StudentInformationSystem::add_1course(std::vector<StudentGroup> course1_groups) {
		for (int i = 0; i < course1_groups.size(); i++) {
			add_student_group(course1_groups[i]);
			assign_curator_to_group(&total_student_groups.back());
		}
	}

	void StudentInformationSystem::add_student_group(StudentGroup new_group) {
		std::vector<Subject> subjects;
			if (new_group.get_subjects().size() == 0){
				for (int i = 0; i < 5; i++)
					subjects.push_back(total_subjects_list[rand() % total_subjects_list.size()]);
			new_group.set_subjects(subjects);
		}
		total_student_groups.push_back(new_group);
		std::vector<Student> students = new_group.get_students_list();
		for (int i = 0; i < students.size(); i++)
			students_userlist.push_back(students[i]);
	}

	std::vector<Student> StudentInformationSystem::get_student_userlist() const { return students_userlist; }
	std::vector<Teacher> StudentInformationSystem::get_teacher_userlist() const { return teachers_userlist; }

	void StudentInformationSystem::filling_students_userlist() {
		for (int i = 0; i < total_student_groups.size(); i++) {
			std::vector<Student> students = total_student_groups[i].get_students_list();
			for (int j = 0; j < students.size(); j++) {
				bool found = false;
				for (int student = 0; student < students_userlist.size(); student++)
					if (students_userlist[student] == students[j]) {
						found = true;
						break;
					}
				if (!found) {
					students_userlist.push_back(students[j]);
				}
			}
		}
	}
}