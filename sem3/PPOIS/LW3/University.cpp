#include "University.h"

namespace StudentInformationSystemLib {
	University::University(std::string name, std::string adress, std::string phone_number, std::vector<StudentGroup> groups, std::vector<Subject> subjects_list) : name(name), adress(adress), phone_number(phone_number), total_student_groups(groups), total_subjects_list(subjects_list) {};
	//	/*name = "BSUIR";
	//	adress = "askjdakld";
	//	phone_number = "123123123";
	//	total_student_groups = { StudentGroup(),
	//	StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}),
	//	StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")})};
	//	total_subjects_list = { Subject(), Subject("ChM"), Subject("PPOIS"),
	//							Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"),
	//							Subject("OTIS"), Subject("IBG"), Subject("FizK"),									
	//							Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"),
	//							Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") };*/
	//	this->name = name;
	//	this->adress = adress;
	//	this->phone_number = phone_number;
	//	total_student_groups = groups;
	//	total_subjects_list = subjects_list;
	//}
	


	// "BSUIR", "askjdakld", "123123123", { StudentGroup(), StudentGroup("111111", {Student("a"), Student("b"), Student("c")}, {Subject("ChM"), Subject("PPOIS"),Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS")}), StudentGroup("222222", {Student("q"), Student("w"), Student("e"), Student("r")}, {Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("Logika"), Subject("TMOIS")})}, { Subject(), Subject("ChM"), Subject("PPOIS"), Subject("MSiSvIT"), Subject("BGCh"), Subject("MOIS"), Subject("OTIS"), Subject("IBG"), Subject("FizK"), Subject("PIOIVIS"), Subject("MA"), Subject("LOIS"), Subject("AOIS"), Subject("LAIAG"), Subject("Logika"), Subject("TMOIS") } 


	std::vector<StudentGroup> University::get_total_student_group_list() const {
		return total_student_groups;
	}
	
	std::vector<Subject> University::get_total_subjects_list() const {
		return total_subjects_list;
	}
}