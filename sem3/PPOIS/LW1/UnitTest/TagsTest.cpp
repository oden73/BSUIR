#include "pch.h"
#include "CppUnitTest.h"
#include "Header.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{
	TEST_CLASS(UnitTest1){ //constructor
	public:
		TEST_METHOD(TestConstructor1){
			Tags::Tags t;
			map<string, bool> check_for_presence;
			check_for_presence[""] = 0;
			int tags_size = t.get_tags_size(), line_size = t.get_line_size();
			
			Assert::IsTrue(tags_size == 4);
			Assert::IsTrue(line_size == 4);
			
			for (int i = 1; i < tags_size * line_size; check_for_presence[to_string(i++)] = 0);
			for (int i = 0; i < tags_size; i++)
				for (int j = 0; j < line_size; j++)
					check_for_presence[t[i][j]] = true;
			for (auto i : check_for_presence)
				Assert::IsTrue(i.second);
		}

		TEST_METHOD(TestConstructor2) {
			Tags::Tags t;
			pair<int, int> empty_cell = t.get_empty_cell();
			Assert::IsTrue(t[empty_cell.first][empty_cell.second] == "");
		}
	};

	TEST_CLASS(UnitTest2) {
public:
	TEST_METHOD(TestOperator0) {
		Tags::Tags t1;
		Assert::IsTrue(t1.get_matrix()[0][0] == t1[0][0]);
	}
	TEST_METHOD(TestOperator1) {
		vector<vector<string>> matrix = { {"1", "2"}, {"3", ""} };
		Tags::Tags t1, t2(2, 2, matrix);
		t1 = t2;
		Assert::IsTrue(t1.get_tags_size() == 2);
		Assert::IsTrue(t1.get_line_size() == 2);
		Assert::IsTrue(t1.get_matrix() == matrix);
	}

	TEST_METHOD(TestOperator2) {
		Tags::Tags t1(1, 1, {{""}}), t2(1, 1, {{""}});
		Assert::IsTrue(t1 == t2);
	}

	TEST_METHOD(TestOperator3) {
		Tags::Tags t1(1, 1, { {""} }), t2(1, 1, { {"1"} });
		Assert::IsTrue(t1 != t2);

		Tags::Tags t3(1, 1, { {"1"} }), t4(1, 2, { {"", "1"} });
		Assert::IsTrue(t3 != t4);

		Tags::Tags t5(2, 1, { {""}, {"1"} }), t6(1, 1, { {"1"} });
		Assert::IsTrue(t5 != t6);
		}
	};

	TEST_CLASS(UnitTest3) { //movement method
		TEST_METHOD(TestMovementW) {
			Tags::Tags t1(2, 2, { {"1", ""}, {"2", "3"} });
			t1.movement('w');
			vector<vector<string>> matrix_after = { {"1", "3"}, {"2", ""} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestImpMovementW) {
			Tags::Tags t1(2, 2, { {"1", "3"}, {"2", ""} });
			t1.movement('w');
			vector<vector<string>> matrix_after = { {"1", "3"}, {"2", ""} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestMovementA) {
			Tags::Tags t1(2, 2, { {"", "1"}, {"2", "3"} });
			t1.movement('a');
			vector<vector<string>> matrix_after = { {"1", ""}, {"2", "3"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestImpMovementA) {
			Tags::Tags t1(2, 2, { {"1", ""}, {"2", "3"} });
			t1.movement('a');
			vector<vector<string>> matrix_after = { {"1", ""}, {"2", "3"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestMovementS) {
			Tags::Tags t1(2, 2, { {"1", "2"}, {"3", ""} });
			t1.movement('s');
			vector<vector<string>> matrix_after = { {"1", ""}, {"3", "2"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestImpMovementS) {
			Tags::Tags t1(2, 2, { {"1", ""}, {"2", "3"} });
			t1.movement('s');
			vector<vector<string>> matrix_after = { {"1", ""}, {"2", "3"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestMovementD) {
			Tags::Tags t1(2, 2, {{ "1", "" }, { "2", "3" }});
			t1.movement('d');
			vector<vector<string>> matrix_after = { {"", "1"}, {"2", "3"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

		TEST_METHOD(TestImpMovementD) {
			Tags::Tags t1(2, 2, { {"", "1"}, {"2", "3"} });
			t1.movement('d');
			vector<vector<string>> matrix_after = { {"", "1"}, {"2", "3"} };
			Assert::IsTrue(t1.get_matrix() == matrix_after);
		}

	};

	TEST_CLASS(UnitTest4) {
		TEST_METHOD(TestRightPosition) {
			Tags::Tags t1(2, 2, { {"1", "2"}, {"3", ""} });
			Assert::IsTrue(t1.check_position());
		}
		
		TEST_METHOD(TestNotRightPosition) {
			Tags::Tags t1(2, 2, { {"", "1"}, {"2", "3"} });
			Assert::IsFalse(t1.check_position());
		}
	};

	TEST_CLASS(UnitTest5) { 
		TEST_METHOD(TestGetTagsSize) {
			Tags::Tags t1;
			t1.set_tags_size(3);
			Assert::IsTrue(t1.get_tags_size() == 3);
		}

		TEST_METHOD(TestGetLineSize) {
			Tags::Tags t1;
			t1.set_line_size(3);
			Assert::IsTrue(t1.get_line_size() == 3);
		}

		TEST_METHOD(TestGetEmptyCell) {
			Tags::Tags t1(1, 1, {{""}});
			pair<int, int> q = {0, 0};
			Assert::IsTrue(t1.get_empty_cell() == q);
		}

		TEST_METHOD(TestGetMatrix) {
			vector<vector<string>> m = { {"1", ""}, {"2", "3"} };
			Tags::Tags t1(2, 2, m);
			Assert::IsTrue(t1.get_matrix() == m);
		}
	};

	TEST_CLASS(UnitTest6) {
		TEST_METHOD(TestSetTagsSize) {
			Tags::Tags t1;
			t1.set_tags_size(4);
			Assert::IsTrue(t1.get_matrix().size() == 4);
			t1.set_tags_size(6);
			Assert::IsTrue(t1.get_matrix().size() == 6);
		}

		TEST_METHOD(TestSetLineSize) {
			Tags::Tags t1;
			t1.set_line_size(4);
			Assert::IsTrue(t1.get_matrix()[0].size() == 4);
			t1.set_line_size(6);
			Assert::IsTrue(t1.get_matrix()[0].size() == 6);
		}

		TEST_METHOD(TestSetEmptyCell) {
			Tags::Tags t1;
			t1.set_empty_cell(0, 0);
			Assert::IsTrue(t1[0][0] == "");
		}

		TEST_METHOD(TestSetMatrix) {
			Tags::Tags t1(2, 2, { {"", "1"}, {"2", "3"}});
			vector<vector<string>> m = { {"1", ""}, {"3", "2"} };
			t1.set_matrix(m);
			Assert::IsTrue(t1.get_matrix() == m);
		}
	};
}
