#include "pch.h"
#include "CppUnitTest.h"
#include "OrientedGraph.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace OrientedGraph;

namespace OrientedGraphTest
{
	TEST_CLASS(UnorientedGraphTest)
	{
	public:
		
		TEST_METHOD(GraphAddVertex)
		{
			Graph<int> graph({ 1, 2, 3 });
			graph.add_vertex(4);
			Assert::AreEqual(4, graph.vertex_amount());
			Assert::IsTrue(graph.vertex_presence(4));
		}

		TEST_METHOD(GraphAddEdge) {
			Graph<int> graph({ 1, 2, 3 });
			graph.add_edge(1, 2);
			Assert::IsTrue(graph.edge_presence(1, 2));
			Assert::AreEqual(1, graph.get_adjacency_matrix()[0][1]);
		}

		TEST_METHOD(GraphRemoveVertexAndEmpty) {
			Graph<int> graph({ 1 });
			graph.remove_vertex(1);
			Assert::IsTrue(graph.empty());
			Assert::AreEqual(0, graph.vertex_amount());
		}

		TEST_METHOD(GraphRemoveEdge) {
			Graph<int> graph({ 1, 2 });
			graph.add_edge(1, 2);
			graph.remove_edge(1, 2);
			Assert::IsFalse(graph.edge_presence(1, 2));
			Assert::AreEqual(0, graph.get_adjacency_matrix()[0][1]);
		}

		TEST_METHOD(GraphClear) {
			Graph<int> graph({ 1, 2 });
			graph.clear();
			Assert::IsTrue(graph.empty());
		}

		TEST_METHOD(GraphOperator) {
			Graph<int> graph1({ 1, 2 });
			graph1.add_edge(1, 2);
			Graph<int> graph2({ 1, 2 });
			graph2.add_edge(1, 2);
			Assert::IsTrue(graph1 == graph2);
		}

		TEST_METHOD(GraphVertexDegree) {
			Graph<int> graph({ 1, 2, 3 });
			graph.add_edge(1, 2);
			graph.add_edge(1, 3);
			Assert::AreEqual(2, graph.vertex_degree(1));
		}

		TEST_METHOD(GraphEdgeDegree) {
			Graph<int> graph({ 1, 2 });
			graph.add_edge(1, 2);
			graph.add_edge(1, 2);
			Assert::AreEqual(2, graph.edge_degree(1, 2));
		}

		TEST_METHOD(GraphEdgeAmount) {
			Graph<int> graph({ 1, 2, 3 });
			graph.add_edge(1, 2);
			graph.add_edge(2, 3);
			graph.add_edge(3, 1);
			Assert::AreEqual(3, graph.edge_amount());
		}
	};
}
