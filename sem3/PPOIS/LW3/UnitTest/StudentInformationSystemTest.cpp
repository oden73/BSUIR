#include "pch.h"
#include "CppUnitTest.h"
#include "StudentInformationSystem.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace StudentInformationSystemLib;
using namespace std;

namespace StudentInformationSystemTest
{
	TEST_CLASS(StudentInformationSystemConsturctor)
	{
	public:
		
		TEST_METHOD(Constructor) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });

			vector<Student> expected_students = { Student(), Student("bbbb"), Student("rrrr"), Student("oooo"), Student("ttttt"),
				Student("a"), Student("b"), Student("c"), Student("q"), Student("w"), Student("e"), Student("r") };
			vector<Student> students = information_system.get_student_userlist();
			Assert::AreEqual(expected_students.size(), students.size());
			for (int i = 0; i < students.size(); i++) {
				Assert::IsTrue(expected_students[i] == students[i]);
			}

			vector<Teacher> expected_teachers = { Teacher(), Teacher("asd", {Subject("PPOIS")}),
								Teacher("qwe", {Subject("ChM"), Subject("MA"), Subject("LAIAG")}), Teacher("zxc", {Subject("OTIS"), Subject("TMOIS")}),
								Teacher("rty", {Subject("MSiSvIT"), Subject("Logika")}),
								Teacher("fgh", {Subject("PIOIVIS")}), Teacher("vbn", {Subject("IBG"), Subject("BGCh")}),
								Teacher("uio", {Subject("LOIS"), Subject("AOIS")}) };
			vector<Teacher> teachers = information_system.get_teacher_userlist();
			Assert::AreEqual(expected_teachers.size(), teachers.size());
			for (int i = 0; i < teachers.size(); i++) {
				Assert::IsTrue(expected_teachers[i] == teachers[i]);
			}
			
			vector<Subject> expected_subjects = { Subject(), Subject("ChM"), Subject("PPOIS"),
								Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"),
								Subject("OTIS"), Subject("IBG"), Subject("FizK"),
								Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"),
								Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") };
			vector<Subject> subjects = information_system.get_total_subjects_list();
			Assert::AreEqual(expected_subjects.size(), subjects.size());
			for (int i = 0; i < subjects.size(); i++) {
				Assert::IsTrue(expected_subjects[i] == subjects[i]);
			}

			vector<string> expected_group_numbers = { "000000", "111111", "222222" };
			vector<StudentGroup> groups = information_system.get_total_student_group_list();
			Assert::AreEqual(3, (int)groups.size());
			for (int i = 0; i < 3; i++) {
				Assert::IsTrue(groups[i] == expected_group_numbers[i]);
			}
		}
	};

	TEST_CLASS(StudentInformationSystemMethods) {
		TEST_METHOD(AddStudent) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			Student student("test");
			student.set_group_number("000000");
			information_system.add_student(student);
			Assert::IsTrue(information_system.get_student_userlist().back() == student);
		}

		TEST_METHOD(AddTeacher) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			Teacher teacher("test", {Subject("test")});
			information_system.add_teacher(teacher);
			Assert::IsTrue(information_system.get_teacher_userlist().back() == teacher);
		}

		TEST_METHOD(AddGroup) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			StudentGroup student_group("123123", { Student() }, { Subject(), Subject(), Subject(), Subject(), Subject(), Subject() });
			information_system.add_student_group(student_group);
			Assert::IsTrue(information_system.get_total_student_group_list().back() == student_group);
		}

		TEST_METHOD(RemoveStudent) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			information_system.remove_student(Student());
			vector<Student> students = information_system.get_student_userlist();
			for (int i = 0; i < students.size(); i++)
				Assert::IsFalse(Student() == students[i]);
		}
		
		TEST_METHOD(RemoveTeacher) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			information_system.remove_teacher(Teacher());
			vector<Teacher> teachers = information_system.get_teacher_userlist();
			for (int i = 0; i < teachers.size(); i++)
				Assert::IsFalse(Teacher() == teachers[i]);
		}

		TEST_METHOD(NewAcademicYear) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			StudentGroup student_group("123123", { Student() }, { Subject(), Subject(), Subject(), Subject(), Subject(), Subject() });
			student_group.set_course(4);
			information_system.add_student_group(student_group);
			StudentGroup course1_group1("999999", { Student() }, { Subject(), Subject(), Subject(), Subject(), Subject(), Subject() });
			StudentGroup course1_group2("123456", { Student() }, { Subject(), Subject(), Subject(), Subject(), Subject(), Subject() });
			course1_group1.set_course(1);
			course1_group2.set_course(1);
			vector<StudentGroup> course1_groups = { course1_group1, course1_group2 };
			information_system.new_academic_year(course1_groups);
			bool group1_presence = false, group2_presence = false;
			vector<StudentGroup> groups = information_system.get_total_student_group_list();
			for (int i = 0; i < groups.size(); i++) {
				Assert::IsFalse(groups[i] == student_group);
				if (groups[i] == course1_group1) {
					group1_presence = true;
				}
				if (groups[i] == course1_group2) {
					group2_presence = true;
				}
			}
			Assert::IsTrue(group1_presence && group2_presence);
		}

		TEST_METHOD(SettingMissedHours) {
			StudentInformationSystem information_system("BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")}) }, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") });
			information_system.add_teacher(Teacher("test", { Subject("test") }));
			StudentGroup group("test", { Student("test") }, { Subject("test"), Subject("test"), Subject("test"), Subject("test"), Subject("test"), Subject("test") });
			information_system.add_student_group(group);
			int hours_before = information_system.get_total_student_group_list().back().get_students_list()[0].show_missing_hours();
			information_system.setting_missed_hours(Teacher("test", { Subject("test") }));
			int hours_after = information_system.get_total_student_group_list().back().get_students_list()[0].show_missing_hours();
			Assert::AreEqual(hours_before + 2, hours_after);
		}
	};

	TEST_CLASS(StudentGroupMethods) {
	public:
		TEST_METHOD(RemoveStudent) {
			StudentGroup group("test", { Student("test"), Student("remove")}, {Subject("test"), Subject("test"), Subject("test"), Subject("test"), Subject("test"), Subject("test")});
			Student removable_student = Student("remove");
			group.remove_student(removable_student);
			vector<Student> students = group.get_students_list();
			for (int i = 0; i < students.size(); i++)
				Assert::IsFalse(students[i] == removable_student);
		}
	};

	TEST_CLASS(PersonalAccountAndStudentMethods) {
	public:
		TEST_METHOD(MailMethods) {
			Student student;
			student.recieve_message("123");
			student.show_message("123");
			student.recieve_message("123123");
			student.show_all_mail();
		}

		TEST_METHOD(Punishment) {
			Student student;
			student.punishment();
		}

		TEST_METHOD(PassCertificate) {
			Student student;
			int hours_before = student.show_missing_hours();
			student.pass_a_certificate();
			int hours_after = student.show_missing_hours();
			Assert::IsTrue(hours_before > hours_after);
		}
	};
}
