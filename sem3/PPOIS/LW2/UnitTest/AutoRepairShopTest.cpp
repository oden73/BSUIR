#include "pch.h"
#include "CppUnitTest.h"
#include "AutoRepairShop.h"
#include "Car.h"
#include "Motorcycle.h"
#include "Truck.h"
#include "Bus.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace AutoRepairShop;
using namespace std;

namespace AutoRepairShopTest
{
	TEST_CLASS(RepairShopConstructor)
	{
	public:	
		TEST_METHOD(RepairShopStrings){
			AutoRepairShopClass repair_shop;
			Assert::IsTrue(repair_shop.get_name() == "Repair Shop 322");
			Assert::IsTrue(repair_shop.get_adress() == "Brown st. 32");
		}

		TEST_METHOD(RepairShopVehicles) {
			AutoRepairShopClass repair_shop;
			vector<Vehicle> vehicles = { Truck("Mercedes"), Car("Mazda"),
											Car(), Motorcycle(), Bus(), Car("BMW") };
			vector<Vehicle> repair_shop_vehicles = repair_shop.get_vehicles_list();
			Assert::AreEqual(vehicles.size(), repair_shop_vehicles.size());
			for (int i = 0; i < vehicles.size(); i++)
				Assert::IsTrue(vehicles[i] == repair_shop_vehicles[i]);
		}

		TEST_METHOD(RepairShopMechanics) {
			AutoRepairShopClass repair_shop;
			vector<Mechanic> mechanics = { Rank2Mechanic("Vladislav Korolkov"),
											Rank2Mechanic() ,
											Rank1Mechanic("Egor Glyoza") ,
											Rank1Mechanic("Maksim Karpuk") ,
											Rank1Mechanic("Vyacheslav Ageenko") };
			vector<Mechanic> repair_shop_mechanics = repair_shop.get_total_mechanics_list();
			Assert::AreEqual(mechanics.size(), repair_shop_mechanics.size());
			for (int i = 0; i < mechanics.size(); i++)
				Assert::IsTrue(mechanics[i] == repair_shop_mechanics[i]);
		}
		TEST_METHOD(RepairShopEquipment) {
			AutoRepairShopClass repair_shop;
			vector<Equipment> equipment = { Equipment("Wrench", {"Car", "Truck", "Bus", "Motorcycle"}),
											Equipment("Hydraulic press", {"Car", "Truck", "Bus"}),
											Equipment("Smaller Hydraulic press", {"Motorcycle"}),
											Equipment("Machine", {"Truck", "Bus"}),
											Equipment() };
			vector<Equipment> repair_shop_equipment = repair_shop.get_equipment_list();
			Assert::AreEqual(equipment.size(), repair_shop_equipment.size());
			for (int i = 0; i < equipment.size(); i++)
				Assert::IsTrue(equipment[i] == repair_shop_equipment[i]);
		}
	};

	TEST_CLASS(RepairShopFunctions) {
		TEST_METHOD(RepairShopAddingRank1Mechanic) {
			AutoRepairShopClass repair_shop;
			Rank1Mechanic mechanic;
			repair_shop.add_new_rank1mechanic(mechanic);
			vector<Rank1Mechanic> mechanics_list = repair_shop.get_rank1mechanic_list();
			int index = -1;
			for(int i = 0; i < mechanics_list.size(); i ++)
				if (mechanics_list[i].get_name() == mechanic.get_name()) {
					index = i;
					break;
				}
			Assert::AreNotEqual(-1, index);
			string chief_name = mechanics_list[index].get_chief_name();
			vector<Rank2Mechanic> chief_list = repair_shop.get_rank2mechanic_list();
			bool found = false;
			for (int i = 0; i < chief_list.size(); i++)
				if (chief_list[i].get_name() == chief_name) {
					found = true;
					break;
				}
			Assert::IsTrue(found);
		}

		TEST_METHOD(RepairShopAddingRank2Mechanic) {
			AutoRepairShopClass repair_shop;
			Rank2Mechanic mechanic("Agu Aba");
			repair_shop.add_new_rank2mechanic(mechanic);
			vector<Rank2Mechanic> mechanics_list = repair_shop.get_rank2mechanic_list();
			bool found = false;
			for (int i = 0; i < mechanics_list.size(); i++)
				if (mechanics_list[i].get_name() == mechanic.get_name()) {
					found = true;
					break;
				}
			Assert::IsTrue(found);
		}

		TEST_METHOD(RepairShopAddingCar) {
			AutoRepairShopClass repair_shop;
			Car car("ASD");
			repair_shop.add_new_vehicle(car);
			vector<Vehicle> vehicles = repair_shop.get_vehicles_list();
			bool found = false;
			for(int i = 0; i < vehicles.size(); i ++)
				if (vehicles[i].get_name() == car.get_name() && vehicles[i].get_vehicle_type() == "Car") {
					found = true;
					break;
				}
			Assert::IsTrue(found);
		}

		TEST_METHOD(RepairShopAddingNotExistingEquipment) {
			AutoRepairShopClass repair_shop;
			Equipment equipment("ASD", {"Car"});
			repair_shop.add_new_equipment(equipment);
			vector<Equipment> equipment_list = repair_shop.get_equipment_list();
			bool found = false;
			for(int i = 0; i < equipment_list.size(); i ++)
				if (equipment_list[i] == equipment 
					&& equipment_list[i].get_vehicle_types() == equipment.get_vehicle_types()) {
					found = true;
					break;
				}
			Assert::IsTrue(found);
		}

		TEST_METHOD(RepairShopAddingExistingEquipment) {
			AutoRepairShopClass repair_shop;
			Equipment equipment("Machine", { "Truck", "Bus" });
			repair_shop.add_new_equipment(equipment);
			vector<Equipment> equipment_list = repair_shop.get_equipment_list();
			bool added = false;
			for (int i = 0; i < equipment_list.size(); i++)
				if (equipment_list[i] == equipment && equipment_list[i].get_total_amount() == 30) {
					added = true;
					break;
				}
			Assert::IsTrue(added);
		}

		TEST_METHOD(RepairShopAssignRank1Mechanic) { 
			AutoRepairShopClass repair_shop;
			repair_shop.add_new_rank1mechanic(Rank1Mechanic("asd asd"));
			repair_shop.add_new_vehicle(Motorcycle("asd"));
			bool is_fixing_before = repair_shop.get_vehicles_list().back().get_being_fixed();
			bool is_busy_before = repair_shop.get_rank1mechanic_list().back().get_is_busy();
			repair_shop.assign_free_mechanic();
			bool is_fixing_after = repair_shop.get_vehicles_list().back().get_being_fixed();
			bool is_busy_after = repair_shop.get_rank1mechanic_list().back().get_is_busy();
			Assert::IsTrue(!is_fixing_before && !is_busy_before && is_fixing_after && is_busy_after);
		}
		
		TEST_METHOD(RepairShopAssignRank2Mechanic) {
			AutoRepairShopClass repair_shop;
			repair_shop.add_new_rank2mechanic(Rank2Mechanic("asd asd"));
			repair_shop.add_new_rank2mechanic(Rank2Mechanic("asd1 asd1"));
			repair_shop.add_new_vehicle(Truck());
			bool is_fixing_before = repair_shop.get_vehicles_list().back().get_being_fixed();
			bool is_busy_before = repair_shop.get_rank2mechanic_list().back().get_is_busy();
			repair_shop.assign_free_mechanic();
			bool is_fixing_after = repair_shop.get_vehicles_list().back().get_being_fixed();
			bool is_busy_after = repair_shop.get_rank2mechanic_list().back().get_is_busy();
			Assert::IsTrue(!is_fixing_before && !is_busy_before && is_fixing_after && is_busy_after);
		}

		TEST_METHOD(RepairShopRemoveMechanic) {
			AutoRepairShopClass repair_shop;
			repair_shop.remove_rank1_mechanic(Rank1Mechanic("Maksim Karpuk"));
			vector<Rank1Mechanic> rank1mechanics = repair_shop.get_rank1mechanic_list();
			for (int i = 0; i < rank1mechanics.size(); i++)
				Assert::IsFalse(rank1mechanics[i].get_name() == "Maksim Karpuk");

			repair_shop.remove_rank2_mechanic(Rank2Mechanic("Vladislav Korolkov"));
			vector<Rank2Mechanic> rank2mechanics = repair_shop.get_rank2mechanic_list();
			for (int i = 0; i < rank2mechanics.size(); i++)
				Assert::IsFalse(rank1mechanics[i].get_name() == "Vladislav Korolkov");
		}

		TEST_METHOD(RepairShopRemoveVehicle) {
			AutoRepairShopClass repair_shop;
			vector<Vehicle> vehicles = repair_shop.get_vehicles_list();
			Vehicle removable_vehicle = vehicles[2];
			repair_shop.remove_vehicle(removable_vehicle);
			vehicles = repair_shop.get_vehicles_list();
			for (int i = 0; i < vehicles.size(); i++)
				Assert::IsFalse(vehicles[i].get_name() == removable_vehicle.get_name()
								&& vehicles[i].get_vehicle_type() == removable_vehicle.get_vehicle_type());
		}

		TEST_METHOD(RepairShopRemoveEquipment) {
			AutoRepairShopClass repair_shop;
			repair_shop.remove_equipment(Equipment("Machine", { "Truck", "Bus" }));
			vector<Equipment> equipment = repair_shop.get_equipment_list();
			for (int i = 0; i < equipment.size(); i++)
				Assert::IsFalse(equipment[i].get_name() == "Machine");
		}

		TEST_METHOD(RepairShopSendVehicle) {
			AutoRepairShopClass repair_shop;
			Rank1Mechanic mechanic = repair_shop.get_rank1mechanic_list()[0];
			Vehicle sending_vehicle = mechanic.get_vehicle();
			repair_shop.send_vehicle(mechanic);
			vector<Vehicle> vehicles = repair_shop.get_vehicles_list();
			Assert::IsFalse(repair_shop.get_rank1mechanic_list()[0].get_is_busy());
			for (int i = 0; i < vehicles.size(); i++)
				Assert::IsFalse(vehicles[i].get_name() == sending_vehicle.get_name()
					&& vehicles[i].get_vehicle_type() == sending_vehicle.get_vehicle_type());
		}
	};
}
