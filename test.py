import unittest
import program as pr

class TestPawnshopFunctions(unittest.TestCase):

    def setUp(self):        
        self.pawnshop = {}

    def test_add_item(self):
        pr.add_item(self.pawnshop, 1, 'Item_1', 'Description_1', 100, '2000-10-10')
        self.assertIn(1, self.pawnshop)

    def test_add_item_edge_case(self):
        pr.add_item(self.pawnshop, 0, '', '', 0, '0')
        self.assertIn(0, self.pawnshop)

    def test_add_item_large_values(self):
        pr.add_item(self.pawnshop, 10000, 'Large Item', 'Description', 9999999999, '200000-10-10')
        self.assertIn(10000, self.pawnshop)  

    #def test_add_item_incorrect(self):
    #    with self.assertRaises(ValueError):
    #        pr.add_item(self.pawnshop, 'a', 'Item_1', 'Description_1', 'b', 'c')  

    def test_add_wrong_item(self):
        try:
            pr.add_item(self.pawnshop, 'a', 'Item_1', 'Description_1', 'b', 'c')  
        except ValueError:
            self.fail("Value error raised")            

    def test_get_item(self):
        pr.add_item(self.pawnshop, 1, 'Item_1', 'Description_1', 100, '2000-10-10')
        item = pr.get_item(self.pawnshop, 1)
        self.assertEqual(item['name'], 'Item_1')

    def test_get_item_empty_collection(self):
        #item = pr.get_item(self.pawnshop, 1)
        #self.assertIsNone(item)
        with self.assertRaises(ValueError):
            pr.get_item(self.pawnshop, 1)

   # def test_get_item_ValueError(self):
   #     try:
   #         pr.get_item(self.pawnshop, 1)  
   #     except ValueError:
   #         self.fail("Value error raised") 

    def test_update_item(self):
        pr.add_item(self.pawnshop, 1, 'Item_1', 'Description_1', 100, '2000-10-10')
        pr.update_item(self.pawnshop, 1, name='Updated Item', description='Updated Description')
        item = pr.get_item(self.pawnshop, 1)
        self.assertEqual(item['name'], 'Updated Item')
        self.assertEqual(item['description'], 'Updated Description')

    def test_update_item_nonexistent(self): 
        pr.update_item(self.pawnshop, 1, name='Updated Name', description='Updated Description')
        self.assertNotIn(1, self.pawnshop)

    def test_delete_item(self):
        pr.add_item(self.pawnshop, 1, 'Item_1', 'Description_1', 100, '2000-10-10')
        pr.delete_item(self.pawnshop, 1)
        self.assertNotIn(1, self.pawnshop)

    def test_delete_nonexistent_item(self):
        pr.delete_item(self.pawnshop, 1)
        self.assertNotIn(1, self.pawnshop)

if __name__ == '__main__':

    unittest.main()