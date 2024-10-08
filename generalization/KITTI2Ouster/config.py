
from easydict import EasyDict as edict


_C = edict()

# data
_C.data = edict()
_C.data.dataset = 'KITTI'
_C.data.root = '/root/dataset/ouster64/vivid++'
_C.data.downsample = 0.05
_C.data.voxel_size_0 = 0.30 # Newer College
_C.data.voxel_size_1 = 0.30 # KITTI
_C.data.max_numPts = 30000 # default 30000
_C.data.manual_seed = 123

# training
_C.train = edict()
_C.train.epoch = 50
_C.train.max_iter = 50000
_C.train.batch_size = 1
_C.train.num_workers = 16
_C.train.pos_num = 512
_C.train.augmentation_noise = 0.01
_C.train.pretrain_model = ''
_C.train.all_stage = ['Ref', 'Desc', 'Keypt', 'Inlier']

# test
_C.test = edict()
_C.test.scale = _C.data.voxel_size_0 / _C.data.voxel_size_1 # 'target size / source size'
_C.test.experiment_id = '06050001'
_C.test.pose_refine = False
_C.test.all_stage = ['Ref', 'Desc', 'Keypt', 'Inlier']
_C.test.batch_size = 1

# point-wise learner
_C.point = edict()
_C.point.in_points_dim = 3
_C.point.in_feats_dim = 3
_C.point.first_feats_dim = 32
_C.point.conv_radius = 2.0
_C.point.keypts_th = 0.5
_C.point.num_keypts = 1500 # default 1500

# patch-wise embedder
_C.patch = edict()
_C.patch.des_r = 3.0
_C.patch.num_points_per_patch = 512 # default 512
_C.patch.rad_n = 3
_C.patch.azi_n = 20
_C.patch.ele_n = 7
_C.patch.delta = 0.8
_C.patch.voxel_sample = 10

# inliers && ransac
_C.match = edict()
_C.match.dist_th = 0.30
_C.match.inlier_th = 2.0
_C.match.similar_th = 0.9
_C.match.confidence = 1.0
_C.match.iter_n = 50000



def make_cfg():
    return _C
