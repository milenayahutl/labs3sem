import unittest
from rk2 import Klass, Schoolchild, SchoolchildKlass, query_1, query_2, query_3


class TestSchoolSystem(unittest.TestCase):
    def setUp(self):
        self.klasses = [
            Klass(1, "А11"),
            Klass(2, "Б10"),
            Klass(3, "А9"),
            Klass(4, "Б8"),
            Klass(5, "В7")
        ]

        self.schoolchildren = [
            Schoolchild(1, "Иванова Мария", 4.5),
            Schoolchild(2, "Петров Алексей", 4.8),
            Schoolchild(3, "Сидорова Анна", 4.2),
            Schoolchild(4, "Козлов Михаил", 4.9),
            Schoolchild(5, "Морозова Елена", 4.6),
            Schoolchild(6, "Лебедев Роман", 4.3),
            Schoolchild(7, "Федорова Ольга", 4.7),
            Schoolchild(8, "Григорьев Денис", 4.1),
        ]

        self.schoolchild_klasses = [
            SchoolchildKlass(1, 1),
            SchoolchildKlass(2, 1),
            SchoolchildKlass(3, 2),
            SchoolchildKlass(4, 2),
            SchoolchildKlass(5, 3),
            SchoolchildKlass(6, 3),
            SchoolchildKlass(7, 4),
            SchoolchildKlass(8, 5),
        ]

    def test_query_1(self):
        children_in_A, classes_A = query_1(self.klasses, self.schoolchildren, self.schoolchild_klasses)

        # Проверяем, что найдены правильные классы на 'А'
        self.assertEqual(len(classes_A), 2)  # А11 и А9
        self.assertEqual(classes_A[0].name, "А11")
        self.assertEqual(classes_A[1].name, "А9")

        # Проверяем, что найдены правильные школьники
        self.assertEqual(len(children_in_A), 4)  # 4 школьника в классах А11 и А9

        # Проверяем конкретных школьников
        student_names = [child.name for child, _ in children_in_A]
        self.assertIn("Иванова Мария", student_names)
        self.assertIn("Петров Алексей", student_names)
        self.assertIn("Морозова Елена", student_names)
        self.assertIn("Лебедев Роман", student_names)

    def test_query_2(self):
        sorted_grades = query_2(self.schoolchildren, self.schoolchild_klasses)

        self.assertEqual(len(sorted_grades), 5)  # 5 классов

        grades = [avg for _, avg in sorted_grades]
        self.assertTrue(all(grades[i] >= grades[i + 1] for i in range(len(grades) - 1)))

        #А11: Иванова (4.5) и Петров (4.8) => среднее = (4.5 + 4.8) / 2 = 4.65
        klass_id_A11 = 1
        for klass_id, avg_grade in sorted_grades:
            if klass_id == klass_id_A11:
                self.assertAlmostEqual(avg_grade, 4.65, places=2)
                break

    def test_query_3(self):
        associations = query_3(self.klasses, self.schoolchildren, self.schoolchild_klasses)

        self.assertEqual(len(associations), 8)  # 8 школьников

        class_names = [klass.name for klass, _ in associations]
        self.assertEqual(class_names, ["А11", "А11", "А9", "А9", "Б10", "Б10", "Б8", "В7"])

        first_association = associations[0]
        self.assertEqual(first_association[0].name, "А11")  # Класс
        self.assertEqual(first_association[1].name, "Иванова Мария")  # Школьник

    def test_empty_data(self):
        empty_result1, empty_classes_A = query_1([], [], [])
        self.assertEqual(len(empty_result1), 0)
        self.assertEqual(len(empty_classes_A), 0)

        empty_result2 = query_2([], [])
        self.assertEqual(len(empty_result2), 0)

        empty_result3 = query_3([], [], [])
        self.assertEqual(len(empty_result3), 0)


if __name__ == "__main__":
    unittest.main()