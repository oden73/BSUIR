#pragma once
#include <vector>
#include <iterator>
#include <iostream>
#include <map>

using std::vector;
using std::map;

namespace OrientedGraph {
	template <typename T>
	class Graph {
	public:
		typedef T type;
		typedef vector<T> VertexList;
		typedef vector<vector<int>> AdjacencyMatrix;
		typedef typename VertexList::iterator vertex_iterator;

		Graph(vector<type> vertexes) {
			adjacency_matrix.resize(vertexes.size());
			vertex_list = vertexes;
			for (int i = 0; i < vertexes.size(); i++) {
				adjacency_matrix[i].resize(vertexes.size());
			}
		}

		bool operator==(Graph<type> other) const {
			VertexList other_vertexes = other.get_vertex_list();
			if (other_vertexes.size() != vertex_list.size()) {
				return false;
			}
			map<type, bool> element_presence;
			for (int i = 0; i < vertex_list.size(); i++)
				element_presence[vertex_list[i]] = true;
			for(int i = 0; i < other_vertexes.size(); i ++)
				if (!element_presence[other_vertexes[i]]) {
					return false;
				}
			return true;
		}
		Graph<type> operator=(Graph<type> other) {
			vertex_list = other.get_vertex_list();
			adjacency_matrix = other.get_adjacency_matrix();
			return *this;
		}

		int vertex_amount() const {
			return vertex_list.size();
		}

		int edge_amount() const {
			int edge_amount = 0;
			for (int i = 0; i < vertex_list.size(); i++)
				for (int j = 0; j < vertex_list.size(); j++)
					edge_amount += adjacency_matrix[i][j];
			return edge_amount;
		}

		int vertex_degree(type vertex) const {
			if (!vertex_presence(vertex)) {
				throw std::runtime_error("invalid vertex");	
			}
			int degree = 0;
			for(int i = 0; i < vertex_list.size(); i ++)
				if (vertex_list[i] == vertex) {
					for (int j = 0; j < vertex_list.size(); j++)
						degree += adjacency_matrix[i][j];
					return degree;
				}
		}

		int edge_degree(type first, type second) const {
			int first_index = 0, second_index = 0;
			for (int i = 0; i < vertex_list.size(); i++) {
				if (first == vertex_list[i]) {
					first_index = i;
				}
				if (second == vertex_list[i]) {
					second_index = i;
				}
			}
			return adjacency_matrix[first_index][second_index];
		}

		void add_vertex(type vertex) {
			if (vertex_presence(vertex)) {
				throw std::runtime_error("invalid vertex to add");
			}
			vertex_list.push_back(vertex);
			vector<int> edges_addition(vertex_list.size(), 0);
			for (int i = 0; i < vertex_list.size() - 1; i++)
				adjacency_matrix[i].push_back(0);
			adjacency_matrix.push_back(edges_addition);
		}

		void add_edge(type first, type second) {
			if (!vertex_presence(first) || !vertex_presence(second)) {
				throw std::runtime_error("there is no such vertex");
			}
			int first_index = 0, second_index = 0;
			for (int i = 0; i < vertex_list.size(); i++) {
				if (first == vertex_list[i]) {
					first_index = i;
				}
				if (second == vertex_list[i]) {
					second_index = i;
				}
			}
			adjacency_matrix[first_index][second_index]++;
		}

		void remove_vertex(type vertex) {
			if (!vertex_presence(vertex)) {
				throw std::runtime_error("there is no such vertex");
			}
			int index = 0;
			for(int i = 0; i < vertex_list.size(); i ++)
				if (vertex_list[i] == vertex) {
					index = i;
					break;
				}
			for (int i = 0; i < vertex_list.size(); i++)
				adjacency_matrix[i].erase(adjacency_matrix[i].begin() + index);
			adjacency_matrix.erase(adjacency_matrix.begin() + index);
			vertex_list.erase(vertex_list.begin() + index);
		}

		void remove_edge(type first, type second) {
			if (!edge_presence(first, second)) {
				throw std::runtime_error("there is no such edge");
			}
			int first_index = 0, second_index = 0;
			for (int i = 0; i < vertex_list.size(); i++) {
				if (first == vertex_list[i]) {
					first_index = i;
				}
				if (second == vertex_list[i]) {
					second_index = i;
				}
			}
			adjacency_matrix[first_index][second_index]--;
		}

		bool vertex_presence(type vertex) const {
			for (int i = 0; i < vertex_list.size(); i++)
				if (vertex == vertex_list[i]) {
					return true;
				}
			return false;
		}

		bool edge_presence(type first, type second) const {
			if (!vertex_presence(first) || !vertex_presence(second)) {
				throw std::runtime_error("there is no such vertex");
			}
			int first_index = 0, second_index = 0;
			for (int i = 0; i < vertex_list.size(); i++) {
				if (first == vertex_list[i]) {
					first_index = i;
				}
				if (second == vertex_list[i]) {
					second_index = i;
				}
			}
			if (!adjacency_matrix[first_index][second_index]) {
				return false;
			}
			return true;
		}
		
		bool empty() const { return adjacency_matrix.empty(); }

		void clear() {
			adjacency_matrix.clear();
			vertex_list.clear();
		}

		AdjacencyMatrix get_adjacency_matrix() const { return adjacency_matrix; }
		VertexList get_vertex_list() const { return vertex_list; }

		vertex_iterator begin() const { return vertex_list.begin(); }
		vertex_iterator end() const { return vertex_list.end(); }
	private:
		VertexList vertex_list;
		AdjacencyMatrix adjacency_matrix;
	};
}