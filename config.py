

class DefaultConfig(object):
    train_img_dir = 'DataSets\\CityScape\\train'
    train_annot_dir = 'DataSets\\CityScape\\trainannot'
    valid_img_dir='DataSets\\CityScape\\val_350f'
    valid_annot_dir='DataSets\\CityScape\\val_350f_annot'

    train_with_ckpt = False
    logdir = "checkpoints/ckpt_swift18"
    ckpt_name = "checkpoints/ckpt_swift18/ckpt_swift18"
    ckpt_path = "checkpoints/ckpt__focalloss_weight/ckpt_test_168.pth"

    batch_size = 12
    val_batch_size = 25

    dataloader_num_worker = 0
    class_num = 21

    learning_rate = 4e-4
    max_epoch = 200

