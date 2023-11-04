#pragma once
#include "Subject.h"

#include <map>
#include <vector>

namespace StudentInformationSystemLib {
	class Schedule {
	public:
		Schedule();
		Schedule(std::vector<Subject>);

		void show()const;

		std::vector<Subject> get_subjects() const;
	private:
		std::vector<std::pair<std::string, Subject>> time_and_subject;
	};
}