# ...
from .wider_face import WIDERFaceDataset
from .xml_style import XMLDataset
### ADDING YOUR DATASET
from .my_dataset import MyDataset
__all__ = [
    'CustomDataset', 'XMLDataset', 'CocoDataset', 'VOCDataset',
    'CityscapesDataset', 'GroupSampler', 'DistributedGroupSampler',
    'build_dataloader', 'ConcatDataset', 'RepeatDataset', 'WIDERFaceDataset',
    'DATASETS', 'build_dataset','MyDataset','table','my_dataset'] # Also Add in List
