#include "Schedule.h"

#include <iostream>

namespace StudentInformationSystemLib {
	Schedule::Schedule() {
		time_and_subject.emplace_back("9:00", Subject());
		time_and_subject.emplace_back("10:35", Subject("AOIS"));
		time_and_subject.emplace_back("12:25", Subject("LOIS"));
	}

	Schedule::Schedule(std::vector<Subject> subjects) {
		std::vector<std::string> time = { "9:00", "10:35", "12:25", "14:00", "15:50", "17:35", "18:25", "19:00", "20:55" };
		if (time.size() < subjects.size()) {
			throw std::runtime_error("too many subjects");
		}
		for (int i = 0; i < subjects.size(); i++)
			time_and_subject.emplace_back(time[i], subjects[i]);
	}

	std::vector<Subject> Schedule::get_subjects() const {
		std::vector<Subject> subjects;
		for (int i = 0; i < time_and_subject.size(); i++)
			subjects.push_back(time_and_subject[i].second);
		return subjects;
	}

	void Schedule::show() const {
		std::cout << "Subjects:\n";
		for (int i = 0; i < time_and_subject.size(); i++)
			std::cout << time_and_subject[i].first << " " << time_and_subject[i].second.get_name() << '\n';
	}
}