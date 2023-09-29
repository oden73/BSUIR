#pragma once
#include <string>
#include <vector>
using namespace std;

namespace Tags {
	class Tags {
	public:
		class TagLine {
		public:
			string& operator[](int);
			vector<string> line_elements;
		};

		TagLine operator[](int);
		void operator=(Tags);
		bool operator==(Tags);
		bool operator!=(Tags);

		Tags();
		Tags(int, int, vector<vector<string>>);

		void movement(char);
		bool check_position();

		int get_tags_size();
		int get_line_size();
		pair<int, int> get_empty_cell();
		vector<vector<string>> get_matrix();
		
		void set_tags_size(int);
		void set_line_size(int);
		void set_empty_cell(int, int);
		void set_matrix(vector<vector<string>>);
	private:
		int tags_size;
		int line_size;
		vector<TagLine> matrix;
		pair<int, int> empty_cell;
		
		void matrix_creation();
		void movement_up();
		void movement_down();
		void movement_left();
		void movement_right();
		void set_greater_tags_size(int);
		void set_smaller_tags_size(int);
		void set_greater_line_size(int);
		void set_smaller_line_size(int);
	};
}

ostream& operator << (ostream&, Tags::Tags t);
istream& operator >> (istream&, Tags::Tags& t);
void print(Tags::Tags);