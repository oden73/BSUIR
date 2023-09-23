#include "Header.h"
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

namespace Tags {
	string& Tags::TagLine::operator[](int index) {
		if (index < 0){
			throw runtime_error("invalid index");
		}
		return line_elements[index]; 
	}

	Tags::TagLine Tags::operator[](int index) {
		if (index < 0) {
			throw runtime_error("invalid index");
		}
		return matrix[index];
	}

	void Tags::operator=(Tags tags) {
		tags_size = tags.tags_size;
		line_size = tags.line_size;
		empty_cell = tags.empty_cell;
		matrix = tags.matrix;
	}

	bool Tags::operator==(Tags tags) {
		if (tags_size != tags.tags_size || line_size != tags.line_size){
			return false;
		}

		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++)
				if (matrix[i][j] != tags.matrix[i][j]) {
					return false;
				}

		return true;
	}

	bool Tags::operator!=(Tags p) {
		if (tags_size != p.tags_size || line_size != p.line_size) {
			return true;
		}

		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++)
				if (matrix[i][j] != p.matrix[i][j]) {
					return true;
				}

		return false;
	}

	Tags::Tags() {
		tags_size = 4;
		line_size = 4;
		matrix_creation();
	}

	Tags::Tags(int tags_size, int line_size, vector<vector<string>> matrix) {
		if (tags_size <= 0 || line_size <= 0 || tags_size != matrix.size() || line_size != matrix[0].size()) {
			throw runtime_error("invalid value for tags' size");
		}
		if (matrix.size() == 0 || matrix[0].size() == 0) {
			throw runtime_error("invalid matrix for tags");
		}

		this->tags_size = tags_size;
		this->line_size = line_size;
		for (int i = 0; i < matrix.size(); i++) {
			Tags::TagLine tagline;
			tagline.line_elements = matrix[i];
			this->matrix.push_back(tagline);
		}
		for (int i = 0; i < this->tags_size; i++)
			for (int j = 0; j < this->line_size; j++)
				if (matrix[i][j] == "")
					empty_cell = { i, j };
	}

	void Tags::movement(char way) {
		switch (way){
		case 'w':
			movement_up();
			break;
		case 's':
			movement_down();
			break;
		case 'a':
			movement_left();
			break;
		case 'd':
			movement_right();
			break;
		default:
			break;
		}
	}

	bool Tags::check_position() {
		int check_number = 1;
		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++) {
				if (i != j && i != tags_size - 1 && to_string(check_number) != matrix[i][j]) {
					return false;
				}
				check_number++;
			}
		return true;
	}

	int Tags::get_tags_size() { return tags_size; }
	int Tags::get_line_size() { return line_size; }
	pair<int, int> Tags::get_empty_cell() { return empty_cell; }

	vector<vector<string>> Tags::get_matrix() {
		vector<vector<string>> s;
		for (int i = 0; i < tags_size; i++)
				s.push_back(matrix[i].line_elements);
		return s;
	}

	void Tags::set_tags_size(int new_size) {
		if (new_size == tags_size) {
			return;
		}

		if (new_size < tags_size) {
			set_smaller_tags_size(new_size);
			return;
		}

		set_greater_tags_size(new_size);
	}

	void Tags::set_line_size(int new_size) {
		if (new_size == line_size) {
			return;
		}
		if (new_size < line_size) {
			set_smaller_line_size(new_size);
			return;
		}
		set_greater_line_size(new_size);
	}

	void Tags::set_empty_cell(int x, int y) {
		if (x < 0 || y < 0 || x >= tags_size || y >= line_size){
			throw runtime_error("invalid index");
		}
		string tmp = matrix[x][y];
		matrix[x][y] = "";
		matrix[empty_cell.first][empty_cell.second] = tmp;
		empty_cell = { x, y };
 	}

	void Tags::set_matrix(vector<vector<string>> new_matrix) {
		if (new_matrix.size() == 0 || new_matrix[0].size() == 0){
			throw runtime_error("invalid matrix for tags");
		}

		this->set_tags_size(new_matrix.size());
		this->set_line_size(new_matrix[0].size());
		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++) {
				matrix[i][j] = new_matrix[i][j];
				if (matrix[i][j] == "") {
					empty_cell = { i, j };
				}
			}
	}
	
	void Tags::matrix_creation() {
		TagLine tagline;
		tagline.line_elements = vector<string>(4);
		matrix = vector<TagLine>(tags_size, tagline);
		vector<pair<int, int>> matrix_indexes;
		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++)
				matrix_indexes.emplace_back(i, j);
		random_shuffle(matrix_indexes.begin(), matrix_indexes.end());

		empty_cell = matrix_indexes.back();
		for (int i = 0; i < line_size * tags_size - 1; i++) {
			int x = matrix_indexes[i].first;
			int y = matrix_indexes[i].second;
			matrix[x].line_elements[y] = to_string(i + 1);
		}
		matrix[empty_cell.first].line_elements[empty_cell.second] = "";
	}

	void Tags::movement_up() {
		if (empty_cell.first == tags_size - 1) {
			return;
		}

		int x = empty_cell.first;
		int y = empty_cell.second;
		matrix[x].line_elements[y] = matrix[x + 1].line_elements[y];
		matrix[x + 1].line_elements[y] = "";
		empty_cell.first++;
	}

	void Tags::movement_down() {
		if (empty_cell.first == 0) {
			return;
		}

		int x = empty_cell.first;
		int y = empty_cell.second;
		matrix[x].line_elements[y] = matrix[x - 1].line_elements[y];
		matrix[x - 1].line_elements[y] = "";
		empty_cell.first--;
	}

	void Tags::movement_left() {
		if (empty_cell.second == line_size - 1) {
			return;
		}

		int x = empty_cell.first;
		int y = empty_cell.second;
		matrix[x].line_elements[y] = matrix[x].line_elements[y + 1];
		matrix[x].line_elements[y + 1] = "";
		empty_cell.second++;
	}

	void Tags::movement_right() {
		if (empty_cell.second == 0) {
			return;
		}

		int x = empty_cell.first;
		int y = empty_cell.second;
		matrix[x].line_elements[y] = matrix[x].line_elements[y - 1];
		matrix[x].line_elements[y - 1] = "";
		empty_cell.second--;
	}

	void Tags::set_smaller_tags_size(int new_size) {
		if (new_size <= 0) {
			throw runtime_error("invalid value for tags' size");
		}
		tags_size = new_size;
		TagLine tagline;
		tagline.line_elements = vector<string>(line_size);
		vector<TagLine> new_matrix(new_size, tagline);
		vector<pair<int, int>> matrix_indexes;
		for (int i = 0; i < new_size; i++)
			for (int j = 0; j < line_size; j++)
					matrix_indexes.emplace_back(i, j);
		random_shuffle(matrix_indexes.begin(), matrix_indexes.end());
		empty_cell = matrix_indexes.back();
		for (int i = 0; i < line_size * tags_size - 1; i++) {
			int x = matrix_indexes[i].first;
			int y = matrix_indexes[i].second;
			new_matrix[x].line_elements[y] = to_string(i + 1);
		}
		new_matrix[empty_cell.first].line_elements[empty_cell.second] = "";
		matrix = new_matrix;
	}
	
	void Tags::set_greater_tags_size(int new_size) {
		vector<int> new_numbers;
		for (int i = tags_size * line_size; i < new_size * line_size; i++)
			new_numbers.push_back(i);
		random_shuffle(new_numbers.begin(), new_numbers.end());
		for (int i = 0; i < new_size - tags_size; i++) {
			vector<string> line_numbers;
			for (int i = 0; i < line_size; i++)
				line_numbers.push_back(to_string(new_numbers[i]));
			TagLine tagline;
			tagline.line_elements = line_numbers;
			matrix.push_back(tagline);
		}
		tags_size = new_size;
	}
	
	void Tags::set_smaller_line_size(int new_size) {
		if (new_size <= 0) {
			throw runtime_error("invalid value for tags' size");
		}
		line_size = new_size;
		TagLine tagline;
		tagline.line_elements = vector<string>(line_size);
		vector<TagLine> new_matrix(tags_size, tagline);
		vector<pair<int, int>> matrix_indexes;
		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < line_size; j++)
				matrix_indexes.emplace_back(i, j);
		random_shuffle(matrix_indexes.begin(), matrix_indexes.end());
		empty_cell = matrix_indexes.back();
		for (int i = 0; i < line_size * tags_size - 1; i++) {
			int x = matrix_indexes[i].first;
			int y = matrix_indexes[i].second;
			new_matrix[x].line_elements[y] = to_string(i + 1);
		}
		new_matrix[empty_cell.first].line_elements[empty_cell.second] = "";
		matrix = new_matrix;
	}

	void Tags::set_greater_line_size(int new_size) {
		vector<int> new_numbers;
		for (int i = tags_size * line_size; i < tags_size * new_size; i++)
			new_numbers.push_back(i);
		random_shuffle(new_numbers.begin(), new_numbers.end());
		for (int i = 0; i < tags_size; i++)
			for (int j = 0; j < new_size - line_size; j++)
				matrix[i].line_elements.push_back(to_string(new_numbers[i]));
		line_size = new_size;
	}
}

ostream& operator << (ostream& ostream, Tags::Tags tags) {
	int tags_size = tags.get_tags_size(), line_size = tags.get_line_size();
	vector<vector<string>> matrix = tags.get_matrix();
	for (int i = 0; i < tags_size; i++) {
		for (int j = 0; j < line_size; j++) {
			if (matrix[i][j] == "") {
				ostream << "# ";
			}
			else {
				ostream << matrix[i][j] << " ";
			}
		}
		ostream << "\n";
	}
	return ostream;
}

//empty cell - #
istream& operator >> (istream& istream, Tags::Tags& tags) {
	int tags_size, line_size; istream >> tags_size >> line_size;
	if (istream) {
		tags.set_tags_size(tags_size);
		tags.set_line_size(line_size);
	}

	vector<vector<string>> matrix(tags_size, vector<string>(line_size));
	for (int i = 0; i < tags_size; i++)
		for (int j = 0; j < line_size; j++) {
			istream >> matrix[i][j];
			if (matrix[i][j] == "#") {
				matrix[i][j] = "";
				tags.set_empty_cell(i, j);
			}
		}

	if (istream) {
		tags.set_matrix(matrix);
		return istream;
	}
}

void print(Tags::Tags t) {
	int tags_size = t.get_tags_size(), line_size = t.get_line_size();
	vector<vector<string>> matrix = t.get_matrix();
	for (int j = 0; j < line_size * 5 + 1; j++)
		cout << '-';
	cout << '\n';

	for (int i = 0; i < tags_size; i++) {
		cout << "|";

		for (int j = 0; j < line_size; j++) {
			for (int k = 0; k < 3 - matrix[i][j].size(); k++)
				cout << " ";
			cout << matrix[i][j] << " |";
		}

		cout << '\n';
		for (int j = 0; j < line_size * 5 + 1; j++)
			cout << '-';
		cout << '\n';
	}
}