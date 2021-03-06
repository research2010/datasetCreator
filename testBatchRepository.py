import unittest
from mock import  Mock, MagicMock, call
from BatchRepository import BatchRepository  

class testBatchRepository(unittest.TestCase):
    def setUp(self):
        self.filesystem = Mock()
        self.filesystem.joinPath = MagicMock(side_effect = lambda x,y: x + '/' + y)
        self.serializer = Mock()
        self.target = BatchRepository(self.filesystem, self.serializer)
        self.filesystem.pathExists.return_value = True


    def testSave(self):
        file1 = Mock()
        file2 = Mock()
        meta = Mock()
        batches = {'batches_1' : file1, 'data_batches_2' : file2, 'batches.meta': meta}
        self.target.save(batches, 'saveFolder')
        
        self.serializer.write.assert_has_calls([call('saveFolder/batches_1',file1),
                                          call('saveFolder/data_batches_2',file2),
                                          call('saveFolder/batches.meta',meta)], any_order=True) 
    
    def testCreateFolderIfNecessary(self):
        self.filesystem.pathExists.return_value = False
        
        self.target.save({'' : Mock()}, 'saveFolder')
        
        self.filesystem.pathExists.assert_called_with('saveFolder')
        self.filesystem.makeDir.assert_called_with('saveFolder')
        
        
        