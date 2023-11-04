#include "Teacher.h"

#include <iostream>

namespace StudentInformationSystemLib {
	Teacher::Teacher() : User() {
		is_curator = false;
		taught_disciplines = { Subject("MOIS"), Subject("BGCh") };
	}

	Teacher::Teacher(std::string name, std::vector<Subject> subjects) : User(name) {
		is_curator = false;
		taught_disciplines = subjects;
	}

	void Teacher::make_interesting_lecture() {
		for (int i = 0; i < taught_disciplines.size(); i++)
			std::cout << "making interesting " << taught_disciplines[i].get_name() << "lecture... done!\n";
	}

	bool Teacher::get_is_curator() const { return is_curator; }
	std::vector<Subject> Teacher::get_taught_disciplines() const { return taught_disciplines; }

	void Teacher::set_is_curator(bool is_curator) { this->is_curator = is_curator; }
}